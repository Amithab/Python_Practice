import random

def simpleStats(a):
  if len(a) == 0:
    return None
   
  mean = sum(a)/len(a)

  b = sorted(a)
  if len(a)%2 == 0:
    median = (b[int(len(a)/2)] + b[int(len(a)/2)-1])/2
  else:
    median = b[int(len(a)/2)]

  mode = max(set(a), key=a.count)
  return (mean, median, mode)


def test(tests):
  for i in range(tests):
    lst = makeRandomList()
    print(lst, simpleStats(lst))

def makeRandomList():
  length = random.randint(1, 10)
  lst = []

  for i in range(length):
    lst.append(random.randint(0, 100))
  return lst

print(simpleStats([3,5,8,2,2]))

test(10)
