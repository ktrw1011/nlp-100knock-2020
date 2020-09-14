import re
from util import load_english_title

body = load_english_title()["text"]

for m in re.finditer(r"\[\[ファイル:(.*?)\|", body):
    print(m.group(1))