Rook move
Statement
Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
Code:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
# Math:
if a == c:
  print("YES")
elif b == d:
  print("YES")
else:
  print("NO")