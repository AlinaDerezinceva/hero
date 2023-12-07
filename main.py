from tkinter import Tk, Canvas
from grid import Grid
from hero import Hero
from weapon import Weapon
from sword import Sword
from bow import Bow
import random

root = Tk()
canvas= Canvas(root, width=800,height=600)
canvas.pack()
grid=Grid(canvas)
grid.display()

fs=open('students.txt','r',encoding='utf-8')

students=[]
for hero in fs:
    s=hero.split(';')
    id=int(s[0])
    name=s[1]
    var=int(s[2])
    group='ИП-22'
    gender=(s[4])
    students.append({'id':id,'full_name':name, 'variant':var, 
     'gender':gender})
      
fs.close()

wp1 = Sword(canvas, 40, 'меч')
wp2 = Bow(canvas, 0, 'щит')

s1 = random.choice(students)
name=f"{s1['full_name'].split()[0]} {s1['full_name'].split()[1][0]} {s1['full_name'].split()[2][0]}"
p1 = Hero(canvas, name, 400, 400, s1['gender'], 100)
p1.setWeapon(wp1)
p1.display()

s2=random.choice(students)
name=f"{s2['full_name'].split()[0]} {s2['full_name'].split()[1][0]} {s2['full_name'].split()[2][0]}"
p2=Hero(canvas, name, 100, 400, s1['gender'], 100)
p2.setWeapon(wp2)
p2.display()

p1.attack(p2)
p2.display()

root.mainloop()