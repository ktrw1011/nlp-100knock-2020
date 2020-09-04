def cipher(sentence):
    message = ""
    for s in sentence:

        if s.islower():
            message += chr(219 - ord(s))
        else:
            message += s

    return message

sentence = "Learn from yesterday, live for today, hope for tomorrow."
print('original sentence:', sentence)
encode_sentence = cipher(sentence)
print('encode sentence:', encode_sentence)
decode_sentence = cipher(encode_sentence)
print('decode sentence:', decode_sentence)
