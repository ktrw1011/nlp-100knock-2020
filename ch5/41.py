# 解析はGiNZAで行う
# 品詞細分類はtokenのtag属性の2番目を採用

import spacy
import ginza
nlp = spacy.load('ja_ginza')

from utils import Morph, Chunk, get_morphs, get_bunsetu_head_list_index

sentences = []
with open('./ai.ja.txt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        
        chunks = []

        # 解析
        doc = nlp(line)
        
        # 文節Head番号=(形態素解析した時のトークンindex)を取得
        bunsetu_head_list = ginza.bunsetu_head_list(doc)

        # 文節に分解
        for i, bunsetu in enumerate(ginza.bunsetu_spans(doc)):
            # 文節を表すChunkクラスをインスタンス化
            chunk = Chunk()
            # 文節を形態素解析
            morphs = get_morphs(bunsetu)
            # chunkのメンバ変数にappend
            chunk.morphs = morphs
            chunks.append(chunk)

            # 係り受け解析
            for token in bunsetu.lefts:
                # 文節トークンが係る元の文節indexを取得
                chunk_idx = get_bunsetu_head_list_index(bunsetu_head_list, token.i)
                chunks[chunk_idx].dst = i

                chunks[i].srcs.append(chunk_idx)

        sentences.append(chunks)
        

for i, chunks in enumerate(sentences):
    for chunk in chunks:
        print(chunk)
        print("="*40)
    if i >= 10:
        break
