import math

def isLegalSudoku(board):
  N = int(math.sqrt(len(board)))
  for i in range(N):
    if not isLegalRow(board, i):
      return False
    if not isLegalCol(board, i):
      return False
    if not isLegalBlock(board, i):
      return False
  return True

def isLegalBlock(board, block):
  N = int(math.sqrt(len(board)))
  colStart = (block%N)*N
  rowStart = int(block/N)*N

  arr = []
  for row in range(rowStart, rowStart+N):
    for col in range(colStart, colStart+N):
      arr.append(board[row][col])

  return areLegalValues(arr)

def isLegalCol(board, col):
  arr = []
  for i in range(len(board)):
    arr.append(board[i][col])
  return areLegalValues(arr)

def isLegalRow(board, row):
  return areLegalValues(board[row])

def areLegalValues(values):
  if not math.sqrt(len(values)).is_integer():
    return False

  if max(values) > len(values):
    return False

  for i in range(1, len(values)+1):
    if values.count(i) > 1:
      return False

  return True


testSudo = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

testSudo2 = [
  [1, 2, 3, 4],
  [3, 4, 2, 1],
  [2, 1, 4, 3],
  [4, 3, 1, 2]
]

testSudo3 = [
  [1, 2, 2, 4],
  [3, 4, 2, 1],
  [2, 1, 4, 3],
  [4, 3, 1, 2]
]

