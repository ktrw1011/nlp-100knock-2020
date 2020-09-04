import random

def word_shuffle(word):
    if len(word) <= 4:
        return word

    # not shuffle head and tail
    head = word[0]
    tail = word[-1]
    rest = list(word[1:-1])
    random.shuffle(rest)

    shuffled = head + "".join(rest) + tail

    return "".join(shuffled)


sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(" ".join([word_shuffle(word) for word in sentence.split()]))

