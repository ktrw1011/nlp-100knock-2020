# 解析はGiNZAで行う
# 品詞細分類はtokenのtag属性の2番目を採用

import spacy
nlp = spacy.load('ja_ginza')

from utils import Morph

sentences = []
with open('./ai.ja.txt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        doc = nlp(line)
        morphs = []
        for token in doc:
            pos_info = token.tag_.split('-')
            morph = Morph(
                surface=token.orth_,
                base=token.lemma_,
                pos=pos_info[0],
                pos1=pos_info[1] if len(pos_info) >= 2 else '',
            )
            morphs.append(morph)

        sentences.append(morphs)

for ms in sentences[0]:
    print(ms)
