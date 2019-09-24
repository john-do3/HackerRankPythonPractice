# https://www.hackerrank.com/challenges/exceptions/problem

T = int(input())

for i in range(0, T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)