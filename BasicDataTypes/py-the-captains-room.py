# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k, k_list = int(input()), list(map(int, input().split()))
room_hash = dict()

for item in k_list:
    if item in room_hash:
        room_hash[item] += 1
    else:
        room_hash[item] = 1

for key, v in room_hash.items():
    if v < k:
        print(key)