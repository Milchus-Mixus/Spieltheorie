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

        # frame erstellen, mit fester Höhe und Breite
        

        #Knopf erstellen mit festem Platz als xy-Koordinate und fester Höhe und Breite
 
        
        #Label erstellen mit festem Platz als xy-Koordinate und fester Höhe und Breite
        Bild = tkinter.PhotoImage(file = "9_of_diamonds.png")
        self.labelEins = tkinter.Label(self,image = Bild)
        self.labelEins.place(x=85, y=85)




# bei Klick auf den Knopf ...
    def OnButtonEinsClick(self):
        global Bild

        Bild = tkinter.PhotoImage(file = "9_of_diamonds.png")
        self.labelEins.configure(image = Bild)





if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Das Fenster')
    app.mainloop()     
