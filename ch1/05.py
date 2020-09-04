def ngram(x, n):
    transpose = list(zip(*[x[i:] for i in  range(2)]))
    return [g for g in transpose]


sentence = "I am an NLPer"
print("char bi-gram", ngram(sentence, 2))
print("word bi-gram", ngram(sentence.split(), 2))
