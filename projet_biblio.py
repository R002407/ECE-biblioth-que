import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


#       BASE DE DONNÉES


def create_db():
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lecteurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            date_naissance TEXT NOT NULL,
            adresse TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()



#       FONCTIONS CRUD


def enregistrer():
    nom_val = nom_entry.get()
    prenom_val = prenom_entry.get()
    date_val = date_entry.get()
    adresse_val = adresse_entry.get()

    if nom_val == "" or prenom_val == "" or date_val == "" or adresse_val == "":
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
        return

    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lecteurs (nom, prenom, date_naissance, adresse) VALUES (?, ?, ?, ?)",
                   (nom_val, prenom_val, date_val, adresse_val))
    conn.commit()
    conn.close()

    messagebox.showinfo("Succès", "Lecteur enregistré avec succès.")
    vider_champs()


def supprimer():
    id_val = id_entry.get()

    if id_val == "":
        messagebox.showwarning("Erreur", "Veuillez entrer un ID.")
        return

    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lecteurs WHERE id=?", (id_val,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Succès", "Lecteur supprimé.")
    vider_champs()


def modifier():
    id_val = id_entry.get()
    nom_val = nom_entry.get()
    prenom_val = prenom_entry.get()
    date_val = date_entry.get()
    adresse_val = adresse_entry.get()

    if id_val == "":
        messagebox.showwarning("Erreur", "Veuillez entrer un ID.")
        return

    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE lecteurs 
        SET nom=?, prenom=?, date_naissance=?, adresse=?
        WHERE id=?
    """, (nom_val, prenom_val, date_val, adresse_val, id_val))

    conn.commit()
    conn.close()

    messagebox.showinfo("Succès", "Lecteur modifié.")
    vider_champs()


def consulter():
    id_val = id_entry.get()

    if id_val == "":
        messagebox.showwarning("Erreur", "Veuillez entrer un ID.")
        return

    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecteurs WHERE id=?", (id_val,))
    result = cursor.fetchone()
    conn.close()

    if result:
        nom_entry.delete(0, END)
        prenom_entry.delete(0, END)
        date_entry.delete(0, END)
        adresse_entry.delete(0, END)

        nom_entry.insert(END, result[1])
        prenom_entry.insert(END, result[2])
        date_entry.insert(END, result[3])
        adresse_entry.insert(END, result[4])
    else:
        messagebox.showinfo("Info", "Aucun lecteur trouvé pour cet ID.")


def vider_champs():
    id_entry.delete(0, END)
    nom_entry.delete(0, END)
    prenom_entry.delete(0, END)
    date_entry.delete(0, END)
    adresse_entry.delete(0, END)



#       INTERFACE GRAPHIQUE (Tkinter)


root = Tk()
root.title("Gestion des lecteurs - Bibliothèque")
img = Image.open("background.jpg")
bg = ImageTk.PhotoImage(img)
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#root.geometry("460x350")
#root.resizable(False, False)
window_width = 600
window_height = 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w // 2) - (window_width // 2)
y = (screen_h // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.geometry(f"{int(screen_w * 0.9)}x{int(screen_h * 0.9)}")

root.resizable(True, True)

# Labels
Label(root, text="ID lecteur :").grid(row=0, column=1, padx=10, pady=10, sticky=W)
Label(root, text="Nom :").grid(row=1, column=1, padx=10, pady=10, sticky=W)
Label(root, text="Prénom :").grid(row=2, column=1, padx=10, pady=10, sticky=W)
Label(root, text="Date de naissance :").grid(row=3, column=1, padx=10, pady=10, sticky=W)
Label(root, text="Adresse :").grid(row=4, column=1, padx=10, pady=10, sticky=W)

# Entrées
id_entry = Entry(root, width=30)
nom_entry = Entry(root, width=30)
prenom_entry = Entry(root, width=30)
date_entry = Entry(root, width=30)
adresse_entry = Entry(root, width=30)

id_entry.grid(row=0, column=2)
nom_entry.grid(row=1, column=2)
prenom_entry.grid(row=2, column=2)
date_entry.grid(row=3, column=2)
adresse_entry.grid(row=4, column=2)

# Boutons
Button(root, text="Enregistrer", width=12, command=enregistrer).grid(row=6, column=0, pady=15)
Button(root, text="Modifier", width=12, command=modifier).grid(row=6, column=1)
Button(root, text="Supprimer", width=12, command=supprimer).grid(row=7, column=0)
Button(root, text="Consulter", width=12, command=consulter).grid(row=7, column=1)

# Création de la base
create_db()

root.mainloop()

