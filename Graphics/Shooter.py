# Basic Animation Framework

from tkinter import *
from random import randint
import random
import math

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    print("Init start")

    #data.circleSize = min(data.width, data.height) / 10
    #data.circleX = data.width/2
    #data.circleY = data.height/2
    data.charText = ""
    data.keysymText = ""
    data.circleCenters = []
    data.timerCalls = 0
    data.bullets = []
    pass

def mousePressed(event, data):
    # use event.x and event.y
    data.circleCenters.append((event.x, event.y))
    orig_dX = event.x-data.width/2
    orig_dY = event.y-data.height/2
    lenVector = math.sqrt(orig_dX**2+orig_dY**2)
    dX = orig_dX/lenVector
    dY = orig_dY/lenVector
    data.bullets.append(((data.width/2, data.height/2),[data.width/2, data.height/2], (dX, dY)))
    #data.circleX = event.x
    #data.circleY = event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    data.charText = event.char
    data.keysymText = event.keysym
    #print(event.keysym, type(event.keysym))
    currK = event.keysym
    if event.char == "d":
      if len(data.circleCenters):
        data.circleCenters.pop(0)
      else:
        print("No more circles to delete!")
    """
    if currK == "KP_Left" or currK == "Left":
      data.circleX-=5
    elif currK == "KP_Right" or currK == "Right":
      data.circleX+=5
    elif currK == "KP_Up" or currK == "Up":
      data.circleY-=5
    elif currK == "KP_Down" or currK == "Down":
      data.circleY+=5
    """
    pass

def timerFired(data):
  data.timerCalls+=1
  for ind, bullet in enumerate(data.bullets):
    dx = bullet[2][0]*20
    dy = bullet[2][1]*20
    bullet[1][0]+=dx
    bullet[1][1]+=dy



  data.bullets = [x for x in data.bullets if x[1][0] >=0 and x[1][0] <= data.width and x[1][1] >= 0 and x[1][1] <= data.height]



  pass

def redrawAll(canvas, data):
    # draw in canvas

    for bullet in data.bullets:
      x = bullet[1][0]
      y = bullet[1][1]
      dx = bullet[2][0]
      dy = bullet[2][1]
      canvas.create_oval(x-10, y-10, x+10, y+10, fill="black")
    for center in data.circleCenters:
      circleX = center[0]
      circleY = center[1]
      circleSize = 20
      canvas.create_oval(circleX- circleSize,
                        circleY - circleSize,
                        circleX + circleSize,
                        circleY + circleSize, fill="cyan")
      canvas.create_line(circleX-circleSize, circleY+circleSize,
                            circleX+circleSize, circleY+circleSize)
    if data.charText != "":
      canvas.create_text(data.width/10, data.height/3,
                            text="char: " + data.charText)
    if data.keysymText != "":
      canvas.create_text(data.width/10, data.height*2/3,
                            text="keysym: " + data.keysymText)
    canvas.create_text(data.width/2, data.height/2,
                        text="Timer Calls: " + str(data.timerCalls))
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
      timerFired(data)
      redrawAllWrapper(canvas, data)
      # pause, then call timerFired again
      canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 41
    root = Tk()
    root.resizable(width=False, height=False)
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.configure(background='white')
    #canvas.configure(background='red') #makes background red during initialization
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    #redrawAll(canvas, data)
    timerFiredWrapper(canvas,data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)
