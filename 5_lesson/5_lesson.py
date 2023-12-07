"""
1. Создать программно файл в текстовом формате,
 записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""

def write_text_to_file():

    with open('text_1.txt', 'w') as f:
        while True:
            line = input('Введите строку: ')
            if line == '':
                break
            f.write(line + '\n')

#write_text_to_file()

"""
2. Создать текстовый файл (не программно), 
сохранить в нем несколько строк, выполнить 
подсчет количества строк, количества слов в каждой строке.
"""

def count_lines_and_words_in_file():
    with open('text_2.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f'Количество строк в файле: {len(lines)}')
        for line in lines:
            words = line.split()
            print(f'Количество слов в строке: {len(words)}')

#сount_lines_and_words_in_file()

"""
3. Создать текстовый файл (не программно), построчно записать 
фамилии сотрудников и величину их окладов. Определить,
 кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников.
"""

def count_salary():
    with open('text_3.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        salary = 0
        count = 0
        for line in lines:
            line = line.split()
            if float(line[1]) < 20000:
                print(line[0])
            salary += float(line[1])
            count += 1
        print(f'Средняя величина дохода сотрудников: {salary / count}')

#count_salary()

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл 
на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
"""

def translate_numbers_to_rus():
    transelate_dict = {'One':'Один', "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
    with open('text_4.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()     
        for line in lines:
            line = line.split()
            line[0] = transelate_dict[line[0]]
            line = ' '.join(line)
            print(line)


#translate_numbers_to_rus()

"""
5. Создать (программно) текстовый файл, 
записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randrange

def count_sum_in_file():
    with open('text_5.txt', 'w+', encoding='utf-8') as f:
        for x in range(10):
            f.write(x:= f"{randrange(10)}\n")
    
    with open('text_5.txt', 'r',encoding='utf-8') as f:
        lines = f.readlines()
        print(lines)
        sum = 0
        for line in lines:
            for el in line.strip():
                sum += int(el)
        print(f'Сумма чисел в файле: {sum}')

#count_sum_in_file()


"""
Необходимо создать (не программно) текстовый файл,
 где каждая строка описывает учебный предмет и наличие лекционных,
   практических и лабораторных занятий по этому предмету и их количество.
 Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
 Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def read_diary():
    with open('text_6.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        diary = {}
        for line in lines:
            line = line.split()
            #line[0] = key
            sum = 0
            for el in line[1:]:
                digits = [char for char in el if char.isdigit()]
                if digits:
                    sum += int(''.join(digits))
                
                diary[line[0]] = sum
            
        print(diary)
                
#read_diary()


"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
 о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
 а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью. Если фирма получила убытки, также добавить
   ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

def firm():
    with open('text_7.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        list_dict = []
        dict = {}
        for line in lines:
            line = line.split()
            if int(line[2]) > int(line[3]):
                profit = int(line[2]) - int(line[3])
            dict[line[0]] = profit
        list_dict.append(dict)
        list_dict.append({'average_profit' : sum(dict.values()) / len(dict)})
    
    json_data = json.dumps(list_dict, ensure_ascii=False, indent=4)   
    return json_data


#print(firm())