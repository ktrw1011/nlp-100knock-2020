sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence = sentence.split()

selects = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {}

for i, word in enumerate(sentence, 1):
    if i in selects:
        result[word[0]] = i
    else:
        result[word[:2]] = i

print(result)