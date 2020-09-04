def ngram(x, n):
    transpose = list(zip(*[x[i:] for i in  range(2)]))
    return [g for g in transpose]

sentence1 = "paraparaparadise"
sentence2 = "paragraph"

X = set(ngram(sentence1, 2))
Y = set(ngram(sentence2, 2))

print("Union", X.union(Y))
print("Intersection", X.intersection(Y))
print("difference", X.difference(Y))

print('se in X', any([True for element in X if ('s', 'e') == element]))
print('se in y', any([True for element in Y if ('s', 'e') == element]))


