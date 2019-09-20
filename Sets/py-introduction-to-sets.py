# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
from functools import reduce

def average(array):
    myset = set(array)
    return reduce(lambda x,y: x+y, myset)/len(myset)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)