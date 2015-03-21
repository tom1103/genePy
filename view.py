from tkinter import *
from gen import *

class Interface(Frame):
    
    def __init__(self, fen):
        Frame.__init__(self, fen, width=800, height=530)
        self.pack()
        
        self.label_lenght = Label(self, text="Password lenght :")
        self.label_lenght.pack(side=TOP)
        self.lenght = Spinbox(self, from_=1, to=100, width=5)
        self.lenght.delete(0, END)
        self.lenght.insert(0, 25)
        self.lenght.pack(side=TOP)
        
        self.label_resultat = Label(self, text="Password :")
        self.label_resultat.pack(side=TOP)
        self.message_resultat = Entry(self, width=30, font=("Verdana", 12))
        self.message_resultat.pack(side=TOP)

        
        self.ok_btn = Button(fen, text="Generate", command=self.generate)
        self.ok_btn.pack(side=TOP)

        self.copy_btn = Button(fen, text="Copy", command=self.copy)
        self.copy_btn.pack(side=RIGHT)
        
    def generate(self,event=None):
        lenght = int(self.lenght.get())
        self.message_resultat.delete(0, END)
        self.message_resultat.insert(0, gen(lenght))
        
    def copy(self):
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