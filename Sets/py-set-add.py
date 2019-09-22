# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
stamps_countries = set()

for _ in range(n):
    stamps_countries.add(input())

print(len(stamps_countries))