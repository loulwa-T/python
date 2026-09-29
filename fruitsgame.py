import pgzrun
import random
HEIGHT=367
WIDTH=800
b=Actor("basket.png")
a=Actor("apple.png")
b.pos=(400,300)
a.pos=(random.randint(1,800),10)
def draw():
    screen.blit("trees.jpg",(0,0))
    a.draw()
    b.draw()
def update():
    a.y+=5
    if keyboard.right:
       b.x+=5 
    if keyboard.left:
        b.x-=5

pgzrun.go()
