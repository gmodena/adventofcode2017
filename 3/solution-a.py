from math import sqrt
if __name__ == '__main__':
    end = int(input())
    n = round(sqrt(end))
    distance = n*n - end
    print(n - distance -1)
