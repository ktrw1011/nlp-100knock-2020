with open("./popular-names.txt") as f:
    col1 = [line.split()[0] for line in f.readlines()]

print(sorted(set(col1)))