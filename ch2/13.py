row = []
with open("./col1.txt") as f1, open("./col2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        row.append((line1.strip(), line2.strip()))

with open("./col1col2.txt", "w") as f:
    for item in row:
        f.write(item[0]+"\t"+item[1]+"\n")