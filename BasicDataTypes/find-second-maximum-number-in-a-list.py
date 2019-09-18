# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

first = -101
second = first

for i in arr:
    if first < i:
        first = i

for i in arr:
    if i != first:
        if (second < i):
            second = i

print(second)
