from datetime import datetime

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
    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur
        self.solde = 0.0
        self.transactions = []

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