
from tkinter import *

import math

def rgbString(red, green, blue):
  return "#%02x%02x%02x" %(red, green, blue)

def drawBelgianFlag(canvas, x0, y0, x1, y1):
  width = (x1-x0)
  canvas.create_rectangle(x0, y0, x0+width/3, y1, fill="black",width=0)
  canvas.create_rectangle(x0+width/3, y0, x0+width*2/3,y1,fill="yellow",
                          width=0)
  canvas.create_rectangle(x0+width*2/3,y0,x1,y1,fill="red",width=0)

def draw(canvas, width, height):
  #canvas.create_rectangle(0,0,150,150,fill="yellow")
  pistachio = rgbString(147, 197, 114)
  print(rgbString(147, 197, 114))
  maroon = rgbString(176, 48, 96)
  margin = 10
  canvas.create_rectangle(margin,margin, width-margin, height-margin,
                          fill = rgbString(147, 200, 114))

  (cx, cy) = (width/2, height/2)
  (rectWidth, rectHeight) = (width/4, height/4)
  canvas.create_rectangle(cx-rectWidth/2, cy-rectHeight/2, cx+rectWidth/2,
                          cy + rectHeight/2, fill =maroon)
  canvas.create_oval((100, 50),( 300, 150), fill="yellow")
  canvas.create_polygon(100,30,200,50,300,30,200,10, fill="green")
  canvas.create_line(100, 50, 300, 150, fill="red", width=5)
  canvas.create_text(200, 100, text="Amazing!",
                       fill="purple", font="Helvetica 20 bold underline")
  canvas.create_text(200, 100, text="Carpe Diem!", anchor=SW,
                       fill="darkBlue", font="Times 22 bold italic")
  drawBelgianFlag(canvas, 25, 25, 175, 150)

  drawBelgianFlag(canvas, 75, 160, 125, 200)

  (cx, cy, r) = (width/2, height/2, min(width, height)/3)
  canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="yellow")
  r *= 0.85
  for hour in range(12):
    hourAngle = math.pi/2-(2*math.pi)*(hour/12)
    hourX = cx+r*math.cos(hourAngle)
    hourY = cy-r*math.sin(hourAngle)
    label = str(hour if (hour>0) else 12)
    canvas.create_text(hourX,hourY, text = label, font="Arial 16 bold")


def runDrawing(width=300, height=300):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  draw(canvas,width, height)
  root.mainloop()
  print("bye!")

runDrawing(800,600)
