from tkinter import Tk, Canvas, ARC
from weapon import Weapon

class Bow(Weapon):

    def __init__(self, c, d, n):
        self._canvas = c
        self._baseDamage = d
        self._name = n

    def display(self, x, y,):
        self._canvas.create_line(x + 100, y - 150, x, y + 30, width=2,  fill='grey')
        self._canvas.create_arc(x+100,y-150,x,y+30, start=65, extent=-220,style=ARC, outline="grey", width=3)