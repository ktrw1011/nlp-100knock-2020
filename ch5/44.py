# spacyに内包されているレンダリングを使って可視化する
import spacy
import random
import ginza
nlp = spacy.load('ja_ginza')

from utils import Morph, Chunk, get_morphs, get_bunsetu_head_list_index, analysis_bunsetu

sentences = []
with open('./ai.ja.txt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        doc = nlp(line)
        chunks = analysis_bunsetu(doc)
        sentences.append(chunks)

# ランダムに一つ選択
chunks = random.choice(sentences)
arcs = []
words = []
for i, chunk in enumerate(chunks):
    words.append({'text':"".join([m.surface for m in chunk.morphs if m.pos != "補助記号"]), "tag":""})
    if chunk.dst is not None:
        arcs.append({
            'start':i,
            'end':chunk.dst,
            'label':"",
            'dir':'right',
        })

# ブラウザで見れる
spacy.displacy.serve(
    {"words":words, 'arcs':arcs},
    style='dep',
    manual=True
)