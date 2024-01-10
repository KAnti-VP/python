# -*- coding: utf-8 -*-


class Filehandler:

    def __init__(self) -> None:
        self.content = []
    
    def read_file(self, file_path_name: str, sep: str = '') -> None:
        with open(file_path_name, 'r', encoding='utf-8') as file:
            for row in file:
                self.content.append(row.strip().split(sep))
    
    def get_content(self) -> list:
        return self.content

    def write_consonants(self):
        with open('massalhangzo.txt', 'w+', encoding='utf-8') as file:
            for row in self.content:
                line = ''
                for word in row:
                    if word[0] in 'qwrtzplkjhgfdsyxcvbnm':
                        line += f'{word}, '
                file.write(line[:-2] + '\n')

    def write_vowels(self):
        with open('maganhangzo.txt', 'w+', encoding='utf-8') as file:
            line = ''
            for row in self.content:
                for word in row:
                    if word[0] in 'aeiouáéyóöőúüű':
                        line += f'{word} '
            file.write(line[:-1])


def print_longet_then_4(arr: list) -> None:
    for row in arr:
        for word in row:
            if len(word) > 4:
                print(word, end=' ')
        print()


def number_of_max_len_4_words(arr):
    count: int = 0
    for row in arr:
        for word in row:
            count += len(word) < 5
    return count


def print_random_word(arr):
    import random
    for row in arr:
        print(row[random.randint(0, len(row) - 1)])


if __name__ == '__main__':
    fh = Filehandler()
    fh.read_file('words_hu.txt', ', ')
    cont = fh.get_content()

    print('1. feladat:')
    print_longet_then_4(cont)

    print('2. feladat:')
    print(number_of_max_len_4_words(cont))

    print('3. feladat:')
    print_random_word(cont)

    print('4. feladat:')
    fh.write_consonants()

    print('5. feladat:')
    fh.write_vowels()
