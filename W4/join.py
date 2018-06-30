def join(L, delimiter):
  joinedString =""
  for i in L:
    joinedString+=i
    if L.index(i) != len(L)-1:
      joinedString+=delimiter
  return joinedString


print(join(["ab","cd","efg"], ","))
