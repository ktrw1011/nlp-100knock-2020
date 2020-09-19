import pickle
with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

for sentence in neko_sentences:
    for item in sentence:
        if item['pos'] == '動詞':
            print(item['surface'])