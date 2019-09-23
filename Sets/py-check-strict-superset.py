# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, input().split()))
for i in range(0, int(input())):
    n = set(map(int, input().split()))
    if not A.issuperset(n):
        print(False)
        exit()

print(True)