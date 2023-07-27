import tkinter


global Bild

# bisheriger Aufbau mit Knopf, Fläche und Bild
class simpleapp_tk(tkinter.Tk):
    
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        global Bild
        Hand = [(2, 0), (3, 1), (1, 4)]
        self.cards = [] 
        for card in Hand:
                self.cards.append(f'{card[0]}{card[1]}.png') 
                print(card)

        
        #Label erstellen mit festem Platz als xy-Koordinate und fester Höhe und Breite
<<<<<<< Updated upstream
        Bild = tkinter.PhotoImage(file = self.cards[0])
        self.card1 = tkinter.Label(self,image = Bild)
        self.card1.place(x=0, y=0)
        print(self.cards[0])
=======
        Bild = tkinter.PhotoImage(file = "9_of_diamonds.png")
        self.labelEins = tkinter.Label(self,image = Bild)
        self.labelEins.place(x=85, y=75, width=30, height=30)




# bei Klick auf den Knopf ...
    def OnButtonEinsClick(self):
        global Bild

        Bild = tkinter.PhotoImage(file = "9_of_diamonds.png")
        self.labelEins.configure(image = Bild)


>>>>>>> Stashed changes


  

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Schwimmen')
    app.mainloop()     
