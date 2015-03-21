from tkinter import *
from gen import *

class Interface(Frame):
    
    def __init__(self, fen):
        Frame.__init__(self, fen, width=400, height=530)
        self.pack(fill=BOTH)
                
        self.label_resultat = Label(self, text="Password :")
        self.label_resultat.pack()
        self.message_resultat = Label(self, font=("Verdana", 12))
        self.message_resultat.pack()
        
        self.ok_btn = Button(fen, text="Generate", command=self.generate)
        self.ok_btn.pack()

    def generate(self,event=None):
        self.message_resultat.configure(text=gen(25))
         

app = Interface(Tk())
app.mainloop()