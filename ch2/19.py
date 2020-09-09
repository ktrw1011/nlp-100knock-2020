from collections import Counter

with open("./popular-names.txt") as f:
    col1 = [line.split()[0] for line in f.readlines()]

counter = Counter(col1)

# デフォルトで数値ソートするっぽい
print(sorted(counter.items(), key=lambda x: x[1], reverse=True))