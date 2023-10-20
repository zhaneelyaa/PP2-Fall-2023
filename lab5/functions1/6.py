def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
result = reverse_words(input_sentence)
print(result)

