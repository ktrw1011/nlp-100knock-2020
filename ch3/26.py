import re
from util import load_english_title

body = load_english_title()["text"]

# https://ja.wikipedia.org/wiki/Template:%E5%9F%BA%E7%A4%8E%E6%83%85%E5%A0%B1_%E5%9B%BD
# より
country_template = {}
for m in re.finditer(r"\|(.+?)\s=\s+(.*)", body):
    # 強調マークアップの削除
    attr = re.sub(r"'+", "", m[2])
    country_template[m[1]] = attr

print(country_template)