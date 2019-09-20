# https://www.hackerrank.com/challenges/symmetric-difference/problem
if __name__ == '__main__':
    M = int(input())
    M_list = map(int, input().split())
    N = int(input())
    N_list = map(int, input().split())

    M_list = set(M_list)
    N_list = set(N_list)

    difM = M_list.difference(N_list)
    difN = N_list.difference(M_list)
    u = difM.union(difN)

    print('\n'.join(list(map(str, sorted(u)))))