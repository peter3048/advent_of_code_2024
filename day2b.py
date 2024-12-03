#too lazy to make this simpler

file = open('input.txt', 'r')
x = file.readlines()
total = 0

for i in x:
    i = i.strip()
    i = i.split(' ')

    i = list(map(int, i))
    tota = 0

    up = 0
    down = 0
    for j in range(0, len(i) - 1, 1):
        a = int(i[j])
        b = int(i[j+1])
        if(a > b):
            if(a - b < 4):
                down += 1
        if(a < b):
            if(b - a < 4):
                up += 1
    if ((len(i) - 1) == up  or (len(i) - 1) == down):
        tota += 1 

    for q in range(len(i)):
        if q > 0:
            i.insert(q-1, x)
        x = i.pop(q)
        up = sorted(i)
        down = sorted(i, reverse=True)

        if (i == up or i == down):
            tot = 0
            for p in range(len(i) - 1):
                if(up[p + 1] - up[p] < 4 and up[p + 1] - up[p] > 0):
                    tot += 1
            if(tot == len(i) - 1):
                tota += 1
    if(tota > 0):
        total += 1

print(total)
