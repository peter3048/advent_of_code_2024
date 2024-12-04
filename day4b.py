file = open('input4.txt', 'r')
a = file.readlines()

total = 0
rows = len(a)
cols = len(a[0]) - 1
for y in range(rows):
    for x in range(cols):
        if a[y][x] == 'A' and y > 0 and x > 0 and y < rows - 1 and x < cols - 1:
                if ((a[y+1][x+1] == 'M' and a[y-1][x-1] == 'S') or (a[y+1][x+1] == 'S' and a[y-1][x-1] == 'M')) and ((a[y-1][x+1] == 'M' and a[y+1][x-1] == 'S') or (a[y-1][x+1] == 'S' and a[y+1][x-1] == 'M')):
                    total += 1
                  
print(total)
