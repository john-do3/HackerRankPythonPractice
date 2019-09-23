from functools import reduce
_, set_a, N = input(), set(input().split()), int(input())

for i in range(0, N):
    cmd, set_b = input().split(), set(input().split())
    if cmd[0] == 'update':
        set_a |= set_b
    if cmd[0] == 'intersection_update':
        set_a &= set_b
    if cmd[0] == 'symmetric_difference_update':
        set_a ^= set_b
    if cmd[0] == 'difference_update':
        set_a -= set_b

if (len(set_a)) > 0:
    print(reduce(lambda x, y: x + y, map(int, set_a)))
else:
    print(0)