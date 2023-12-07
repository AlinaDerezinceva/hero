from tkinter import Tk, Canvas
from random import randrange
 
 
class Weapon():
    
    def __init__(self, c, d, n):
        self._canvas = c
        self_baseDamage = d
        self._name = n
        
    def display(self, x, y):
        pass
    