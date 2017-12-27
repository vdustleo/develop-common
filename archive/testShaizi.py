STAT = {}
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                for m in range(1,7):
                    z = i + j + k + l + m
                    if z not in STAT:
                        STAT[z] = 1
                    else:
                        STAT[z] = STAT[z] + 1

for z in STAT:
    print(z, STAT[z], STAT[z]/(6*6*6*6*6))
    
