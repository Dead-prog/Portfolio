import customtkinter as ctk
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import threading

class app(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Analyseur de donnée")
        self.geometry("900x400")
        self._max_width = 900
        self._max_height = 400

        #separation des deux partie
        # Une ligne verticale de 2 pixels de large et 300 pixels de haut
        self.ligne_v = ctk.CTkFrame(self, height=400, width=2, fg_color="gray")
        self.ligne_v.place(x=250, y=0)

        self.titre()
        self.port()
        self.plage()
        self.nom_courbe()
        self.bouton_lire()
        self.btn_creer_courbe()

    def titre(self):
        self.titre = ctk.CTkLabel(
            self,
            text="Paramèttre",
            font=("Arial", 30),
        )
        self.titre.place(x=40, y=20)

    def port(self):
        # Liste des ports
        self.option = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"]

        # Création du menu défilant
        self.menu = ctk.CTkOptionMenu(
            self,
            values=self.option,
            width=200,
        )

        # Positionnement précis à X=50, Y=50
        self.menu.place(x=20, y=80)

    def plage(self):
        self.box1 = ctk.CTkEntry(
            self,
            height=20,
            width=80,
            justify="center",
            state="normal",
        )
        self.box1.place(x=20, y=130)

        self.texte = ctk.CTkLabel(
            self,
            text="à"
        )
        self.texte.place(x=120, y=130)

        self.box2 = ctk.CTkEntry(
            self,
            height=20,
            width=80,
            justify="center",
            state="normal",
        )
        self.box2.place(x=140, y=130)

    def bouton_lire(self):
        self.btn_lire = ctk.CTkButton(
            self,
            text="Lire les valeur",
            width=200,
            command=self.fonc_btn1
        )
        self.btn_lire.place(x=20, y=220)

    def fonc_btn1(self):
        # 1. On récupère le port sélectionné par l'utilisateur
        self.port_choisi = self.menu.get()
        print(f"[Système] Bouton cliqué. Tentative sur le port : {self.port_choisi}")

        try:
            self.donnee = donnee(self.port_choisi, int(self.box2.get()))
            print(f"Connexion réussie sur {self.port_choisi}")


        except serial.SerialException as e:
            print(f"Erreur de connexion : {e}")
        except ValueError as e:
            print(f"Erreur de connexion : {e}")

    def nom_courbe(self):
        self.nom = ctk.CTkEntry(
            self,
            height=30,
            width=200,
            justify="center",
            placeholder_text="Nom de la courbe"
        )
        self.nom.place(x=20, y=170)

    def btn_creer_courbe(self):
        self.btn = ctk.CTkButton(
            self,
            text="Creer la courbe",
            width=200,
            command=self.fonc_btn2
        )
        self.btn.place(x=20, y=270)

    def fonc_btn2(self):
        try:
            self.y_donnee = self.donnee.valeurs
            self.x_donnee = list(range(len(self.y_donnee)))

            self.fig, self.ax = plt.subplots(figsize=(6, 3.8))
            # Configuration de base des axes
            self.ax.set_title(self.nom.get())
            self.ax.set_xlabel("plage de valeur choisie")
            self.ax.set_ylabel("Valeurs")
            self.ax.plot(self.x_donnee, self.y_donnee, "b-o")
            self.ax.grid(True)

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(
                x=260, y=10, width=600, height=380)

        except AttributeError as e:
            print(f"Erreur de connexion : {e}")



class donnee():
    def __init__(self, port_choisi, limite):
        self.serial = serial.Serial(
            port=port_choisi,
            baudrate=9600,
            timeout=1
        )

        self.limite = limite
        self.valeurs = []
        self.nb = 0

        self.thread = threading.Thread(
            target=self.lire_ligne,
            daemon=True
        )
        self.thread.start()

    def lire_ligne(self):

        while self.nb < int(self.limite):
            self.ligne = self.serial.readline()

            if self.ligne:
                try:
                    self.valeur = int(self.ligne)
                    self.valeurs.append(self.valeur)
                    print(self.valeur)
                except ValueError:
                    print("Donnée invalide :", self.ligne)

            self.nb += 1

        print(self.valeurs)
        self.serial.close()
        self.actif = False



class courbe():
    def __init__(self, nom_courbe, y_min_value, y_max_value, y_donnee):

        self.nom_courbe = nom_courbe
        self.y_min_value = y_min_value
        self.y_max_value = y_max_value
        self.y_donnee = y_donnee

        #activation du mode interractif
        plt.ion()

        self.fig, self.ax = plt.subplots(figsize=(6, 3.8))

        self.ax.set_ylim(
            int(self.y_min_value),
            int(self.y_max_value)
        )

        self.ax.set_xlim(
            int(self.y_min_value),
            int(self.y_max_value)
        )

        # Configuration de base des axes
        self.ax.set_title(self.nom_courbe)
        self.ax.set_xlabel("index des valeur")
        self.ax.set_ylabel("Plage de valeur choisie")
        self.ax.grid(True)




if __name__ == "__main__":
    app = app()
    app.mainloop()