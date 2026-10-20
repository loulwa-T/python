import pgzrun
import random
HEIGHT=700
WIDTH=1000
b=Actor("spaceship.png")
b.pos=(500,600)
enemies=[]
eb=[]
def newenemy():
    for i in range (5):

     e=Actor("craft.png")
     e.pos=(120+i*200,50)
     enemies.append(e)
    clock.schedule(newenemy,2)
newenemy()
def draw():
    screen.blit("space.jpg",(0,0))
    for enemy in enemies:
        enemy.draw()
    b.draw()
    for bullet in eb:
        bullet.draw()
def update():
    if keyboard.left:
        b.x-=5
    if keyboard.right:
        b.x+=5
    for enemy in enemies:
        enemy.y+=5
    for bullet in eb:
        bullet.y-=3

def on_key_down(key):
    if key==keys.SPACE:
      bu=Actor("bullet.png",(b.x,b.y))
      eb.append(bu)

pgzrun.go()