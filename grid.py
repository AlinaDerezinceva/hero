from tkinter import Tk, Canvas, Frame, BOTH


class Grid():
 
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.update()
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.stepX = 100
        self.stepY = 100
    
    def display(self):
        self.__drawHorizontalLines()
        self.__drawVerticalLines()
        
    def __drawHorizontalLines(self):
        for y in range(2, self.height, self.stepY):
            self.canvas.create_line(0, y, self.width, y, dash=(1, 1))
            self.canvas.create_text(12, y-7, text=y-2, fill="grey")
        
    def __drawVerticalLines(self):
        for x in range(2, self.width, self.stepX):
            self.canvas.create_line(x, 0, x, self.height, dash=(1, 1))
            self.canvas.create_text(x+10, 10, text=x-2, fill="grey")
  
