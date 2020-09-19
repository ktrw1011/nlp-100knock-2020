from collections import deque

import pickle
with open('./neko.txt.mecab', 'rb') as f:
    neko_sentences = pickle.load(f)

for sentence in neko_sentences:
    queue = deque()
    for item in sentence:
        queue.append(item)

        if len(queue) == 3:
            if queue[0]["pos"] == "名詞" and queue[1]["surface"] == "の" and queue[2]["pos"] == "名詞":
                print(''.join([q["surface"] for q in queue]))
            queue.popleft()


        