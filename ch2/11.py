with open("./popular-names.txt") as f:
    text = f.read()

text = text.replace("\t", " ")

print(text)