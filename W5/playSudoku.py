# Basic Animation Framework

from tkinter import *
from random import randint
import random
import math
from SudokuCheck import isLegalSudoku

"""
Box class to represent one unit of a sudoku puzzle
"""
class Box(object):
  def __init__(self, rowPos, colPos, value=0, peers=None):
    self.rowPos = rowPos
    self.colPos = colPos
    self.value = value
    self.peers = peers

"""
Returns set of coordinates for block in sudoku puzzle of given size excluding
current box
"""
def buildBlock(rowPos, colPos, size):
  block = []
  rowStart = rowPos//size*size
  colStart = colPos//size*size
  for row in range(rowStart, rowStart+size):
    for col in range(colStart, colStart+size):
      if row != rowPos or col != colPos:
        block.append([row,col])
  return block

"""
Returns set of coordinates for row in sudoku puzzle of given size excluding 
current box
"""
def buildRow(rowPos, colPos, size):
  row = []
  for cVal in range(0, size*size):
    if cVal != colPos:
      row.append([rowPos, cVal])
  return row

"""
Returns set of coordinates for column in sudoku puzzle of given size excluding
current box
"""
def buildCol(rowPos, colPos, size):
  col = []
  for rVal in range(0, size*size):
    if rVal != rowPos:
      col.append([rVal, colPos])
  return col

"""
Builds all peers for current box not including current box
"""
def buildPeerCoors(row, col, size):
  peers = buildBlock(row, col, size)
  peerAdd = [x for x in buildRow(row, col, size) if x not in peers]
  peers.extend(peerAdd)
  peerAdd = [x for x in buildCol(row, col, size) if x not in peers]
  peers.extend(peerAdd)
  return peers

"""
Prints out sudoku board for given size
"""
def printBoard(grid):
  size = len(grid)
  blockSize = int(math.sqrt(size))
  print("\n")
  for rowInd, row in enumerate(grid):
    for colInd, box in enumerate(row):
      print(box.value, end= ' ')
      if not (colInd+1)%blockSize and colInd < size - 1:
        print("|",end='')
    print()
    if not (rowInd+1)%blockSize and rowInd < size - 1:
      print("-------------------")
  print("\n")

"""
Print box peer links for checking
"""
def testLinks(board):
  for rowInd, row in enumerate(board):
    for colInd, box in enumerate(row):
      print("[", box.rowPos, box.colPos, "]:", [[x.rowPos, x.colPos] for x in box.peers])

"""
Interlink all boxes with their peer box instances
"""
def buildLinks(board):
  #print("Building Links")
  blockSize = int(math.sqrt(len(board)))
  for rowInd, row in enumerate(board):
    for colInd, box in enumerate(row):
      box.peers = [board[x[0]][x[1]] for x in buildPeerCoors(box.rowPos, box.colPos, blockSize)]

"""
Finds next box for recursive search
"""
def findNextBox(grid, box):
  if box.colPos < len(grid) - 1:
    return grid[box.rowPos][box.colPos+1]
  elif box.rowPos < len(grid) - 1:
    return grid[box.rowPos+1][0]
  return None

"""
Test findNextBox
"""
def testFindNextBox():
  grid = buildLinks("i")

  box = grid[0][0]
  while(box):
    print(box.rowPos, box.colPos)
    box = findNextBox(grid, box)

"""
Recursive function to fill up board randomly and legally
"""
def fillRecur(grid, box):
  neighborVals = [x.value for x in box.peers if x.value]
  options = [x for x in range(1, len(grid)+1) if x not in neighborVals]
  random.shuffle(options)

  for posVal in options:
    box.value = posVal
    nextBox = findNextBox(grid, box)
    # base case 1 if board is filled
    if not nextBox:
      return True

    # recursive call
    if fillRecur(grid, nextBox):
      return True

  # base case 2 if no option works move up to upper level
  box.value = 0
  return False

# Builds links and calls recursive fill function
def fillBoard(board):
  buildLinks(board)

  # recursive board filling
  isFilled = fillRecur(board, board[0][0])

  if not isFilled:
    return False
  return True

"""
Creates board of given size and calls function to fill it with valid values
starting from an empty board of all 0's
And checks for legality
"""
def generateBoard(size):
  board = [[Box(row, col) for col in range(size)] for row in range(size)]
  if not fillBoard(board):
    print("Could not generate board")
    return False
  elif not isLegalSudoku(transformBoard(board)):
    print("Not a legal board")
    return board
  print("Done generating board")
  return board

"""
Creates linked board from given values in matrix
"""
def getBoard(matrix):
  size = len(matrix)
  board = [[Box(row, col, matrix[row][col]) for col in range(size)] for row in range(size)]

  buildLinks(board)
  return board


def solveRecur(origMatrix, grid, box):
  options = []
  # skips processing this box if part of original matrix
  if origMatrix[box.rowPos][box.colPos]:
    nextBox = findNextBox(grid, box)
    if not nextBox:
      return True
    if solveRecur(origMatrix, grid, nextBox):
      return True
    return False
    
  # slower method: options.append(origMatrix[box.rowPos][box.colPos])
  else:
    neighborVals = []
    for peer in box.peers:
      if peer.value:
        neighborVals.append(peer.value)
      elif origMatrix[peer.rowPos][peer.colPos]:
        neighborVals.append(origMatrix[peer.rowPos][peer.colPos])

    options.extend([x for x in range(1, len(grid)+1) if x not in neighborVals])

  for posVal in options:
    box.value = posVal
    nextBox = findNextBox(grid, box)

    # base case 1 if board is filled
    if not nextBox:
      return True

    # recursive call
    if solveRecur(origMatrix, grid, nextBox):
      return True

  # base case 2 if no option works move up to upper level
  box.value = 0
  return False


def solveRecur2(cells):
  if len(cells):
    currBox = cells.pop(0)
  else:
    return True

  neighborVals = [x.value for x in currBox.peers]
    
  options = [x for x in range(1, 10) if x not in neighborVals]

  for posVal in options:
    currBox.value = posVal

    if solveRecur2(cells):
      return True

  currBox.value = 0
  cells.insert(0, currBox)
  return False


def solveMatrix(board):
  cells = [board[x][y] for x in range(len(board)) for y in range(len(board)) if not board[x][y].value]
  return solveRecur2(cells)



"""
Transforms 2d array of Box objects into 2d array of values for sudoku
"""
def transformBoard(board):
  grid = []
  for rowInd, row in enumerate(board):
    grid.append([x.value for x in row])
  return grid





dups = 0
def findDupRecur2(cells):
  global dups
  if len(cells):
    currBox = cells.pop(0)
  else:
    dups+=1
    if dups > 1:
      return True
    return False

  neighborVals = [x.value for x in currBox.peers]
  options = [x for x in range(1,10) if x not in neighborVals]
  
  for posVal in options:
    currBox.value = posVal

    if findDupRecur2(cells):
      return True

  currBox.value = 0
  cells.insert(0, currBox)
  return False

def findDupSol2(board):
  global dups
  dups = 0
  cells = [board[x][y] for x in range(len(board)) for y in range(len(board)) if not board[x][y].value]
  cells2 = cells.copy()
  duplicateExists = findDupRecur2(cells)
  for box in cells2:
    box.value = 0
  #print("end of duplicates\n")
  #printBoard(board)
  return duplicateExists






#import time
#start_time = time.time()
#board = generateBoard(9)
#print("Time to generate: --- %s seconds ---" % (time.time() - start_time))
"""
if board:
  transformed = transformBoard(board)
  #print(transformed)
  print(isLegalSudoku(transformed))
  printBoard(board, 9)
"""
# use duplicate global variable to count # of solutions
duplicates = 0

def findDupRecur(origMatrix, grid, box):
  # skips options processing if box part of original matrix
  global duplicates
  if origMatrix[box.rowPos][box.colPos]:
    nextBox = findNextBox(grid, box)
    if not nextBox:
      if duplicates == 2:
        return True
      return False
    if findDupRecur(origMatrix, grid, nextBox):
      return True
    return False

  neighborVals = []
  for peer in box.peers:
    if peer.value:
      neighborVals.append(peer.value)
    elif origMatrix[peer.rowPos][peer.colPos]:
      neighborVals.append(origMatrix[peer.rowPos][peer.colPos])

  options = [x for x in range(1, len(grid)+1) if x not in neighborVals]
  for posVal in options:
    box.value = posVal
    nextBox = findNextBox(grid, box)

    if not nextBox:
      duplicates+=1
      if duplicates > 1:
        return True
      return False

    if findDupRecur(origMatrix, grid, nextBox):
      return True

  box.value = 0
  return False

def findDuplicateSolutions(origMatrix, grid):
  global duplicates
  duplicates = 0
  return findDupRecur(origMatrix, grid, grid[0][0])



matrix = [[0,8,0,0,0,9,7,4,3],
            [0,5,0,0,0,8,0,1,0],
            [0,1,0,0,0,0,0,0,0],
            [8,0,0,0,0,5,0,0,0],
            [0,0,0,8,0,4,0,0,0],
            [0,0,0,3,0,0,0,0,6],
            [0,0,0,0,0,0,0,7,0],
            [0,3,0,5,0,0,0,8,0],
            [9,7,2,4,0,0,0,5,0]]
import time

def isUnique(matrix, display=True, timed=False, printStatement=None):
  if timed:
    startTime = time.time()
  board = getBoard(matrix)
  duplicateExists = findDupSol2(board)#findDuplicateSolutions(matrix, board)
  if display:
    if duplicateExists:
      print("Duplicates exist - Not unique!")
    else:
      print("Unique!")
  if timed:
    if printStatement:
        print("%s - %s seconds" %(printStatement, time.time()-startTime))
    else:
      print(" --- %s seconds --- " %(time.time()-startTime))
  return not duplicateExists

#isUnique(matrix, True, True, "Duplicate puzzle")


def generatePuzzle():
  board = generateBoard(9)

  cells = []
  count = 0
  for rowInd, row in enumerate(board):
    cells.extend(row)

  #print(cells)
  random.shuffle(cells)
  #len(cells)
  for cell in cells:
    currValue = cell.value
    cell.value = 0
    if findDupSol2(board):
      cell.value = currValue


    #for colInd, box in enumerate(row):
    #  count+=1
    #  startTime = time.time()
    #  currValue = box.value
    #  box.value = 0
      #print("Before replaced", box.rowPos, box.colPos, box.value, currValue, "\n")
      #printBoard(board)
    #  if findDupSol2(board):
        #print("Replaced", box.rowPos, box.colPos, box.value, currValue)
    #    box.value = currValue
      #if findDuplicateSolutions(transformBoard(board), board):
      #  print("Replaced")
      #  box.value = currValue
      #print(" %d squares done. %s seconds" %(count, time.time()-startTime))
      #printBoard(board)
      #print("board", transformBoard(board))

  printBoard(board)

sT = time.time()
generatePuzzle()
print("generation time: %s seconds" %(time.time()-sT))





def solveMat(matrix):
  board = getBoard(matrix)
  solveRecur(matrix, board, board[0][0])
  printBoard(board)
  print(isLegalSudoku(transformBoard(board)))

def solveMat2(matrix):
  board = getBoard(matrix)
  isSolved = solveMatrix(board)
  print("Solved:", isSolved)
  printBoard(board)
  print("IsLegal:", isLegalSudoku(transformBoard(board)))

matrix = [[0,0,3,0,1,0,0,2,0],
            [9,0,5,3,0,0,0,4,0],
            [0,8,0,0,0,2,3,6,0],
            [5,7,4,9,0,0,0,0,0],
            [0,0,0,4,2,8,0,0,3],
            [0,0,0,0,0,0,0,0,0],
            [0,0,8,7,4,3,0,0,0],
            [0,0,0,0,0,0,2,8,0],
            [0,0,0,0,0,1,0,0,4]]

#isUnique(matrix, True, True, "Easy unique puzzle")

#print(solveMatrix(getBoard(matrix)))
"""
sT = time.time()
solveMat2(matrix)
print("--- %s seconds ---" %(time.time()-sT))
"""
#import time
"""
sT = time.time()
board = getBoard(matrix)
print(findDuplicateSolutions2(matrix, board))
print(" easy unique puzzle --- %s seconds --- " %(time.time()-sT))
sT = time.time()
solveMat(matrix)
print(" easy puzzle --- %s seconds --- " %(time.time()-sT))
"""
"""
Long test:
import time
sT = time.time()
for i in range(1000):
  solveMat(matrix)
diff = time.time()-sT
print("=== %s seconds  %s seconds ---" %(diff, diff/100))

"""
matrix = [[0,0,3,0,1,0,0,2,0],
            [9,0,5,3,0,0,0,4,0],
            [0,8,0,0,0,2,3,6,0],
            [5,7,4,9,0,0,0,0,0],
            [0,0,0,4,2,8,0,0,3],
            [0,0,0,0,0,0,0,0,0],
            [0,0,8,7,4,3,0,0,0],
            [0,0,0,0,0,0,2,8,0],
            [0,0,0,0,0,1,0,0,4]]
"""
import time
sT = time.time()
solveMat(matrix)
print(" easy puzzle --- %s seconds --- " %(time.time()-sT))
# hard puzzle
matrix = [[7,1,0,2,0,0,0,0,0],
            [0,9,0,7,0,0,0,0,1],
            [2,0,0,0,0,0,5,0,4],
            [0,0,4,8,0,0,0,0,0],
            [0,2,0,0,4,0,0,1,0],
            [0,0,0,0,0,3,6,0,0],
            [5,0,9,0,0,0,0,0,7],
            [1,0,0,0,0,8,0,3,0],
            [0,0,0,0,0,1,0,5,9]]
sT = time.time()
solveMat(matrix)
print(" hard puzzle --- %s seconds --- " %(time.time()-sT))
"""
#hardest
matrix = [[0,6,1,0,0,7,0,0,3],
            [0,9,2,0,0,3,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,8,5,3,0,0,0,0],
            [0,0,0,0,0,0,5,0,4],
            [5,0,0,0,0,8,0,0,0],
            [0,4,0,0,0,0,0,0,1],
            [0,0,0,1,6,0,8,0,0],
            [6,0,0,0,0,0,0,0,0]]
#isUnique(matrix, True, True, "Hardest unique puzzle")
"""
sT = time.time()
solveMat2(matrix)
print("--- hardest puzzle %s seconds ---" %(time.time()-sT))
"""
"""
sT = time.time()
board = getBoard(matrix)
print(findDuplicateSolutions2(matrix, board))
print(" hardest dup puzzle --- %s seconds --- " %(time.time()-sT))
"""

"""
sT = time.time()
solveMat(matrix)
print(" hardest puzzle --- %s seconds --- " %(time.time()-sT))

# Inkala2010
matrix = [[0,0,5,3,0,0,0,0,0],
            [8,0,0,0,0,0,0,2,0],
            [0,7,0,0,1,0,5,0,0],
            [4,0,0,0,0,5,3,0,0],
            [0,1,0,0,7,0,0,0,6],
            [0,0,3,2,0,0,0,8,0],
            [0,6,0,5,0,0,0,0,9],
            [0,0,4,0,0,0,0,3,0],
            [0,0,0,0,0,9,7,0,0]]
sT = time.time()
solveMat(matrix)
print(" Inkala2010 puzzle --- %s seconds --- " %(time.time()-sT))

# Inkala2012
matrix = [[8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0]]
sT = time.time()
solveMat(matrix)
print(" Inkala2012 puzzle --- %s seconds --- " %(time.time()-sT))
"""
####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.startX = 100
    data.startY = 100
    print("Init start")

    data.sudArr = transformBoard(generateBoard(9))
    """
    data.circleSize = min(data.width, data.height) / 10
    data.circleX = data.width/2
    data.circleY = data.height/2
    data.charText = ""
    data.keysymText = ""
    """
    pass

def mousePressed(event, data):
    # use event.x and event.y
    #data.circleX = event.x
    #data.circleY = event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    #data.charText = event.char
    #data.keysymText = event.keysym
    pass

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(data.startX, data.startY, data.startX + 450, 
                            data.startY + 450)

    drawArr = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    for row in range(9):
      for col in range(9):
        canvas.create_rectangle(col*50+data.startX, 
                                row*50+data.startY,
                                col*50+data.startX + 50,
                                row*50+data.startY + 50)
        canvas.create_text(col*50 + data.startX + 25,
                            row*50+data.startY + 25,
                            text=data.sudArr[row][col], font=('Helvetica', 25))

    for row in range(4):
      canvas.create_line(data.startX - 3, data.startY + row*150, 
                            data.startX + 453, data.startY +row*150, width=7)

    for col in range(4):
      canvas.create_line(data.startX + col*150, data.startY - 3, 
                            data.startX + col*150, data.startY + 453, width=7)



    """
    canvas.create_oval(data.circleX-data.circleSize,
                        data.circleY - data.circleSize,
                        data.circleX + data.circleSize,
                        data.circleY + data.circleSize)
    if data.charText != "":
      canvas.create_text(data.width/10, data.height/3,
                            text="char: " + data.charText)
    if data.keysymText != "":
      canvas.create_text(data.width/10, data.height*2/3,
                            text="keysym: " + data.keysymText)
    """
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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)
