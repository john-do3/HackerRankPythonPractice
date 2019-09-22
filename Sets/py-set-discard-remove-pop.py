# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

from functools import reduce

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(0,N):
    command = input()
    if command == 'pop':
        s.pop()
    else:
        command = command.split()
        arg = int(command[1])
        if (command[0] == 'remove'):
            s.remove(arg)
        else:
            s.discard(arg)

if (len(s)) > 0:
    print(reduce(lambda x,y: x+y, s))
else:
    print(0)