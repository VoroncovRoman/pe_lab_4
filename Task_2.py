import os
from operator import itemgetter

class WorkWithStudent:
    def __init__(self):
        data = self.read_file(r'C:\Users\HP\Desktop\students.csv')
        data, title_data = self.convert_str_to_list(data)

        # ЗАДАНИЕ 2.1. Выведите информацию о студентах, отсортировав их по фамилии
#         sort_data_1 = self.sort_by_age(data)
#         self.output(sort_data_1, title_data)

        # ЗАДАНИЕ 2.2. Выведите информацию о студентах, в возрасте старше 23 лет
        sort_data_2 = self.older_then_N_age(data)
        self.output(sort_data_2, title_data)


    def read_file(self, path):
        file = open(path, 'r', encoding='utf-8')
        data = file.read()
        file.close()
        return data

    def convert_str_to_list(self, data):
        list_of_studend = data.split('\n')
        for i in range(len(list_of_studend)):
            list_of_studend[i] = list_of_studend[i].split(';')
        title = list_of_studend.pop(0)
        return list_of_studend, title

    def output(self, d, t):
        print(t, '\n---------------------------------------')
        for i in range(len(d)):
            print(d[i])


    # ЗАДАНИЕ 2.1. Выведите информацию о студентах, отсортировав их по фамилии
    def sort_by_age(self, d):
        return sorted(d, key=itemgetter(1))


    # ЗАДАНИЕ 2.2. Выведите информацию о студентах, в возрасте старше 22 лет
    # ПРИМЕЧАНИЕ. В исходном датасете не было студентов с возрастом в 22 года.
    # Возраст изменен на 23 года
    def older_then_N_age(self, d):
        sorted_row_list = []
        for i in range(len(d)):
            if int(d[i][2]) >= 24:
                sorted_row_list.append(d[i])
        return sorted_row_list



    def add_entry(self):
        pass
    '''Проходим по списку строки и все элементы загружаем в переменную,
    используя конкатинацию строк и точку с запятой (;)
    Затем проходим по списку таблицы и производим конкатинацию с знаком
    перехода на новую строку (\n).
    Если это не сработает, то тогда не будем юзать (\n), а просто заполним
    текстовый файл циклом
    '''

if __name__ == '__main__':
    WWS = WorkWithStudent()

