import re

sentence_list = []

while True:
    sentence = list(map(str, input().split()))

    sentence_list += sentence

    if "E-N-D" in sentence_list:
        sentence_list.pop()
        break

max_size = 0
max_word = ""

for word in sentence_list:
    word = re.sub('[^a-z-]', '', word.lower())

    if len(word) > max_size:
        max_size = len(word)
        max_word = word

print(max_word)