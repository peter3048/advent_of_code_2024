file = open("input1.txt", "r")
x = file.readlines()
total = 0

a = []
b = []

for i in x:
    a.append(int(i[0:5]))
    b.append(int(i[8:13]))

for o in a:
    tot = 0
    for p in b:
        if o == p:
            tot += 1
    total += tot * o        

print(total)


