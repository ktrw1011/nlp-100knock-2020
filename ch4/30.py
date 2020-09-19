import pprint
import pickle
with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

for i, sentence in enumerate(neko_sentences):
    pprint.pprint(sentence)
    # too long
    if i > 10:
        break