import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

#configuration de la window
root = ctk.CTk()
root.title("Visualiseur de Fonction")
root.geometry("800x600")

#Titre
ctk.CTkLabel(root, text="Visualiseur de fonction", font= ("Arial", 25)).pack(pady=5)

fig, ax = plt.subplots()

def draw():
    try:
        func = str(fonc.get())

        x = np.linspace(-10, 10, 1000)
        y = eval(func)

        ax.clear()
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("y = " + func)
        ax.grid(True)

        canvas.draw()
    except SyntaxError:
        messagebox.showerror("Erreur", "Pour une fonction valide vous devez mettre: \n 5*x pas 5x ; \n x pas X; \n 5**2 pas 5² \n et il est imperatif de mettre un x (une variable celle si doit etre x et rien d'autre) ")
    except ValueError:
        messagebox.showerror("Erreur", "Pour une fonction valide vous devez mettre: \n 5*x pas 5x ; \n x pas X; \n 5**2 pas 5² \n et il est imperatif de mettre un x (une variable celle si doit etre x et rien d'autre) ")
    except NameError:
        messagebox.showerror("Erreur", "la variable doit s'appeler x et rien d'autre")

canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side="bottom", fill="both", expand=True)

#frame, entry, btn
Ffonc = ctk.CTkFrame(root, width=400, height=30)
Ffonc.pack(pady=5)

fonc = ctk.CTkEntry(Ffonc, width=200)
fonc.pack(side="left")

btn = ctk.CTkButton(Ffonc, text="Appliquer", command=draw)
btn.pack()

root.mainloop()