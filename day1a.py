file = open("input1.txt", "r")
x = file.readlines()
total = 0

a = []
b = []

for i in x:
    a.append(int(i[0:5]))
    b.append(int(i[8:13]))

a.sort()
b.sort()

for i in range(len(x)):
    total += abs(a[i] - b[i])

print(total)
