if __name__ == '__main__':
    n=int(input())
    score = []
    for _ in range(n):
        name = input()
        grade = float(input())
        score.append([name,grade])
    givengrades = sorted({x[1] for x in score})
    sts = sorted(x[0] for x in score if x[1]==givengrades[1])
    for s in sts:
        print(s)