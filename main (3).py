N = int(input("N:"))
h = input("h: ")
w = input("w: ")

list1 = list(h.replace(" ", ""))
list2 = list(w.replace(" ", ""))
hList = [int(i) for i in list1]
wList = [int(i) for i in list2]

Area = 0

for n in range(N):
  height1 = hList[n]
  height2 = hList[n+1]
  heightTri = abs(height2 - height1)
  width = wList[n]
  if height1 > height2:
    tallH = height1
    shortH = height2
  else:
    tallH = height2
    shortH = height1
  singleArea = (shortH * width) + ((heightTri * width) / 2)
  Area = Area + singleArea

print(Area)





