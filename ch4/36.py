from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import pickle

with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

counter = Counter()
for sentence in neko_sentences:
    counter.update([item["surface"] for item in sentence])

commons = counter.most_common()[:10]
plt.bar(x=[common[0] for common in commons], height=[common[1] for common in commons])
plt.show()