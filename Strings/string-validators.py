# https://www.hackerrank.com/challenges/string-validators/problem
if __name__ == '__main__':
    s = list(input())

    print(any(c for c in s if c.isalnum()))
    print(any(c for c in s if c.isalpha()))
    print(any(c for c in s if c.isdigit()))
    print(any(c for c in s if c.islower()))
    print(any(c for c in s if c.isupper()))
