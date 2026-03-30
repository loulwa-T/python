import turtle
pen= turtle.Turtle()
screen=turtle.Screen()
list=["xxxxxxxxxxxxxxx",
     "xx xx xx xx xx ",
     "x     x      x ",
     "x x x x x  x x ",
     "x             x",
     "xx  xx  xx   xx",
     "x  x  x  x  x  ",
     "  xx        xxx",
     "x  xx      xx x",
     "         x  x  ",
     "xxx xxx xx xx x",
     "xx    xx  x x  ",
     "xxxx   x     xx",
     "x xx x x x x x ",
     "xxxxxxxxxxxxxxx"]
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
def right():
        x=pen.cor()
        x+=24
        y=pen.ycor()
        pen.goto(x,y)
screen.listen()
screen.onkey(right,"Right")
turtle.done()



