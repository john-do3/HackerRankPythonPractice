# https://www.hackerrank.com/challenges/py-set-union/problem

n = input()
n_set = set(input().split())
b = input()
b_set = set(input().split())
print(len(n_set|b_set))