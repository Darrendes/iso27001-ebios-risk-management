#!/usr/bin/env python3
"""
Script d'Audit de Conformité ISO 27001 v1.0 - AMÉLIORÉ
Fictional Technology Services Company
Audit + Indicateurs de Gouvernance + KPI SMSI
"""

import json
from datetime import datetime
from collections import defaultdict
import statistics

class AuditISOConformiteV1:
    def __init__(self, organization="Fictional Technology Services Company"):
        self.organization = organization
        self.audit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.resultats = {}
        self.incidents = []  # Historique incidents
        self.vulnerabilites = []  # Vulnérabilités détectées
        
        self.statistiques = {
            "total_controles": 0,
            "conformes": 0,
            "non_conformes": 0,
            "partiellement_conformes": 0,
            "taux_conformite": 0.0
        }
        
        self.kpi = {
            "maturity_level": 0,  # 1-5 (Initial, Repeatable, Defined, Managed, Optimized)
            "risk_score": 0,  # 0-100
            "incident_rate": 0,  # incidents/mois
            "mttr": 0,  # Mean Time To Resolve
            "security_training": 0,  # % employés
        }
        
        self.controles = self.define_controles()
    
    def define_controles(self):
        """Définir 30 contrôles critiques ISO 27001 - Version allégée pour exemple"""
        return {
            # Gouvernance (A.5)
            "A.5.1": {"nom": "Politique générale SMSI", "categorie": "Gouvernance", "poids": 1, "maturity": 1},
            "A.5.2": {"nom": "Direction et support SMSI", "categorie": "Gouvernance", "poids": 1, "maturity": 1},
            "A.5.3": {"nom": "Responsabilités", "categorie": "Gouvernance", "poids": 1, "maturity": 1},
            
            # Gestion des risques (A.6)
            "A.6.1": {"nom": "Contexte SMSI", "categorie": "Risques", "poids": 2, "maturity": 2},
            "A.6.2": {"nom": "Analyse risques (EBIOS)", "categorie": "Risques", "poids": 2, "maturity": 3},
            "A.6.3": {"nom": "Traitement risques", "categorie": "Risques", "poids": 2, "maturity": 2},
            
            # Accès (A.9)
            "A.9.1": {"nom": "Politique accès", "categorie": "Accès", "poids": 2, "maturity": 2},
            "A.9.2": {"nom": "Gestion accès utilisateurs", "categorie": "Accès", "poids": 2, "maturity": 2},
            "A.9.3": {"nom": "Droits révisés", "categorie": "Accès", "poids": 1, "maturity": 2},
            "A.9.4": {"nom": "MFA", "categorie": "Accès", "poids": 2, "maturity": 3},
            "A.9.5": {"nom": "Gestion mots de passe", "categorie": "Accès", "poids": 2, "maturity": 2},
            
            # Données (A.8)
            "A.8.1": {"nom": "Classification données", "categorie": "Données", "poids": 2, "maturity": 2},
            "A.8.2": {"nom": "Traçabilité", "categorie": "Données", "poids": 1, "maturity": 2},
            
            # Chiffrement (A.11)
            "A.11.1": {"nom": "Chiffrage transit", "categorie": "Crypto", "poids": 2, "maturity": 3},
            "A.11.2": {"nom": "Chiffrage repos", "categorie": "Crypto", "poids": 2, "maturity": 3},
            
            # Infrastructure (A.14)
            "A.14.1": {"nom": "Sauvegardes", "categorie": "Infra", "poids": 2, "maturity": 3},
            "A.14.2": {"nom": "Redondance", "categorie": "Infra", "poids": 2, "maturity": 2},
            "A.14.3": {"nom": "Plan continuité", "categorie": "Infra", "poids": 2, "maturity": 3},
            
            # Développement (A.15)
            "A.15.1": {"nom": "Environnements dev", "categorie": "Dev", "poids": 2, "maturity": 2},
            "A.15.2": {"nom": "Gestion changements", "categorie": "Dev", "poids": 2, "maturity": 2},
            
            # Incidents (A.16)
            "A.16.1": {"nom": "Signalement incidents", "categorie": "Incidents", "poids": 2, "maturity": 2},
            "A.16.2": {"nom": "Gestion incidents", "categorie": "Incidents", "poids": 2, "maturity": 2},
            "A.16.3": {"nom": "Amélioration post-incident", "categorie": "Incidents", "poids": 1, "maturity": 3},
            
            # Conformité (A.18)
            "A.18.1": {"nom": "Obligations légales", "categorie": "Conformité", "poids": 2, "maturity": 2},
            "A.18.2": {"nom": "Audit interne", "categorie": "Conformité", "poids": 2, "maturity": 3},
        }
    
    def evaluer_controle(self, code_controle, statut, evidence="", notes="", duree_jours=0):
        """Évaluer un contrôle avec données supplémentaires"""
        if code_controle not in self.controles:
            print(f"⚠️ Contrôle {code_controle} non reconnu")
            return False
        
        statuts_valides = ["CONFORME", "PARTIELLEMENT", "NON_CONFORME"]
        if statut not in statuts_valides:
            print(f"❌ Statut invalide")
            return False
        
        self.resultats[code_controle] = {
            "nom": self.controles[code_controle]["nom"],
            "categorie": self.controles[code_controle]["categorie"],
            "statut": statut,
            "evidence": evidence,
            "notes": notes,
            "poids": self.controles[code_controle]["poids"],
            "maturity": self.controles[code_controle]["maturity"],
            "duree_implementation_jours": duree_jours
        }
        return True
    
    def ajouter_incident(self, date, type_incident, description, severite_1_5, temps_resolution_h):
        """Ajouter un incident pour calculer MTTR et incident rate"""
        self.incidents.append({
            "date": date,
            "type": type_incident,
            "description": description,
            "severite": severite_1_5,
            "mttr_heures": temps_resolution_h
        })
    
    def ajouter_vulnerabilite(self, code_controle, vulnerabilite, impact, remediation):
        """Ajouter une vulnérabilité détectée"""
        self.vulnerabilites.append({
            "controle": code_controle,
            "vulnerabilite": vulnerabilite,
            "impact": impact,
            "remediation": remediation
        })
    
    def calculer_maturity_level(self):
        """Calculer CMM (Capability Maturity Model) 1-5"""
        if len(self.resultats) == 0:
            return 1
        
        # Poids par statut
        poids_statut = {
            "CONFORME": 1.0,
            "PARTIELLEMENT": 0.5,
            "NON_CONFORME": 0.0
        }
        
        # Moyenne pondérée
        score_total = sum(self.resultats[c]["poids"] * poids_statut[self.resultats[c]["statut"]] 
                         for c in self.resultats)
        poids_total = sum(self.resultats[c]["poids"] for c in self.resultats)
        
        moy = score_total / poids_total if poids_total > 0 else 0
        
        # Mapping score → CMM level
        if moy >= 0.9:
            return 5  # Optimized
        elif moy >= 0.75:
            return 4  # Managed
        elif moy >= 0.5:
            return 3  # Defined
        elif moy >= 0.25:
            return 2  # Repeatable
        else:
            return 1  # Initial
    
    def calculer_risk_score(self):
        """Calculer score de risque global (0-100)"""
        if len(self.resultats) == 0:
            return 100
        
        # Risques résiduels par contrôle
        poids_risque = {
            "CONFORME": 0,
            "PARTIELLEMENT": 30,
            "NON_CONFORME": 100
        }
        
        score = sum(self.resultats[c]["poids"] * poids_risque[self.resultats[c]["statut"]] 
                   for c in self.resultats)
        poids_total = sum(self.resultats[c]["poids"] for c in self.resultats)
        
        return round(score / poids_total if poids_total > 0 else 100, 2)
    
    def calculer_statistiques(self):
        """Calculer tous les KPI"""
        total = len(self.resultats)
        if total == 0:
            return
        
        conformes = sum(1 for r in self.resultats.values() if r["statut"] == "CONFORME")
        partiels = sum(1 for r in self.resultats.values() if r["statut"] == "PARTIELLEMENT")
        non_conformes = sum(1 for r in self.resultats.values() if r["statut"] == "NON_CONFORME")
        
        taux = (conformes * 1.0 + partiels * 0.5) / total * 100
        
        self.statistiques = {
            "total_controles": total,
            "conformes": conformes,
            "partiellement_conformes": partiels,
            "non_conformes": non_conformes,
            "taux_conformite": round(taux, 2)
        }
        
        # Calculer KPI
        self.kpi["maturity_level"] = self.calculer_maturity_level()
        self.kpi["risk_score"] = self.calculer_risk_score()
        
        # MTTR (Mean Time To Resolve)
        if self.incidents:
            self.kpi["mttr"] = round(statistics.mean(i["mttr_heures"] for i in self.incidents), 2)
            self.kpi["incident_rate"] = round(len(self.incidents) / 3, 2)  # Par mois (3 mois audit)
        
        # Sécurité training (placeholder)
        self.kpi["security_training"] = 85  # À remplacer par données réelles
    
    def generer_rapport_detaille(self, output_file="audit_conformite_v1_rapport.txt"):
        """Générer rapport professionnel détaillé"""
        self.calculer_statistiques()
        
        rapport = []
        rapport.append("=" * 100)
        rapport.append("RAPPORT D'AUDIT DE CONFORMITÉ ISO 27001:2022 - VERSION 1.0")
        rapport.append("=" * 100)
        rapport.append(f"Organisation : {self.organization}")
        rapport.append(f"Date audit : {self.audit_date}")
        rapport.append("")
        
        # EXECUTIVE SUMMARY
        rapport.append("📊 EXECUTIVE SUMMARY")
        rapport.append("-" * 100)
        rapport.append(f"Taux de conformité global : {self.statistiques['taux_conformite']}%")
        rapport.append(f"Maturity Level : {self.kpi['maturity_level']}/5 ({'Initial' if self.kpi['maturity_level']==1 else 'Repeatable' if self.kpi['maturity_level']==2 else 'Defined' if self.kpi['maturity_level']==3 else 'Managed' if self.kpi['maturity_level']==4 else 'Optimized'})")
        rapport.append(f"Risk Score : {self.kpi['risk_score']}/100 ({'🔴 CRITIQUE' if self.kpi['risk_score']>60 else '🟠 ÉLEVÉ' if self.kpi['risk_score']>40 else '🟡 MOYEN' if self.kpi['risk_score']>20 else '🟢 FAIBLE'})")
        rapport.append(f"Incidents (J1-J9) : {len(self.incidents)} | MTTR Moyen : {self.kpi['mttr']}h")
        rapport.append(f"Taux de formation sécurité : {self.kpi['security_training']}% employés")
        rapport.append("")
        
        # RÉSUMÉ STATISTIQUES
        rapport.append("📋 RÉSUMÉ CONFORMITÉ")
        rapport.append("-" * 100)
        rapport.append(f"Total contrôles évalués : {self.statistiques['total_controles']}")
        rapport.append(f"✅ Conformes : {self.statistiques['conformes']} ({self.statistiques['conformes']/self.statistiques['total_controles']*100:.1f}%)")
        rapport.append(f"🟡 Partiellement conformes : {self.statistiques['partiellement_conformes']} ({self.statistiques['partiellement_conformes']/self.statistiques['total_controles']*100:.1f}%)")
        rapport.append(f"❌ Non conformes : {self.statistiques['non_conformes']} ({self.statistiques['non_conformes']/self.statistiques['total_controles']*100:.1f}%)")
        rapport.append("")
        
        # DÉTAIL PAR CATÉGORIE
        rapport.append("🏗️ CONFORMITÉ PAR CATÉGORIE")
        rapport.append("-" * 100)
        categories = defaultdict(lambda: {"total": 0, "conformes": 0})
        for code, resultat in self.resultats.items():
            cat = resultat["categorie"]
            categories[cat]["total"] += 1
            if resultat["statut"] == "CONFORME":
                categories[cat]["conformes"] += 1
        
        for cat in sorted(categories.keys()):
            total = categories[cat]["total"]
            conformes = categories[cat]["conformes"]
            pct = (conformes / total * 100) if total > 0 else 0
            barre = "█" * int(pct/5) + "░" * (20-int(pct/5))
            rapport.append(f"{cat:18} : {conformes:2}/{total:2} {barre} {pct:5.1f}%")
        
        rapport.append("")
        
        # CONTRÔLES NON-CONFORMES
        non_conformes = [c for c, r in self.resultats.items() if r["statut"] in ["NON_CONFORME", "PARTIELLEMENT"]]
        if non_conformes:
            rapport.append("⚠️ CONTRÔLES CRITIQUES À CORRIGER (PLAN D'ACTION)")
            rapport.append("-" * 100)
            for i, code in enumerate(sorted(non_conformes), 1):
                r = self.resultats[code]
                rapport.append(f"{i}. [{code}] {r['nom']} ({r['categorie']})")
                rapport.append(f"   Statut : {r['statut']}")
                if r['notes']:
                    rapport.append(f"   Notes : {r['notes']}")
                rapport.append(f"   Durée estimée correction : {r['duree_implementation_jours']} jours")
                rapport.append("")
        
        # VULNÉRABILITÉS
        if self.vulnerabilites:
            rapport.append("🔓 VULNÉRABILITÉS DÉTECTÉES")
            rapport.append("-" * 100)
            for vuln in self.vulnerabilites:
                rapport.append(f"Contrôle {vuln['controle']} : {vuln['vulnerabilite']}")
                rapport.append(f"  Impact : {vuln['impact']}")
                rapport.append(f"  Remédiation : {vuln['remediation']}")
                rapport.append("")
        
        # INCIDENTS HISTORIQUES
        if self.incidents:
            rapport.append("📌 HISTORIQUE INCIDENTS (J1-J9)")
            rapport.append("-" * 100)
            for incident in sorted(self.incidents, key=lambda x: x['date'], reverse=True):
                rapport.append(f"{incident['date']} - {incident['type']} (Sévérité {incident['severite']}/5, MTTR {incident['mttr_heures']}h)")
                rapport.append(f"  {incident['description']}")
            rapport.append("")
        
        # RECOMMANDATIONS
        rapport.append("🎯 RECOMMANDATIONS PRIORITAIRES")
        rapport.append("-" * 100)
        if self.kpi['risk_score'] > 60:
            rapport.append("1. 🔴 URGENT (< 2 semaines) : Tous 'NON_CONFORME' doivent être traités")
            rapport.append("2. Augmenter 'PARTIELLEMENT' → 'CONFORME' < 1 mois")
        elif self.kpi['risk_score'] > 40:
            rapport.append("1. IMPORTANT (< 1 mois) : Corriger 'NON_CONFORME'")
            rapport.append("2. Améliorer 'PARTIELLEMENT' < 6 semaines")
        else:
            rapport.append("1. MOYEN (< 6 semaines) : Plan d'amélioration continue")
            rapport.append("2. Audit de suivi tous les 3 mois")
        
        rapport.append(f"3. Formation sécurité annuelle (actuellement {self.kpi['security_training']}% - cible 100%)")
        rapport.append(f"4. Maturity Level {self.kpi['maturity_level']}/5 → Viser niveau 4+ en 6 mois")
        rapport.append("")
        
        rapport.append("=" * 100)
        rapport.append(f"Rapport généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        rapport.append("=" * 100)
        
        rapport_text = "\n".join(rapport)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rapport_text)
        
        print(rapport_text)
        print(f"\n✓ Rapport sauvegardé : {output_file}")
        return rapport_text
    
    def exporter_json(self, output_file="audit_conformite_v1.json"):
        """Exporter tous les résultats et KPI en JSON"""
        self.calculer_statistiques()
        
        export = {
            "audit": {
                "organisation": self.organization,
                "date": self.audit_date,
                "statistiques": self.statistiques,
                "kpi": {k: v for k, v in self.kpi.items()},
            },
            "resultats": {k: {**v, "maturity": v.get("maturity", 0)} for k, v in self.resultats.items()},
            "incidents": self.incidents,
            "vulnerabilites": self.vulnerabilites
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export, f, ensure_ascii=False, indent=2)
        
        print(f"✓ JSON exporté : {output_file}")

# ====================================================
# EXEMPLE D'UTILISATION
# ====================================================
if __name__ == "__main__":
    audit = AuditISOConformiteV1("Fictional Technology Services Company")
    
    print("🔍 AUDIT CONFORMITÉ ISO 27001 v1.0 - SCÉNARIO RÉALISTE\n")
    
    # Évaluer contrôles
    audit.evaluer_controle("A.5.1", "CONFORME", "Politique_SMSI_Generale.docx signé", "Approved J6", 0)
    audit.evaluer_controle("A.5.2", "CONFORME", "", "CTO responsable", 0)
    audit.evaluer_controle("A.6.1", "PARTIELLEMENT", "EBIOS RM en cours", "Finalisé J9", 3)
    audit.evaluer_controle("A.6.2", "CONFORME", "Matrice EBIOS 20 scénarios", "", 0)
    audit.evaluer_controle("A.9.1", "CONFORME", "Politique accès rédigée", "", 0)
    audit.evaluer_controle("A.9.4", "PARTIELLEMENT", "MFA déployée ERP/BD, manque sur email", "Complét J8", 2)
    audit.evaluer_controle("A.8.1", "CONFORME", "Classification données définie", "", 0)
    audit.evaluer_controle("A.14.1", "NON_CONFORME", "Pas de plan sauvegarde", "URGENT déployer J7", 7)
    audit.evaluer_controle("A.14.3", "NON_CONFORME", "Plan continuité inexistant", "À créer J8-J9", 5)
    audit.evaluer_controle("A.16.2", "PARTIELLEMENT", "Procédure incident, pas de tests", "Test plan J9", 3)
    
    # Ajouter incidents (exemples simples)
    audit.ajouter_incident("2026-05-15", "Tentative phishing", "Email usurpant CEO", 2, 4)
    audit.ajouter_incident("2026-05-20", "Accès non autorisé", "Compte ex-employé actif", 4, 24)
    audit.ajouter_incident("2026-05-25", "Configuration erreur", "Bucket S3 public 2h", 1, 2)
    
    # Ajouter vulnérabilités
    audit.ajouter_vulnerabilite("A.14.1", "Aucune sauvegarde hors-site", "Perte totale données", "Backup immédiat + offsite")
    audit.ajouter_vulnerabilite("A.9.4", "Email sans MFA", "Brèche comptes email", "Déployer MFA toutes apps")
    
    # Générer rapports
    audit.generer_rapport_detaille("audit_conformite_v1_rapport.txt")
    audit.exporter_json("audit_conformite_v1.json")
    
    print("\n" + "="*80)
    print("KPI GOUVERNANCE SMSI")
    print("="*80)
    print(f"Taux de conformité : {audit.statistiques['taux_conformite']}%")
    print(f"Maturity Level : {audit.kpi['maturity_level']}/5")
    print(f"Risk Score : {audit.kpi['risk_score']}/100")
    print(f"MTTR Moyen : {audit.kpi['mttr']}h")
    print(f"Incident Rate : {audit.kpi['incident_rate']}/mois")
    print("="*80)
