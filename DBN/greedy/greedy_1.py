import sys

def greedy():

  n, m, k = map(int, sys.stdin.readline().split())
  nums = sorted(map(int, sys.stdin.readline().split()))
  first = nums[n-1]
  second = nums[n-2]
  print((first*k + second) * (m // (k + 1))+(m % (k + 1) * first))


greedy()
