List Comprehensions
https://www.hackerrank.com/challenges/list-comprehensions/problem


You are given three integers X,Y,Z and N representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N .

Solution:

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = []

for i in range (x+1):

  for j in range (y+1):

    for k in range (z+1):

        if ((i+j+k)!= n):
            lst.append([i,j,k])
print(lst)
