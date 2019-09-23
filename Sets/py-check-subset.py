# https://www.hackerrank.com/challenges/py-check-subset/problem

T = int(input())
for i in range(0, T):
    a, set_a = int(input()), set(map(int, input().split()))
    b, set_b = int(input()), set(map(int, input().split()))

    print(set_a.issubset(set_b))