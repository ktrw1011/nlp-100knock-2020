import spacy
import random
import ginza
nlp = spacy.load('ja_ginza')

from utils import *

sentences = []
with open('./ai.ja.txt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        doc = nlp(line)
        chunks = analysis_bunsetu(doc)
        sentences.append(chunks)


with open("ans_48.txt", "w") as f:
    for chunks in sentences:
        nodes = []
        for chunk in chunks:
            if check_meishi(chunk.morphs):
                chunk_surface = get_chunk_surface(chunk, exclude_kigou=True)
                nodes.append([chunk_surface])
                
                dst = chunk.dst
                while dst:
                    dst_chunk = chunks[dst]
                    dst_chunk_surface = get_chunk_surface(dst_chunk, exclude_kigou=True)
                    nodes[-1].append(dst_chunk_surface)
                    dst = dst_chunk.dst

        for node in nodes:
            if len(node) > 1:
                f.write(" -> ".join(node)+"\n")