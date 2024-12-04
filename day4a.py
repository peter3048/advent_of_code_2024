file = open('input4.txt', 'r')
a = file.readlines()

total = 0
rows = len(a)
cols = len(a[0]) - 1
for y in range(rows):
    for x in range(cols):
        if a[y][x] == 'X':
            if y + 3 < rows:
                if a[y+1][x] == 'M' and a[y+2][x] == 'A' and a[y+3][x] == 'S':
                    total += 1

            if x + 3 < cols:
                if a[y][x+1] == 'M' and a[y][x+2] == 'A' and a[y][x+3] == 'S':
                    total += 1

            if x - 3 >= 0:
                if a[y][x-1] == 'M' and a[y][x-2] == 'A' and a[y][x-3] == 'S':
                    total += 1

            if y - 3 >= 0:
                if a[y-1][x] == 'M' and a[y-2][x] == 'A' and a[y-3][x] == 'S':
                    total += 1

            if y + 3 < rows and x + 3 < cols:
                if a[y+1][x+1] == 'M' and a[y+2][x+2] == 'A' and a[y+3][x+3] == 'S':
                    total += 1

            if y - 3 >= 0 and x - 3 >= 0:
                if a[y-1][x-1] == 'M' and a[y-2][x-2] == 'A' and a[y-3][x-3] == 'S':
                    total += 1

            if y + 3 < rows and x - 3 >= 0:
                if a[y+1][x-1] == 'M' and a[y+2][x-2] == 'A' and a[y+3][x-3] == 'S':
                    total += 1

            if y - 3 >= 0 and x + 3 < cols:
                if a[y-1][x+1] == 'M' and a[y-2][x+2] == 'A' and a[y-3][x+3] == 'S':
                    total += 1

print(total)
