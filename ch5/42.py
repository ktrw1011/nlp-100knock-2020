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
    for chunk in chunks:
        # 句読点などは出力しない
        chunk_surface = "".join([m.surface for m in chunk.morphs if m.pos != "補助記号"])

        chunk_surfaces.append(chunk_surface)
        chunk_dsts.append(chunk.dst)

    for i, dst in enumerate(chunk_dsts):
        if dst is not None:
            print(f"{chunk_surfaces[i]}\t{chunk_surfaces[dst]}")