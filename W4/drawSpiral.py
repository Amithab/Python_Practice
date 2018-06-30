from tkinter import *
import math

def drawSpiral(canvas, width, height):
  for i in range(32):
    gap = 5
#    canvas.create_oval(7*width/16.0-i*gap, 7*height/16.0-i*gap, 
 #                       i*gap+ 9*width/16.0, i*gap + 9*height/16.0)
    for j in range(28):
      drawSmallCircle(canvas, j*360.0/28+i, width, height, 
        height/2.0-(7*height/16.0-i*gap), i)





def drawSmallCircle(canvas, angle, width, height, radius, gradient):
  yCenter = -radius*math.sin(angle*math.pi/180)
  xCenter = radius*math.cos(angle*math.pi/180)
  color=rgbString(255-32+gradient, 255-gradient*5,25+ gradient*5)
  canvas.create_oval(width/2+xCenter-2, height/2+yCenter-2, width/2+xCenter+2, 
                    height/2+yCenter+2, fill=color,outline='')

def rgbString(red, green, blue):
  return "#%02x%02x%02x" %(red, green, blue)


def runDrawing(width=400, height=400):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  drawSpiral(canvas, width, height)
  root.mainloop()
  print("Nice Spiral")

runDrawing()
