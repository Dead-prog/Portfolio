import os

class Recette:

    def __init__(self):
        os.makedirs("Recette", exist_ok=True)
        reponse = self.begin()

        # gestion des recette
        if reponse == 1:
            try:
                self.recette_name = str(input("\nDonnez le nom de la recette: "))
            except ValueError:
                print("Veulliez entrez un non valide")
            self.add_recette(self.recette_name)
        elif reponse == 2:
            try:
                self.recette_to_edit = str(input("Quelle recette voulez vous réecrire: "))
            except ValueError:
                print("Veulliez entrez un nom de recette valide")
            self.edit_recette(self.recette_to_edit)
        elif reponse == 3:
            self.recette_to_read = str(input("Quelle recette voulez vous lire: "))
            self.read_recette(self.recette_to_read)
        elif reponse == 4:
            self.recette_to_delete = str(input("Quelle recette voulez vous supprimer: "))
            self.delete_recette(self.recette_to_delete)
        elif reponse == 5:
            print("Voici les recette enregistré")

            print(self.nb_recette())

            print(f"il ya donc {len(self.nb_recette())} recette")

    def begin(self):
        print("Bienvenue sur votre gestionnaire de recette")
        print("1- Ajoutez une recette")
        print("2- réecrire une recette")
        print("3- Lire une recette")
        print("4- supprimer une recette")
        print("5- voire les recette enregistrer" + "\n")

        while True:
            try:
                answer = int(input("Que voulez-vous faire: "))
                if 1 <= answer <= 6:
                    return answer
                else:
                    print("Veuillez entrer un nombre entre 1 et 6.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    # fonction pour ajouter une recette
    def add_recette(self, name):
        with open(f"Recette/{name}.txt", "w+") as file:
            file.write("INGREDIENT" + "\n" + "\n")

            while True:
                try:
                    self.nb_ingredient = int(input("Combien y'a t-il d'ingredient: "))
                    if self.nb_ingredient <= 0:
                        break
                    else:
                        print("le nombre ne peut pas etre inferieur a 0")
                except ValueError:
                    print("Veuillez entrer un nombre d'ingredients valide.")

            for i in range(self.nb_ingredient):
                self.ingredient = input(f"\ningredient {i + 1}: ")
                file.write(self.ingredient + "\n")

            file.write("\nETAPE A SUIVRE" + "\n" + "\n")

            while True:
                try:
                    self.nb_etape = int(input("Combien y'a t-il d'etape: "))
                    if self.nb_etape <= 0:
                        break
                    else:
                        print("le nombre ne peut pas etre inferieur a 0")
                except ValueError:
                    print("Veuillez entrer un nombre d'ingredients valide.")

            for i in range(self.nb_etape):
                self.etape = input(f"\netape {i + 1}: ")
                file.write(self.etape + "\n")

        print("Recette enregistré \n")

    # fonction pour modifier une recette
    def edit_recette(self, name):
        with open(f"Recette/{name}.txt", "w+") as file:
            file.write("INGREDIENT" + "\n" + "\n")

            while True:
                try:
                    self.nb_ingredient = int(input("Combien y'a t-il d'ingredient: "))
                    if self.nb_ingredient >= 0:
                        break
                    else:
                        print("le nombre ne peut pas etre inferieur a 0")
                except ValueError:
                    print("Veuillez entrer un nombre d'ingredients valide.")

            for i in range(self.nb_ingredient):
                self.ingredient = input(f"\ningredient {i + 1}: ")
                file.write(self.ingredient + "\n")

            file.write("\nETAPE A SUIVRE" + "\n" + "\n")

            while True:
                try:
                    self.nb_etape = int(input("Combien y'a t-il d'etape: "))
                    if self.nb_etape <= 0:
                        break
                    else:
                        print("le nombre ne peut pas etre inferieur a 0")
                except ValueError:
                    print("Veuillez entrer un nombre d'ingredients valide.")

            for i in range(self.nb_etape):
                self.etape = input(f"\netape {i + 1}: ")
                file.write(self.etape + "\n")

        print("Recette modifié \n")

    # fonction pour lire une recette
    def read_recette(self, name):
        with open(f"Recette/{name}.txt", "r") as file:
            print("\n" + file.read())

        print("Fin de la lecture \n")

    # fonction pour supprimer une recette
    def delete_recette(self, name):
        os.remove(f"Recette/{name}.txt")

        print("Recette supprimé \n")

    def nb_recette(self):
        self.count_recette = os.listdir("Recette")
        return self.count_recette

running = True

while running:
    Recette()

    try:
        user_exit = input("Voulez-vous sortir (oui ou non): ").lower()
        if user_exit == "oui":
            running = False
        elif user_exit != "non":
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
    except ValueError:
        print("Veulliez entrer des character valide ")
