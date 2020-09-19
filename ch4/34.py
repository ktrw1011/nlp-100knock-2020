from collections import deque

import pickle
with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

for sentence in neko_sentences:
    candidate = []
    nouns = []
    for item in sentence:
        if item["pos"] == "名詞":
            nouns.append(item["surface"])
        else:
            if len(nouns) > 0:
                candidate.append(nouns)
            nouns = []

    if len(candidate) > 0:
        print(''.join(max(candidate)))