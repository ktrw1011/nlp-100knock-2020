from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import pickle

with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

# 共起を考えるspanを一文として考える
counter = Counter()
for sentence in neko_sentences:
    for item in sentence:
        if item["surface"] == "猫":
            counter.update([s["surface"] for s in sentence if s["surface"] != "猫"])

commons = counter.most_common()[:10]
plt.bar(x=[common[0] for common in commons], height=[common[1] for common in commons])
plt.show()