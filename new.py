from tkinter import Tk, Canvas, Frame, BOTH, NW
 
 
class human(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.master.title("Smth")
        self.pack(fill=BOTH, expand=1)
        self.canvas=Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)
        
    def display(self):
        self.__drawHead()
        self.__drawBody()
        self.__drawLegs()
        self.__drawHends()
        self.__drawEyes()
        
    def __drawHead(self):
        self.canvas.create_oval(120, 120, 180, 180, width=2)
        
        
    def __drawBody(self):
        self.canvas.create_line(150, 180, 150, 285, width=2)
        
    def __drawLegs(self):
        self.canvas.create_line(100, 350, 150, 285,200,350, width=2)
        
    def __drawHends(self):
        self.canvas.create_line(100, 250, 150, 200,200,250, width=2)
        
    def __drawEyes(self):
        self.canvas.create_oval(140, 140, 140, 140, width=2),
        self.canvas.create_oval(140, 140, 140, 140, width=2)
       

