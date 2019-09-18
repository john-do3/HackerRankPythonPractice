# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    first = min(students, key=lambda x: x[1])[1]
    filtered = []
    for item in students:
        if item[1] != first:
            filtered.append(item)

    second = min(filtered, key=lambda x: x[1])[1]
    seconds = []

    for item in students:
        if item[1] == second:
            seconds.append(item[0])

    print('\n'.join(sorted(set(seconds))))
