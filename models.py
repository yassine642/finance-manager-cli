import json
import os
from datetime import datetime

class PortfolioFinance:
    def __init__(self, nom_utilisateur, fichier_data="data.json"):
        self.nom_utilisateur = nom_utilisateur
        self.fichier_data = fichier_data
        self.solde = 0.0
        self.transactions = []
        self.charger_donnees()  # Charge automatiquement les données au démarrage

    def ajouter_transaction(self, description, montant, categorie):
        if montant == 0:
            return False
        
        self.solde += montant
        transac = {
            "description": description,
            "montant": montant,
            "categorie": categorie,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        self.transactions.append(transac)
        self.sauvegarder_donnees()  # Sauvegarde automatique après chaque modification
        return True

    def sauvegarder_donnees(self):
        """Enregistre le solde et les transactions dans un fichier JSON."""
        data = {
            "nom_utilisateur": self.nom_utilisateur,
            "solde": self.solde,
            "transactions": self.transactions
        }
        with open(self.fichier_data, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def charger_donnees(self):
        """Recharge les données depuis le fichier JSON s'il existe."""
        if os.path.exists(self.fichier_data):
            try:
                with open(self.fichier_data, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.solde = data.get("solde", 0.0)
                    self.transactions = data.get("transactions", [])
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier JSON : {e}")

class Transaction:
    def __init__(self, description, montant, categorie):
        self.description = description
        self.montant = montant  # Positif (revenu) ou négatif (dépense)
        self.categorie = categorie
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def __repr__(self):
        signe = "+" if self.montant > 0 else ""
        return f"[{self.date}] {self.description} ({self.categorie}) : {signe}{self.montant:.2f} €"


class PortfolioFinance:
    def __init__(self, nom_utilisateur, fichier_data="data.json"):
        self.nom_utilisateur = nom_utilisateur
        self.fichier_data = fichier_data
        self.solde = 0.0
        self.transactions = []
        self.charger_donnees()  # Charge automatiquement les données au démarrage

    def ajouter_transaction(self, description, montant, categorie):
        if montant == 0:
            return False
        
        self.solde += montant
        transac = {
            "description": description,
            "montant": montant,
            "categorie": categorie,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        self.transactions.append(transac)
        self.sauvegarder_donnees()  # Sauvegarde automatique après chaque modification
        return True

    def sauvegarder_donnees(self):
        """Enregistre le solde et les transactions dans un fichier JSON."""
        data = {
            "nom_utilisateur": self.nom_utilisateur,
            "solde": self.solde,
            "transactions": self.transactions
        }
        with open(self.fichier_data, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def charger_donnees(self):
        """Recharge les données depuis le fichier JSON s'il existe."""
        if os.path.exists(self.fichier_data):
            try:
                with open(self.fichier_data, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.solde = data.get("solde", 0.0)
                    self.transactions = data.get("transactions", [])
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier JSON : {e}")
                

    def ajouter_transaction(self, description, montant, categorie):
        if montant == 0:
            print("Le montant ne peut pas être nul.")
            return False
        
        self.solde += montant
        nouvelle_transac = Transaction(description, montant, categorie)
        self.transactions.append(nouvelle_transac)
        print(f"-> Operation enregistree. Nouveau solde : {self.solde:.2f} €")
        return True

    def simuler_epargne(self, montant_mensuel, taux_annuel, duree_annees):
        """Simule les intérêts composés (boucle for)."""
        solde_simule = self.solde
        taux_mensuel = (taux_annuel / 100) / 12
        mois_totaux = duree_annees * 12

        print(f"\n--- Simulation d'epargne sur {duree_annees} ans ---")
        for mois in range(1, mois_totaux + 1):
            solde_simule += montant_mensuel
            solde_simule += solde_simule * taux_mensuel
            
            if mois % 12 == 0:
                annee = mois // 12
                print(f"Annee {annee} : {solde_simule:.2f} €")
        
        return solde_simule