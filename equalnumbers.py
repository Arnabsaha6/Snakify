Equal numbers
Statement
Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

Code:
a=int(input())
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if (a==b and a==c and b==c):
  print (3) # all are same
elif (a==b and a!=c and b!=c) or (b==c and b!=a and c!=a)or (c==a and c!=b and a!=b):
  print (2) # two of the numbers are same
else:
  print (0)