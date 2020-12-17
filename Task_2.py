# -----------------------------------------------------------------------------
#  Программная инженерия
#  Лабораторная 4 от 15.12.2020
#
#  Задание 2. Пусть дан файл students.csv, в котором содержится информация о
# студентах в виде No;ФИО;Возраст;Группа
#  1. Считайте информацию из файла в список списков ...
# -----------------------------------------------------------------------------

import os
import pickle
from operator import itemgetter


class WorkWithStudent:

    def __init__(self):
        self.data = []
        self.title_data = []


    def read_file(self, path):
        file = open(path, 'r', encoding='utf-8')
        self.data = file.read()
        file.close()

        self.convert_str_to_list(self.data)


    def convert_str_to_list(self, d):
        list_of_studend = d.split('\n')
        for i in range(len(list_of_studend)):
            list_of_studend[i] = list_of_studend[i].split(';')
        self.title_data = list_of_studend.pop(0)
        self.data = list_of_studend

        self.output()



    def output(self, d=None, t=None):

        if d == None:
            d = self.data
        if t == None:
            t = self.title_data

        print(t, '\n---------------------------------------')
        for i in range(len(d)):
            print(d[i])



    # ЗАДАНИЕ 2.1. Выведите информацию о студентах, отсортировав их по фамилии
    def sort_by_fio(self):
        return sorted(self.data, key=itemgetter(1))


    # ЗАДАНИЕ 2.2. Выведите информацию о студентах, в возрасте старше 22 лет
    # ПРИМЕЧАНИЕ. В исходном датасете не было студентов с возрастом в 22 года.
    # Возраст изменен на 23 года
    def older_then_N_age(self):
        sorted_row_list = []
        for i in range(len(self.data)):
            if int(self.data[i][2]) >= 24:
                sorted_row_list.append(self.data[i])
        return sorted_row_list


    # ЗАДАНИЕ 2.3 и 2.4
    def add_data(self, fio, age, group):
        number = int(self.data[-1][0])
        self.data.append([str(number+1), fio, str(age), str(group)])


    def del_data(self):
        print('del_data: Данной функции еще нет, но вы держитесь там. Всего хорошего. Хорошего настроения Вам')

    def convert_rowlist_to_str(self):
        d = self.data
        t = self.title_data
        new_str = ''

        for i in range(len(t)):
            new_str += str(t[i])
            new_str += ';'
        t = [new_str]
        new_str = ''

        for i in range(len(d)):
            for j in range(len(d[i])):
                new_str += str(d[i][j])
                new_str += ';'
            d[i] = new_str
            new_str = ''
        return d, t

    def write_file(self, path):

        d, t = self.convert_rowlist_to_str()

        td = t + d

        f = open(path, 'w')
        for i in range(len(td)):
            f.write(td[i]+'\n')
        f.close()

    # ЗАДАНИЕ 2.5 и 2.6
    def save_pickle_file(self, path):
        pack = [self.title_data, self.data]

        f = open(path, 'wb')
        pickle.dump(pack, f)

    def load_pickle_file(self, path):
        f = open(path, 'rb')
        new_pack = pickle.load(f)

        print(new_pack)

if __name__ == '__main__':
    WWS = WorkWithStudent()