import pgzrun
import random
HEIGHT=440
WIDTH=440
minion=Actor(IMG_0573.jpeg)
minion.pos=(random.randint(0,340),random.randint(0,340))
score=0
def draw ():
 screen.blit(IMG_568.jpeg,(0;0))
screen.draw.text(str(score),(10,10))
def move():
    minion.pos=(random.randint(0,340),random.randint(0,340))
    clock.scheduele(move,1)
def on_mouse_down(pos):
    global score
    if minion.collidepoint(pos)
     score+=1
    e
 score-=1lse:
move()
pgzrun.go
