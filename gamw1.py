import pgzrun
WIDTH=600
HEIGHT=400
boom=False
odie=Actor("odie.png")
garfield=Actor("garfield.png")
odie.pos=(200,100)
garfield.pos=(400,300)
def draw():
    screen.blit("sea.png",(0,0))
    garfield.draw()
    odie.draw()   
    screen.blit(???,(garfield.x,garfield.y))
def update():
    global boom
    if keyboard.left:
        odie.x-=5
    if keyboard.right:
        odie.x+=10
    if keyboard.a:
        garfield.x-=10
    if keyboard.s:
        garfield.x+=10
    if odie.colliderected(garfield):
        boom=True
    else:
        boom=False
        
pgzrun.go()
