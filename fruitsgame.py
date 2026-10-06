import pgzrun
import random
score=0
HEIGHT=367
WIDTH=800
b=Actor("basket.png")
b.pos=(400,300)
fruits=[]
fruitimages=["apple.png","gapple.png"]
def newfruit():
    fruit=Actor(random.choice(fruitimages))
    fruit.pos=(random.randint(1,800),10)
    fruits.append(fruit)
    clock.schedule(newfruit,2)
def draw():
    if score<=0:
        screen.blit("",(50,50))
        return
    screen.blit("trees.jpg",(0,0))
    for fruit in fruits:
     fruit.draw()
    b.draw()
    screen.draw.text("score="+str(score),(50,50))
def update():
    global score
    if keyboard.right:
       b.x+=10
    if keyboard.left:
        b.x-=10
    for fruit in fruits:
         fruit.y+=5
         if fruit.colliderect(b):
             score+=1
             fruits.remove(fruit)
         if fruit.y>367:
             score-=1
             fruits.remove(fruit)
             
newfruit()
pgzrun.go()
