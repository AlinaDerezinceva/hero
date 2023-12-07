from tkinter import Tk, Canvas
from weapon import Weapon
from random import randrange 


class Sword(Weapon):
    
    def __init__(self, c, d, n):
        self._canvas = c
        self._baseDamage = d
        self._name = n
        
    def display(self, x, y):
        self._canvas.create_line(x + 100, y - 150, x, y + 50 , x, y+30, width = 3, fill= 'green')
        self._canvas.create_line(x + 50, y+30, x, y-35, width=3, fill='green')
    
    def hit(self):
        damage = randrange(self._baseDamage-5, self._baseDamage+5)
        return damage