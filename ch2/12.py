col1 = []
col2 = []
with open("./popular-names.txt") as f:
    for line in f:
        line = line.strip().split("\t")
        col1.append(line[0])
        col2.append(line[1])

with open("./col1.txt", "w") as f:
    for item in col1:
        f.write(item+'\n')

with open("./col2.txt", "w") as f:
    for item in col2:
        f.write(item+'\n')

