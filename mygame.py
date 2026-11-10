import pgzrun
import random
score=0
HEIGHT=1024
WIDTH=1024
worm=Actor("cuteworm.png",(500,500))
apple=Actor("applecore.png")
pb=Actor("pb.png")
def draw():
    screen.blit("grass.jpg",(0,0))
    worm.draw()
    apple.draw()
    pb.draw()
    screen.draw.text("score"+str(score),(50,50))

def update ():
  global score
  if keyboard.right and worm.x<1000:
    worm.x+=10
  if keyboard.left and worm.x>50:
    worm.x-=10
  if keyboard.up and worm.y>0:
    worm.y-=10
  if keyboard.down and worm.y<1000:
    worm.y+=10   
  if worm.colliderect(apple):
    score+=1
    apple.x=(random.randint(20,1000))
    apple.y=(random.randint(20,1000))
  if worm.colliderect(pb):
    score-=2
    pb.x=(random.randint(20,1000))
    pb.y=(random.randint(20,1000))
    

def spawn():
  apple.x=(random.randint(20,1000))
  apple.y=(random.randint(20,1000))
  clock.schedule(spawn,3)

def pspawn():
  pb.x=(random.randint(20,1000))
  pb.y=(random.randint(20,1000))
  clock.schedule(pspawn,5)  

spawn()
pspawn()
pgzrun.go()
