# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n, n_set = input(), set(input().split())
b, b_set = input(), set(input().split())
print(len(n_set.symmetric_difference(b_set)))