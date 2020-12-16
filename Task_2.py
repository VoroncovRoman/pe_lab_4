#!/usr/bin/env python
# coding: utf-8

# In[9]:


# -----------------------------------------------------------------------------
#  Программная инженерия
#  Лабораторная 4 от 15.12.2020
# 
#  Задание 1. Пусть дана некоторая директория (папка). Посчитайте количество 
#  файлов в данной директории (папке) и выведите на экран
# -----------------------------------------------------------------------------

import os

def get_files_count(p: str) -> int:
    return len(os.listdir(p))

path = r'C:\Users\HP\Desktop\test'
files_count = get_files_count(path)

print(files_count)


# In[78]:


# -----------------------------------------------------------------------------
#  Программная инженерия
#  Лабораторная 4 от 15.12.2020
# 
#  Задание 2. Пусть дан файл students.csv, в котором содержится информация о
# студентах в виде No;ФИО;Возраст;Группа
#  1. Считайте информацию из файла в список списков ...
# -----------------------------------------------------------------------------

file = open(r'C:\Users\HP\Desktop\students.csv', 'r', encoding='utf-8')
data = file.read()
print(data)
file.close()


# In[79]:


row_list = data.split('\n')


# In[80]:


for i in range(len(row_list)):
    row_list[i] = row_list[i].split(';')
    
print(row_list)


# In[81]:


title = row_list.pop(0)
print(title)
print('---------')
for i in range(len(row_list)):
    print(row_list[i])
    


# In[82]:


sort_row_list = []
for i in range(len(row_list)):
    if int(row_list[i][2]) >= 24:
        sort_row_list.append(row_list[i])

print(title)
print('---------')
for i in range(len(sort_row_list)):
    print(sort_row_list[i])


# In[83]:


no = '11'
fio = 'Попов Василий Евгеньевич'
age = 25
group = 351617
row_list.append([no, fio, age, group])

for i in range(len(row_list)):
    print(row_list[i])


# In[84]:


new_str = ''
for i in range(len(row_list)):
    for j in range(len(row_list[i])):
        new_str += str(row_list[i][j])
        new_str += ';'
    row_list[i] = new_str
    new_str = ''
    
print(row_list)


# In[85]:


f = open(r'C:\Users\HP\Desktop\students1.csv', 'w')
for i in range(len(row_list)):
    f.write(row_list[i]+'\n')
f.close()


# In[28]:


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
#         sort_data_2 = self.older_then_N_age(data)
#         self.output(sort_data_2, title_data)
        
        # ЗАДАНИЕ 2.3. Реализуйте возможность записи данных в csv файл
        fio = 'Попов Васили Николаевич'
        age = 25
        group = 351617
        adding_data = self.add_data(data, fio, age, group)
        self.output(adding_data, title_data)

    

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
    
    
    # ЗАДАНИЕ 2.3. Реализуйте возможность записи данных в csv файл
    def add_data(self, data, fio, age, group):
        number = int(data[-1][0])
        data.append([str(number+1), fio, age, group])
        return data
        
    def save_file(self):
        
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

