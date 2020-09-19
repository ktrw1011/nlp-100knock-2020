from collections import Counter

import pickle
with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

counter = Counter()
for sentence in neko_sentences:
    counter.update([item["surface"] for item in sentence])

print(counter)