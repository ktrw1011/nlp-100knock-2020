import math

n = int(input())

with open("./popular-names.txt") as f:
    rows = f.readlines()

# 切り上げ
total = 0
split_num = math.ceil(len(rows)/n)
for i, j in enumerate(range(0, len(rows), split_num)):
    subset_row = rows[j:j+split_num]
    total += len(subset_row)
    with open(f"text_{i+1}.txt", "w") as f:
        for item in subset_row:
            f.write(item)

assert total == len(rows)