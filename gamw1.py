import pgzrun
WIDTH=600
HEIGHT=400
odie=Actor("odie.png")
garfield=Actor("garfield.png")
def draw():
    screen.blit("sea.png",(0,0))
    garfield.draw()
    odie.draw()             
pgzrun.go()
