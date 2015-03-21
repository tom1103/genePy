from tkinter import *
from gen import *

class Interface(Frame):
    
    def __init__(self, fen):
        Frame.__init__(self, fen, width=800, height=530)
        self.pack(fill=BOTH)
        
        self.lenght = Spinbox(fen, from_=0, to=100)
        self.lenght.pack()        
        self.label_resultat = Label(self, text="Password :")
        self.label_resultat.pack()
        self.message_resultat = Entry(self, width=30, font=("Verdana", 12))
        self.message_resultat.pack()

        
        self.ok_btn = Button(fen, text="Generate", command=self.generate)
        self.ok_btn.pack()

    def generate(self,event=None):
        lenght = int(self.lenght.get())
        self.message_resultat.delete(0, END)
        self.message_resultat.insert(0, gen(lenght))
         

app = Interface(Tk())
app.mainloop()