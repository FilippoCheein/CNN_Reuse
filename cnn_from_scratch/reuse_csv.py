
result = []
with open('reuse_stats2.csv', 'w+') as s:
    with open('reuse_out2', 'r') as r:
        while(1):
            line = r.readline()
            if(len(line) == 0):
                break
            line = line.split()
            found = False
            for entry in result:
                if line[1] == entry:
                    entry[1] += 1
                    found = True
                    break
            if found == False:
                result.append([line[1], 1]) # [frequency, frequency of frequency]

        for e in result:
                r.write(e[0] + ", " + e[1] + "\n")

        
