Find the Runner-Up Score!
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Solution:

n = int(input())
arr = list(map(int,input().split()))
largest = max(arr)

for i in range(n):
  if largest == max(arr):
    arr.remove(max(arr))
print(max(arr))
