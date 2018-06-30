def letterCounts(s):
  counts = [0]*26
  for ch in s.upper():
    if ((ch>="A") and (ch <= "Z")):
      counts[ord(ch)-ord("A")]+=1
  return counts



def testCounts():
  for i in ["a","b","c","abc","ab","ac","hello","locker","alphabet",
            "ice cream"]:
    print( letterCounts(i))

def areAlmostAnagrams(s1, s2):
  if abs(len(s1)-len(s2)) >1:
    return False
  
  oneCount = letterCounts(s1)
  twoCount = letterCounts(s2)
  
  countDiff=0

  for i in range(len(oneCount)):
    if oneCount[i] != twoCount[i]:
      countDiff+=1

  if countDiff>1:
    return False
  return True

def testAlmostAnagrams():
  for s1,s2 in [("lemon", "melon"), ("class","slacks"),("dog","bog")]:
    print( s1, s2, areAlmostAnagrams(s1,s2))


testAlmostAnagrams()
