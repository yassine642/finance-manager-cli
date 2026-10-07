import customtkinter as ctk
from models import PortfolioFinance
from stats import afficher_graphique_depenses  # si placé dans stats.py

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FinanceAppGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestionnaire de Budget Personel")
        self.geometry("500x600")

        self.portefeuille = PortfolioFinance("Utilisateur")

        # --- En-tête : Solde ---
        self.lbl_titre = ctk.CTkLabel(self, text="Solde Actuel", font=("Arial", 16))
        self.lbl_titre.pack(pady=(20, 5))

        self.lbl_solde = ctk.CTkLabel(self, text=f"{self.portefeuille.solde:.2f} €", font=("Arial", 32, "bold"))
        self.lbl_solde.pack(pady=(0, 20))

        # --- Champs de saisie ---
        self.entry_desc = ctk.CTkEntry(self, placeholder_text="Description (ex: Course)")
        self.entry_desc.pack(pady=10, fill="x", padx=40)

        self.entry_montant = ctk.CTkEntry(self, placeholder_text="Montant (ex: -35.50 ou 1200)")
        self.entry_montant.pack(pady=10, fill="x", padx=40)

        self.entry_cat = ctk.CTkEntry(self, placeholder_text="Catégorie (ex: Nourriture, Salaire)")
        self.entry_cat.pack(pady=10, fill="x", padx=40)

        # --- Boutons ---
        self.btn_ajouter = ctk.CTkButton(self, text="Ajouter Transaction", command=self.action_ajouter)
        self.btn_ajouter.pack(pady=15, fill="x", padx=40)

        self.btn_graphique = ctk.CTkButton(self, text="📊 Voir Graphique Dépenses", fg_color="green", command=self.action_graphique)
        self.btn_graphique.pack(pady=10, fill="x", padx=40)

    def action_ajouter(self):
        try:
            desc = self.entry_desc.get().strip()
            montant = float(self.entry_montant.get())
            cat = self.entry_cat.get().strip()

            if desc and cat:
                if self.portefeuille.ajouter_transaction(desc, montant, cat):
                    # Mise à jour de l'affichage du solde
                    self.lbl_solde.configure(text=f"{self.portefeuille.solde:.2f} €")
                    
                    # Réinitialisation des champs
                    self.entry_desc.delete(0, 'end')
                    self.entry_montant.delete(0, 'end')
                    self.entry_cat.delete(0, 'end')
        except ValueError:
            print("Veuillez entrer un montant valide.")

    def action_graphique(self):
        afficher_graphique_depenses(self.portefeuille.transactions)

if __name__ == "__main__":
    app = FinanceAppGUI()
    app.mainloop()