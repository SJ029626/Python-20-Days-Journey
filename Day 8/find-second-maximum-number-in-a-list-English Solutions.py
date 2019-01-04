if __name__ == '__main__':
    #n = int(input())
    #ar = map(int, input().strip().split())
    n = int(input())
    ar = list({int(x) for x in input().split()})[:n]
    ar.sort()
    print(ar[-2])