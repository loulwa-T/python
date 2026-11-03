import pgzrun
import random
HEIGHT=700
WIDTH=1000
b=Actor("spaceship.png")
b.pos=(500,600)
enemies=[]
eb=[]
lives=3
neb=[]
def newenemy():
    for i in range (5):

     e=Actor("craft.png")
     e.pos=(120+i*200,50)
     enemies.append(e)
    clock.schedule(newenemy,2)
newenemy()
def enemyshoot():
   enemy=random.choice(enemies)
   bullet=Actor("bullet.png")
   bullet.pos=enemy.pos
   neb.append(bullet)
   clock.schedule(enemyshoot,2)

def draw():
    global lives
    if lives<=0:
       screen.blit("gover.png",(0,0))
       return 
    screen.blit("space.jpg",(0,0))
    for enemy in enemies:
        enemy.draw()
    b.draw()
    for bullet in eb:
        bullet.draw()
    screen.draw.text("lives"+str(lives),(50,50))
    for ebullet in neb:
       ebullet.draw()
       
def update():
    global lives
    if lives<=0:
       return
    if keyboard.left:
        b.x-=5
    if keyboard.right:
        b.x+=5
    for enemy in enemies:
        enemy.y+=5
    for bullet in eb:
        bullet.y-=3
    for enemy in enemies:
     if b.colliderect(enemy):
        enemies.remove(enemy)
        lives-=1
     if enemy.y>700:
        enemies.remove(enemy)
     for bullet in eb:
        if bullet.colliderect(enemy):
           enemies.remove(enemy)
           eb.remove(bullet)
           lives+=1
    for bullet in neb:
       bullet.y+=3
def on_key_down(key):
    if key==keys.SPACE:
      bu=Actor("bullet.png",(b.x,b.y))
      eb.append(bu)


             
pgzrun.go()