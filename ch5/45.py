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


with open("ans_45.txt", "w") as f:
    for chunks in sentences:
        for chunk in chunks:
            # 文節に動詞を含むか調べる
            attrs = [m.pos for m in chunk.morphs]
            if "動詞" in attrs:
                # 基本形
                base_word = chunk.morphs[attrs.index("動詞")].base
                # 係り先
                srcs = chunk.srcs
                
                # 係り元の助詞を集める
                jyosis = []
                for i in srcs:
                    jyosi = ""
                    for m in chunks[i].morphs:
                        if m.pos == "助詞":
                            jyosi += m.surface
                    
                    if jyosi != "":
                        jyosis.append(jyosi)
                    
                if len(jyosis) > 0:
                    f.write(base_word+"\t"+"\t".join(jyosis)+"\n")