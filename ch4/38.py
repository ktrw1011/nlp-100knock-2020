from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import pickle

with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

counter = Counter()
for sentence in neko_sentences:
    counter.update([item["surface"] for item in sentence])


plt.hist(x=list(counter.values()), bins=100)
plt.show()