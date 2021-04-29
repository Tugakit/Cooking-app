from tkinter import *
import webbrowser

def web():
    webbrowser.open_new("127.0.0.1")

#Créer une premiere fenetre
window = Tk()

#Titre de la fenetre et personalisation
window.title("Login")
window.geometry("600x800")
window.minsize(600,800)
window.config(background="#1b1717")

#frame
frame = Frame(window, bg="#1b1717") #bd=1, relief=SUNKEN pour avoir un peu de reliefe dans la boite

#Afficher du texte
texte1 = Label(window, text="Bienvenue sur l'application", font=("Courrier", 30), bg="#1b1717", fg="white")
texte1.pack(side=TOP)

#Ajouter un autre texte
texte1 = Label(frame, text="Se connecter", font=("Courrier", 25), bg="#1b1717", fg="white")
texte1.pack(expand=YES)

#ajouter un bouton
bouton1 = Button(frame, text="Login", font=("Courrier", 25), bg="#ce1212", fg="#1b1717", command=web)
bouton1.pack(expand=YES, pady=25, fill=X )

frame.pack(expand=YES)

#Boucle d'affichage
window.mainloop()
