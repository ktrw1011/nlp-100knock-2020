n = int(input())

with open("./popular-names.txt") as f:
    for i, line in enumerate(f, 1):
        if i >= n:
            break
        else:
            print(line.strip())