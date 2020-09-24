import spacy
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


for chunks in sentences:
    chunk_surfaces = []
    chunk_dsts = []
    # 文節の属性
    chunk_poss = []
    for chunk in chunks:
        chunk_surface = "".join([m.surface for m in chunk.morphs if m.pos != "補助記号"])
        chunk_pos = [m.pos for m in chunk.morphs]

        chunk_surfaces.append(chunk_surface)
        chunk_dsts.append(chunk.dst)
        chunk_poss.append(chunk_pos)

    for i, dst in enumerate(chunk_dsts):
        if dst is not None:
            # 名詞を含む文節が動詞を含む文節に係る場合のみ表示
            if "名詞" in chunk_poss[i] and "動詞" in chunk_poss[dst]:
                print(f"{chunk_surfaces[i]}\t{chunk_surfaces[dst]}")