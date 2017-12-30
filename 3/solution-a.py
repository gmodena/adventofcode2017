from math import sqrt

def closed_form(end):
    # TODO(gmodena): this works only if n
    # and end are on the same arm of the spiral
    n = round(sqrt(end))
    distance = n*n - end
    return n - distance -1

if __name__ == '__main__':
    end = int(input())
    print(closed_form(end))
