from tkinter import Tk, Canvas, ARC, W
from human import human


class Student(human):
   
   def __init__(self, canvas,name,x,y,gen,gr,var):
        super().__init__(canvas,name,x,y,gen)
        self.group = gr
        self.variant = var 
        
    def _drawName(self):
        self.canvas.create_text(self.x+25,self.y-220,
        text=f'{self._name},{self.group}, №{self.variant}',
        anchor=W, font="Arial", fill="salmon")
        
