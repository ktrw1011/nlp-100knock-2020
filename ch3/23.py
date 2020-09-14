import re
from util import load_english_title

body = load_english_title()["text"]

# これだとNG
# 多分(.+)が最長一致で=をマッチさせるから
#print(re.findall(r"\n(=+)(.+)(=+)\n", body))

for m in re.finditer(r"\n(=+)(.*?)(=+)\n", body):
    # == でセクションが1より
    level = len(m.group(1)) - 1
    name = m.group(2)
    print(level, name)