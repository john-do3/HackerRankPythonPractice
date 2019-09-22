# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n, n_set = input(), set(input().split())
b, b_set = input(), set(input().split())
print(len(n_set.intersection(b_set)))