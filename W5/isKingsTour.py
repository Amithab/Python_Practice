def isKingsTour(board):
  N = len(board)
  x = [x for x in board if 1 in x][0]
  rpos = board.index(x)
  cpos = x.index(1)

  for i in range(1, N**2):
    foundNext = False
    for r in range(rpos-1, rpos+2):
      for c in range(cpos-1, cpos+2):
        #print(r, c, board[r][c])
        if correctPosition(r, c, N) and not (r == rpos and c == cpos) and board[r][c] == i+1:
          rpos = r
          cpos = c
          foundNext = True
          break

      if foundNext:
        break
    if not foundNext:
      return False
  return True

          

"""
def findAdjacent(board, row, col, N):
  arr = []
  for r in range(row-1, row+2):
    for c in range(col-1, col+2):
      if correctPosition(r, c, N) and not r == row and not c == col:
        arr.append(board[r][c])
  return arr
"""
def correctPosition(r, c, N):
  if r< N and r >= 0 and c < N and c >= 0:
    return True
  return False


testKings = [ [3, 2, 1], [6, 4, 9], [5, 7, 8] ]
testKings2 = [ [1, 2, 3], [7, 4, 8], [6, 5, 9] ]
testKings3 = [ [3, 2, 1], [6, 4, 9], [5, 7, 8] ]
testKings4 = [ [1, 14, 15, 16], [13, 2, 7, 6], [12, 8, 3, 5], [11, 10, 9, 4] ]

print(isKingsTour(testKings))
print(isKingsTour(testKings2))
print(isKingsTour(testKings3))
print(isKingsTour(testKings4))
