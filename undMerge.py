####################################################
# mergeSort still not understood
####################################################

def merge(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
#    print"start: ",index1, index2, length, a, aux
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
 #       print index1, index2, length, a, aux
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort(a):
  n = len(a)
  step = 1
  while (step < n):
#    print(n, step, a, len(a))
    for start1 in range(0, n, 2*step):
      start2 = min(start1 + step, n)
      end = min(start1 + 2*step, n)
#      print("inside for",start1, start2, end, a)
      merge(a, start1, start2, end)
    step *= 2


def testMerge():
  a = [3,2,18,9,34,6,5,7,12,15,17,11]
  mergeSort(a)
  print(a)

testMerge()
