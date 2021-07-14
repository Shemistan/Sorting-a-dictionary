# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию.
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

import zipfile


class Grader:

    def __init__(self, zip_file_name=None, file_name=None):
        self.zip_file_name = zip_file_name
        self.file_name = file_name
        self.dictionary = {}
        self.checking = False

    def unziping(self):
        zfile = zipfile.ZipFile(self.zip_file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
            return filename

    def paint_for_table(self, a, b):
        print('+', '-' * 10, '+', '-' * 10, '+')
        print('| {:^10} |'.format(a), end='')
        print(' {:^10} |'.format(b))
        print('+', '-' * 10, '+', '-' * 10, '+')

    def creating_a_dictionary(self):  # создание словаря с символами и их количеством
        stat = {}
        if self.zip_file_name is not None:
            self.file_name = self.unziping()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in stat:
                            stat[char] += 1
                        else:
                            stat[char] = 1
        self.dictionary = stat
        self.checking = True

    def checking_dictionary_creation(self):  # оптимизация для однократного создания словаря
        if not self.checking:
            self.creating_a_dictionary()

    def sorted_by_value(self, revers=True):
        self.checking_dictionary_creation()
        summ = 0
        stat = self.dictionary
        sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=revers)
        self.paint_for_table(a='буква', b='частота')
        for i in sorted_stat:
            print('| {:^10} '.format(i[0]), end='')
            print('| {:^10} |'.format(i[1]))
            summ += i[1]
        self.paint_for_table(a='итого', b=summ)

    def sorted_by_value_descending(self):  # сортировка значений по убыванию
        self.sorted_by_value()

    def sorted_by_value_ascending(self):  # сортировка значений по возрастанию
        self.sorted_by_value(revers=False)

    def sorted_by_keys(self, revers=True):
        self.checking_dictionary_creation()
        stat = self.dictionary
        list_key = list(stat.keys())
        list_key.sort(reverse=revers)
        summ = 0
        self.paint_for_table(a='буква', b='частота')
        for i in list_key:
            print('| {:^10} '.format(i), end='')
            print('| {:^10} |'.format(stat[i]))
            summ += stat[i]
        self.paint_for_table(a='итого', b=summ)

    def sorted_by_keys_ascending(self):  # сортировка по возрастанию
        self.sorted_by_keys(revers=False)

    def sorted_by_keys_descending(self):  # сортировка по убыванию
        self.sorted_by_keys()


test = Grader(file_name='voyna-i-mir.txt')

test.sorted_by_value()
# test.sorted_by_value_ascending()
# test.sorted_by_value_descending()
# test.sorted_by_keys()
# test.sorted_by_keys_ascending()
# test.sorted_by_keys_descending()
