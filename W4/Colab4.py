from tkinter import *
import math

def lookAndSay(a):
  ind = 0
  tupleArr = []
  while(ind < len(a)):
    indAdd = findConsecutive(a, ind)
    tupleArr.append((indAdd, a[ind]))
    ind+=indAdd
  return tupleArr




def findConsecutive(a, ind):
  numCons = 0
  consNum = a[ind]
  while(ind<len(a)):
    if(a[ind] !=consNum):
      break
    ind+=1
    numCons+=1
  
  return numCons

"""
# testing for previous functions
print(findConsecutive([1,2,2,3,4],0))
print(findConsecutive([1,2,2,3,4],1))
print(lookAndSay([1,2,2,3,4]))
print(lookAndSay([]))
print(lookAndSay([1,1,1]))
print(lookAndSay([-1,2,7]))
print(lookAndSay([3,3,8,-10,-10,-10]))
"""

def findAngles(numPoints):
  angleArr=[]
  angleArc = 360.0/numPoints
  angleOffset = 360.0/(2*numPoints)
  angleStart = 270-angleArc+angleOffset

  for i in range(numPoints):
    angleArr.append(angleStart)
    angleStart+=angleArc
    if(angleStart>360):
      angleStart-=360

  return angleArr

def findStarCoor(angleArr, radius):
  coorArr = []
  for i in range(len(angleArr)):
    coorArr.append((round(radius*math.cos(math.pi*angleArr[i]/180),2), 
                    round(radius*math.sin(math.pi*angleArr[i]/180),2)))

  return coorArr

def drawStar(canvas, centerX, centerY, diameter, numPoints, color):
  canvas.create_oval(centerX-diameter/2, centerY-diameter/2,
                     centerX+diameter/2, centerY+diameter/2);
  canvas.create_oval(centerX-diameter*3/16, centerY-diameter*3/16,
                     centerX+diameter*3/16, centerY+diameter*3/16, fill=color,
                     width=0)
  #canvas.create_polygon(centerX-10, centerY, centerX+10, centerY,
   #                     centerX, centerY+50,fill=color);

  radius = diameter/2.0
  angleArr = findAngles(numPoints)
  starCoor = findStarCoor(angleArr, diameter*3.0/16)

  for i in range(len(starCoor)):
    midAngle = (angleArr[i]+angleArr[i-1])/2
    if(abs(angleArr[i]-angleArr[i-1])>180):
      midAngle = (angleArr[i]+angleArr[i-1]-360)/2
    outerX = round(radius*math.cos(math.pi*midAngle/180),2)
    outerY = round(radius*math.sin(math.pi*midAngle/180),2)

    canvas.create_polygon(centerX+starCoor[i][0], centerY+starCoor[i][1],
                          centerX+outerX, centerY+outerY,
                          centerX+starCoor[i-1][0], centerY+starCoor[i-1][1],
                          fill=color)



def runDrawing(centerX, centerY, diameter, numPoints, color, width=300, 
               height=300):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  drawStar(canvas, centerX, centerY, diameter, numPoints, color)
  root.mainloop()
  print("Done!")

runDrawing(250, 250, 200, 9, "yellow", 500, 500)

"""
#testing for findAngles helper function
for i in range(2,10):
  print(findAngles(i))
"""

"""
#testing for findStarCoor helper function
for i in range(2,6):
  print(findStarCoor(findAngles(i), 100))
"""
