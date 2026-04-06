import turtle
pen= turtle.Turtle()
screen=turtle.Screen()
pen.up()
list=["xxxxxxxxxxxxxxx",
     "xx xx xx xx xx ",
     "x     x      xx",
     "x x x x x  x xx",
     "x             x",
     "xx  xx  xx   xx",
     "x  x  x  x  x x",
     "x xx        xxx",
     "x  xx      xx x",
     "x        x  x x",
     "xxx xxx xx  x x",
     "xx    xx  x   x",
     "xxxx   x     xx",
     "x xx x x x x xx",
     "xxxxxxxxxxxxxxx"]
tile_list=[]
for y in range (len(list)):
    for x in range (len(list[y])):
     tilex= -288+(x*24)
     tiley=288-(y*24)
     character= list[y][x]
     if character =="x":
      tile=turtle.Turtle()
      tile.shape("square")
      tile.color("pink")
      tile.up()
      tile.speed(0)
      tile.goto(tilex,tiley)
      tile_list.append(tile)
def validmove(x,y):
     for tile in tile_list:
        if x==tile.xcor() and y==tile.ycor():
             return False
     return True
def right():
        x=pen.xcor()
        x+=24
        y=pen.ycor()
        if validmove(x,y)==True:
         pen.goto(x,y)
screen.listen()
screen.onkey(right,"Right")
def left():
        x=pen.xcor()
        x-=24
        y=pen.ycor()
        if validmove(x,y)==True:
         pen.goto(x,y)
screen.listen()
screen.onkey(left,"Left")
def up():
        y=pen.ycor()
        y+=24
        x=pen.xcor()
        if validmove(x,y)==True:
         pen.goto(x,y)
screen.listen()
screen.onkey(up,"Up")
def Down():
        y=pen.ycor()
        y-=24
        x=pen.xcor()
        if validmove(x,y)==True:
         pen.goto(x,y)
screen.listen()
screen.onkey(Down,"Down")
turtle.done()


