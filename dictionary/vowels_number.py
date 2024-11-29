def vowel_nuber(text):
    result = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in text.lower():
        if letter in 'aeiou':
            result[letter] += 1
    return result

print(vowel_nuber('ambrella'))
print(vowel_nuber('Every hotel could have a fancy bed'))
print(vowel_nuber('Harry Potter'))
print(vowel_nuber('I am a beginner programmer.'))
