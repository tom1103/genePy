from tkinter import *
from tkinter.messagebox import *
from generator import *
from db import *

class Interface(Frame):
    """Interface pour génération pass et save"""
    def __init__(self, fen):
        Frame.__init__(self, fen, width=800, height=530)
        self.pack()

# Longueur du mot de passe
        self.label_lenght = Label(self, text="Password lenght :")
        self.label_lenght.pack(side=TOP)
        self.lenght = Spinbox(self, from_=1, to=100, width=5)
        self.lenght.delete(0, END)
        self.lenght.insert(0, 25)
        self.lenght.pack(side=TOP)

# Input pour le login
        self.login_label = Label(self, text="Login :")
        self.login_label.pack(side=TOP)
        self.message_login = Entry(self, width=30, font=("Verdana", 12))
        self.message_login.pack(side=TOP)

# Input pour le mot de passe
        self.label_resultat = Label(self, text="Password :")
        self.label_resultat.pack(side=TOP)
        self.message_resultat = Entry(self, width=30, font=("Verdana", 12))
        self.message_resultat.pack(side=TOP)

# Input pour les notes
        self.label_note = Label(self, text="Note :")
        self.label_note.pack(side=TOP)
        self.message_note = Entry(self, width=30, font=("Verdana", 12))
        self.message_note.pack(side=TOP)

# Bouton de sauvegarde
        self.save_btn = Button(self, text='Save', command=self.save)
        self.save_btn.pack()

# Bouton de génération des mot de passe
        self.ok_btn = Button(fen, text="Generate", command=self.generate)
        self.ok_btn.pack(side=TOP)

# Bouton pour la copy du mot de passe dans la presse papier
        self.copy_btn = Button(fen, text="Copy", command=self.copy)
        self.copy_btn.pack(side=RIGHT)

    def generate(self, event=None):
        """Génération du mot de passe"""
        lenght = int(self.lenght.get())
        gen1 = Generator()
        gen1.createList('num', 'char', 'spe')
        self.message_resultat.delete(0, END)
        self.message_resultat.insert(0, gen1.gen(lenght))


    def save(self, event=None):
        """Sauvegarde dans la BDD"""
        db = Db()
        try:
            db.dataInsert(self.message_login.get(), self.message_resultat.get(), self.message_note.get())
            showinfo('Information', 'Le mot de passe à bien été sauvegardé')
        except:
            showerror('Erreur', 'Mot de passe non sauvegardé')

        db.close()


    def copy(self):
        """Copie dans le presse papier du mot de passe"""
        # effacer l'éventuel contenu précédent du clipboard
        self.clipboard_clear()
        try:
            # saisir la sélection s'il y en a une (sinon -> except)
            t = self.message_resultat.get()
            self.message_resultat.selection_range(0, END)
            # et envoyer le texte sélectionné dans le clipboard
            self.clipboard_append(t)
        except:
            pass

app = Interface(Tk())
app.mainloop()
