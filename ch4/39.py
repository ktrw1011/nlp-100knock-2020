# ジップの法則
# 頻出順位がk番目の頻度は頻出順位1番目の頻度を1/kした値になる法則
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import pickle
import math

with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

counter = Counter()
for sentence in neko_sentences:
    counter.update([item["surface"] for item in sentence])

words, word_freqs = zip(*counter.most_common())
word_freq_rank = range(0, len(words))

word_freq_rank = [math.log(x+1) for x in word_freq_rank]
word_freqs = [math.log(x) for x in word_freqs]

plt.scatter(word_freqs, word_freq_rank )
plt.show()