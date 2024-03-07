def get_code(char):
    return 26 if char == ' ' else ord(char) - 97


def coding(text, key_text='abcdefgijk'):
    # chr(i), i - 97, ord(chr(i))
    res = ''
    for i, c in enumerate(text):
        res += chr((get_code(c) + get_code(key_text[i])) % 27 + 97)
    return res


def decoding(text, key_text='abcdefgijk'):
    res = ''
    for i, c in enumerate(text):
        decoded_char_code = (ord(c) - 97 - get_code(key_text[i])) % 27
        res += ' ' if decoded_char_code == 26 else chr(decoded_char_code + 97)
    return res


print('helloworld', 'hfnosauzun', coding('helloworld'))
print('aaaaaaaaa', 'bbbbbbbbbb', coding('aaaaaaaaa', 'bbbbbbbbbb'))
print('aaaaaaaaa', 'bbbbbbbbbb', decoding('bbbbbbbbbb', 'bbbbbbbbbb'))
print('hfnosauzun', 'helloworld', decoding('hfnosauzun'))
