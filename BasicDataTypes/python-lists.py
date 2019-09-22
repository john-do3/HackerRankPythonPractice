# https://www.hackerrank.com/challenges/python-lists/problem

lst = []
N = int(input())
for i in range(0,N):
    cmdline = input().split()
    cmd = cmdline[0]
    if (len(cmdline) > 1):
        arg1 = int(cmdline[1])
    if (len(cmdline) > 2):
        arg2 = int(cmdline[2])
    if cmd == 'insert':
        lst.insert(arg1, arg2)
    elif cmd == 'print':
        print(lst)
    elif cmd == 'remove':
        lst.remove(arg1)
    elif cmd == 'append':
        lst.append(arg1)
    elif cmd == 'sort':
        lst.sort()
    elif cmd == 'pop':
        lst.pop()
    elif cmd == 'reverse':
        lst.reverse()

