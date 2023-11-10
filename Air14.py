#~~> MrRøølåÐe <~~#
""" programme qui célèbre votre victoire."""

import random
import tkinter as tk

exercises= [f"Air{num:02d}.py" for num in range(14)]

def display_action(action):
    sep = 8* "-*-*"
    result_label_1.config(text=f"{sep}\n {action}")

def gage(result):
    
    action ={
          0 : "Split était facile",
          1 : "Split en fonction était simple",
          2 : "Concat plutôt cool",
          3 : "Chercher l'intrus,\n toujours pas trouvé",
          4 : "Un seul à la fois,\n et pas un de plus !",
          5 : "Sur chacun d'entre eux,\n pas de bol c'est à coté du bol",
          6 : "Contrôle de pass sanitaire\n c'est du passé",
          7 : "Insertion dans un tableau trié,\n là ça commence",
          8 : "Melanger 2 tableaux triés,\n on y est",
          9 : "Rotation vers la gauche\n Insoumis ?",
          10 : "Afficher le contenu,\n interressant !",
          11 : "Afficher une pyramide!\n et pourquoi pas la Lune...",
          12 : "Le Roi des tris, ouf \nc'est pas game of trône",
          13 : "Meta Exercice, ouf satisfaction\n beaucoup d'étude pour celui-ci ",
          14 : "J'ai terminé l'épreuve de l'Air et\n c'était pas loin de la tempête",
    }
    coment = action[result]
    display_action(coment)

def lancer_de_de():
    de_six_faces = [int for int in range(15)]
    result = random.choice(de_six_faces)
    result_label.config(text=f"Air{result:02d}")
    gage(result)

# Créez une fenêtre
window = tk.Tk()
window.title("Lanceur de Dé")
# Définissez les dimensions de la fenêtre (largeur x hauteur + position_x + position_y)
window.geometry("400x150")
# Calculez les dimensions de la fenêtre centrée sur l'écran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 400) // 2
y = (screen_height - 300) // 2
window.geometry(f"400x150+{x}+{y}")

# Créez un bouton pour lancer le dé
roll_button = tk.Button(window, text="Lancer le Dé", command=lancer_de_de, bg="grey")
roll_button.pack(side="bottom", anchor="center",fill="x")

# Créez une étiquette pour afficher le résultat
result_label = tk.Label(window, text="", font=("Helvetica", 20),width=100)
result_label_1 = tk.Label(window, text="", font=("Helvetica", 14),width=200)
result_label.pack()
result_label_1.pack()

# Mettez à jour la fenêtre
window.update_idletasks()

# Lancez la boucle principale de l'interface graphique
window.mainloop()