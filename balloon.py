import turtle
import random
turtle.colormode(255)
screen=turtle.Screen()
food=turtle.Turtle()
food.shape("triangle")
food.up()
food.goto(-200,-200)
food.left(90)
def right():
    x=food.xcor()+10
    y=food.ycor()
    if x<250:
     food.goto(x,y)
screen.listen()
screen.onkey(right,"Right")
def left():
    x=food.xcor()-10
    y=food.ycor()
    if x>-250:
     food.goto(x,y)
screen.onkey(left,"Left")
list=[]
badlist=[]
def bal():
 balloon=turtle.Turtle()
 balloon.speed(0)
 balloon.hideturtle()
 balloon.shape("circle")
 balloon.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
 balloon.up()
 balloon.left(90)
 balloon.goto(random.randint(-250,250),250)
 balloon.showturtle()
 list.append(balloon)

score=0
sp=turtle.Turtle()


def badbal():
 badballoon=turtle.Turtle()
 badballoon.speed(0)
 badballoon.hideturtle()
 badballoon.shape("circle")
 badballoon.pencolor("red")
 badballoon.fillcolor("black")
 badballoon.up()
 badballoon.left(90)
 badballoon.goto(random.randint(-250,250),250)
 badballoon.showturtle()
 badlist.append(badballoon)

gameover=True
while gameover:
   t=random.randint(1,25)
   if t==9:
    bal()
   for balloon in list:
    balloon.backward(5)
    if balloon.distance (food)<15:
     list.remove(balloon)
     balloon.hideturtle()
     score+1
     sp.write(score)
    elif balloon.ycor()<-250:
     balloon.hideturtle()
     list.remove(balloon)
   ti=random.randint(1,250)
   if ti==2:
     badbal()
   for badballoon in badlist:
     badballoon.backward(5)
     if badballoon.distance (food)<15:
      badballoon.write ("game over")
      gameover=False
     elif badballoon.ycor()<-250:
      badballoon.hideturtle()
      badlist.remove(badballoon)
    
