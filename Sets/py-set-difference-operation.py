# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n, n_set = input(), set(input().split())
b, b_set = input(), set(input().split())
print(len(n_set.difference(b_set)))