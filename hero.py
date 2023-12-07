from tkinter import Tk, Canvas, ARC, W
from human import human


class Hero(human):
    def __init__(self, canvas,name, x, y, gen, h):
        super().__init__(canvas,name, x, y, gen)
        self.health = h
        self._wp = None
        
        
        self.health_bar_width = 100
        self.health_bar_height = 10
        self.health_bar_x = self.x +1.5
        self.health_bar_y = self.y - 250
        self.health_bar_color = 'blue'
        self.dead_color = 'red'
    
    def _drawName(self):
        self.canvas.create_text(self.x + 1.5 , self.y - 280, text = self._name, font= "Times 18", anchor=W, fill="black")
        self.canvas.create_rectangle(self.health_bar_x + self.health,
                                     self.y-250,
                                     self.health_bar_x + 100,
                                     self.health_bar_y + self.health_bar_height,
                                     fill = 'red')
                                     
        self.canvas.create_rectangle(self.health_bar_x,
                                     self.health_bar_y,
                                     self.health_bar_x + self.health,
                                     self.health_bar_y + self.health_bar_height,
                                     fill = self.health_bar_color)
       
    def setWeapon(self, weapon):
        self._wp = weapon
    
    def attack (self, enemy):
        damage = self._wp.hit()
            
        if enemy._wp.__class__.__name__=='shield':
            if enemy.health - damage + 10 > 0:
                enemy.health -= (damage + 10)
            else:
                enemy.health = 0
            print(f'{self._name} нанёс {"" if self.gen=="м" else "ла"} {damage} урона {enemy._name}!')
            print(f'y {enemy._name} осталось {enemy.health}  здоровья, так как щит блокирует 5 урона')
        else:
            if enemy.health - damage > 0:
                enemy.health -= damage
            else:
                enemy.health = 0
            print(f'{self._name} нанёс {"" if self.gen=="м" else "ла"} {damage} урона {enemy._name}!')
            print(f'y {enemy._name} осталось {enemy.health} здоровья')
    
    
       
        
    
    def _drawWeapon(self):
        self._wp.display(self.x+80, self.y-100)
    
    def display(self):
        self._drawName()
        super().display()
        self._drawWeapon()
