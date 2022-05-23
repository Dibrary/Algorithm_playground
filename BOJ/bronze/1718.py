
alphabet = "abcdefghijklmnopqrstuvwxyz"

sentence = input()
pw_key = input()

result = ""
for idx, s in enumerate(sentence):
    if s == " ":
        result += " "
    else:
        key_index = alphabet.index(pw_key[idx%len(pw_key)])
        sentence_index = alphabet.index(s)
        value = sentence_index - key_index -1
        if value < 0:
            value = 26+value
        result += alphabet[value]

print(result)


