# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    result = []
    mylist = list(s)
    for s in mylist:
        if s.isupper():
            result.append(s.lower())
        else:
            result.append(s.upper())
    return ''.join(result)

if __name__ == '__main__':
    s = input().strip()
    print(swap_case(s))