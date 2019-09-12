word_count = {}
text_to_enter = input("Enter some text: ")
word_occurrences = text_to_enter.split()
for word in word_occurrences:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1
word_occurrences = list(word_count.keys())
word_occurrences.sort()
max_length = max((len(word) for word in word_occurrences))
for word in word_occurrences:
    print("{:{}} : {}".format(word, max_length, word_count[word]))
