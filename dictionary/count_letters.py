def letter_counter(text):
    result = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
    return result


print(letter_counter('Poppy seeds'))
print(letter_counter('Bhagavad-gita'))
