punctuation_marks = ',.:;?!'
sentence = input('Enter a sentence with punctuation marks: ')
sentence_without = ''

for letter in sentence:
    if letter not in punctuation_marks:
        sentence_without += letter

print('Sentence without punctuation marks:', sentence_without)


