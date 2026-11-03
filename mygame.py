import pgzrun
import random
score=0
HEIGHT=1024
WIDTH=1024
worm=Actor("cuteworm.png",(500,500))
def draw():
    screen.blit("grass.jpg",(0,0))
    worm.draw()

pgzrun.go()