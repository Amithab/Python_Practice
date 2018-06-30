from tkinter import *
import math

def drawChessboard(canvas, winWidth, winHeight):
  for y in range(8):
    for x in range(8):
      color = 'white'
      if((x+y)%2!=0):
        color='#808080'
      canvas.create_rectangle(x*winWidth/8.0, y*winHeight/8.0, 
                              (x+1)*winWidth/8.0, (y+1)*winHeight/8.0, 
                              fill=color)

      if(y == 0 or y == 7):
        color = 'black'
        if(y == 7):
          color = 'white'
        canvas.create_oval(x*winWidth/8.0+winWidth/32.0, y*winHeight/8.0 +
            winHeight/32.0, x*winWidth/8.0+3*winWidth/32.0, y*winHeight/8.0+
                3*winHeight/32.0,fill=color)
      
      if(y==1 or y==6):
        color = 'black'
        if(y==6):
          color = 'white'

        canvas.create_polygon(x*winWidth/8.0+winWidth/32.0, y*winHeight/8.0+
          3*winHeight/32.0, x*winWidth/8.0 + winWidth/16.0, y*winHeight/8.0+
          winHeight/32.0, x*winWidth/8.0+3*winWidth/32.0, y*winHeight/8.0+
          3*winHeight/32.0,fill=color, outline='black')

"""
Still need to write out letters for rook, knight, etc on respective pieces
"""



def runDrawing(width=400, height=400):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  drawChessboard(canvas, width, height)
  root.mainloop()
  print("Good Game!")


runDrawing(400, 500)

