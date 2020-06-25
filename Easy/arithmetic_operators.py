Arithmetic Operators
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

Read two integers from STDIN and print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Solution:

a = int(input())
b = int(input())


print((a+b),(a-b),(a*b),sep='\n')
