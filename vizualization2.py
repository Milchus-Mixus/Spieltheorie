import tkinter

global Bild
global CorX
global CorY
global Hand

CorX=[290, 420, 550, 290, 420, 550, 30, 160, 290, 550, 680, 810]
CorY=[420, 420, 420, 220, 220, 220, 20, 20, 20, 20, 20, 20]

#Hand = hand + open_cards + oponent_Hand_1 + oponent_hand_2
Hand = [(1, 2), (1, 0), (0, 2), (3, 5), (3, 3), (1, 4), (2, 4), (0, 3), (2, 1), (0, 0), (1, 1), (1, 5)]

for k in range (6,12):
     Hand[k] = (2,4)
print(Hand)

# bisheriger Aufbau mit Knopf, Fläche und Bild
class simpleapp_tk(tkinter.Tk):
    
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        global Bild
        #Hand = [(2, 0), (3, 1), (1, 4)]
        self.cards = [] 
        for card in Hand:
                self.cards.append(f'PNG-cards-1.3\\{card[0]}{card[1]}.png') 
                print(card)
        Player = 0
        Bilder = []
        for Position in range (0, 11):
        #Label erstellen mit festem Platz als xy-Koordinate und fester Höhe und Breite
            Bild = tkinter.PhotoImage(file = self.cards[Position])
            self.Position = tkinter.Label(self,image = Bild)
            self.Position.place(x=CorX[Position], y=CorY[Position])
            print(Position, self.cards[Position], CorX[Position], CorY[Position])


  

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Schwimmen')
    app.mainloop()     
