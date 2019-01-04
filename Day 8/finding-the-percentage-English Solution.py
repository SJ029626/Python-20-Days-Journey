if __name__ == '__main__':
    n = int(input())
    marks = {}
    for _ in range(n):
        name, mark0, mark1, mark2 = input().split()
        marks[name] = tuple(float(x) for x in (mark0,mark1,mark2))
    s = input()
    print('{:.2f}'.format(sum(marks[s])/3))
