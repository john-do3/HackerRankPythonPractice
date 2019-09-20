# https://www.hackerrank.com/challenges/finding-the-percentage/problem
from functools import reduce

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    name_marks = student_marks[query_name]

    print('{:.2f}'.format(reduce(lambda x,y: x+y,name_marks)/len(name_marks)))
