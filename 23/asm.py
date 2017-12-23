a = 0
b = 67  # 1
c = b   # 2
d = 0
e = 0
f = 0
g = 0
h = 0

# count the number of mul
# smoke test for asm translation correctness
count = 0

# jumps > 0: if-else
# jumps < 0: do-while
if a != 0: # 2, 5
    b *= 100 # 5
    b += 100000 # 6
    c = b # 7
    c += 17000 # 8

while True: # 32
    f = 1 # 9 - flag register
    d = 2 # 10
    outer_g = True
    while outer_g: # 15, 20
        e = 2 # 11
        #print("outer")
        inner_g = True
        while inner_g:
            #print("inner")
            g = d # 12
            g *= e # 13
            count += 1
            g -= b # 14
            if g == 0: # 15
                f = 0 # 16
            e += 1 # 17
            g = e # 18
            g -= b # 19
            if g == 0: # 20
                inner_g = False
        d += 1 # 21
        g = d # 22
        g -= b # 23
        if g == 0: # 24
            outer_g = False
    if f == 0: # 25
        h += 1 # 26
    g = b # 27
    g -= c # 28
    if g == 0: # 29
        break # 30 - jump out
    b -= 17 # 31

print(count)
