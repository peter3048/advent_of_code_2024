file = open('input3.txt', 'r')
a = file.readlines()
total = 0
do = True

for p in a:
    for i in range(len(p)):
        if(p[i:i+4] == 'do()'):
            do = True
        if(p[i:i+7] == "don't()"):
            do = False

        if(p[i:i+4] == 'mul(' and do):
            str = p[i + 4:i+12]
            str = str.split(",")
            try:
                str[1] = str[1].split(")")
                try:
                    if(str[0].find(' ') == -1 and str[1][0].find(' ') == -1):
                        total += int(str[0]) * int(str[1][0])
                except:
                    total += 0
            except:
                total += 0   
            
print(total)

        
