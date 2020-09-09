with open("./popular-names.txt") as f:
    col3 = [int(line.split()[2]) for line in f.readlines()]

print(sorted(col3, reverse=True))