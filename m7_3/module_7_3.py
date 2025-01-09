# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП
# Задача "Найдёт везде"

def del_punctuation(string):
    """
    Эта функция удаляет лишнюю пунктуацию из строки и переводит её в нижний регистр
    :param string: исходная строка с пунктуацией
    :return: строка без пунктуации в нижнем регистре
    """
    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
    for symbol in punctuation:
        string = string.replace(symbol, '')
    return string.lower()


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        words = []
        for file in self.file_names:
            with open(file, encoding='utf-8') as open_file:
                for line in open_file:
                    line = del_punctuation(line)
                    words.extend(line.split())
            all_words[file] = words
            words = []
        return all_words

    def find(self, word):
        find_words = dict()
        for name, words in self.get_all_words().items():
            i = 0
            for word_now in words:
                i += 1
                if word_now == word.lower():
                    find_words[name] = i
                    break
        return find_words

    def count(self, word):
        count_words = dict()
        for name, words in self.get_all_words().items():
            i = 0
            for word_now in words:
                if word_now == word.lower():
                    i += 1
            if i != 0:
                count_words[name] = i
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

