import re
from util import load_english_title

body = load_english_title()["text"]

def remove_inner_link(text):
    # [A]のみならその中の単語(A)を取り出して
    # [A|B]であれば(B)を取り出す
    def func1(m):
        inner_text = m[1]
        inner_text = re.sub(r".+\|(.+)", func2, inner_text)
        return inner_text

    def func2(m):
        return m[1]
# https://ja.wikipedia.org/wiki/Template:%E5%9F%BA%E7%A4%8E%E6%83%85%E5%A0%B1_%E5%9B%BD
# より
country_template = {}
for m in re.finditer(r"\|(.+?)\s=\s+(.*)", body):
    # 強調マークアップの削除
    attr = re.sub(r"'+", "", m[2])

    # 内部リンクの削除
    # [[記事名#節名|表示文字]]
    attr = remove_inner_link(attr)

    country_template[m[1]] = attr

print(country_template)