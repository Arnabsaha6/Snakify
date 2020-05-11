Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.
Code:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
square1 = "none"
square2 = "none"
# Math:
# square1
if a%2 == 1:
  if b%2 == 1:
    square1 = "black"
  else:
    square1 = "white"
else:
  if b%2 == 0:
    square1 = "black"
  else:
    square1 = "white"
# square2
if c%2 == 1:
  if d%2 == 1:
    square2 = "black"
  else:
    square2 = "white"
else:
  if d%2 == 0:
    square2 = "black"
  else:
    square2 = "white"

if square1 == square2:
	print("YES")
else:
	print("NO")