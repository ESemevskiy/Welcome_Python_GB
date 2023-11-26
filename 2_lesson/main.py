"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
#
# my_list = ['A', 2, 2.2, None, True, (1, 2.2), {"1": 2, 3: complex(3, 2)}, [3, 4]]
#
# for elem in my_list:
#     print(f'Element {elem} - Type {type(elem)}')

"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input()
"""

# elem_list = []
#
# while True:
#     print("ВВедите число чтобы добавить в список")
#     print("Напишите 'run' чтобы закончить")
#
#     elem = input("Число: ")
#
#     if elem == 'run':
#         break #Выход из цикла ввода
#
#     if elem.isdigit():
#         elem_list.append(elem)
#
#     else:
#         print("Неправильный ввод, повторите")
#         continue # Было введено неправильное значение, повторите ввод
#
# elem_list_len = len(elem_list)
#
# if elem_list_len == 0:
#     print("Ваш список пуст")
#
# else:
#
#     eo = elem_list_len % 2 == 0
#
#     for idx, elem in enumerate(elem_list):
#         if idx % 2 == 0:
#             current_elem = elem_list[idx]
#             if eo:
#                 elem_list[idx], elem_list[idx + 1] = elem_list[idx + 1], elem_list[idx1]
#             else:
#                 if idx == elem_list_len - 1:
#                     continue
#                 else:
#                     elem_list[idx], elem_list[idx + 1] = elem_list[idx + 1], elem_list[idx]
#         else:
#             continue
#     print(elem_list)


"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""
season_list = ['зима', 'весна', 'лето', 'осень']


#########Лист############################
# season_list = [season for season in season_list for _ in range(3)]
#
# season_list[0], season_list[11] = season_list[11], season_list[0]
#
# month_number = int(input("Введите число от 1 до 12: "))
# if (month_number > 0) and (month_number < 13):
#     print(f'Ваш сезон - {month_number} : {season_list[month_number - 1]}')
# else:
#     print(f"Произошла ошибка ввода")

################Словарь#####################
# season_dict = dict(zip(range(1, 13), season_list))
#
# month_number = int(input("Введите число от 1 до 12: "))
# if (month_number > 0) and (month_number < 13):
#     print(f'Ваш сезон - {month_number} : {season_dict[month_number - 1]}')
# else:
#     print(f"Произошла ошибка ввода")



"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове
"""
#
# word_list = input("Введите слова разделенные пробелом: ").split()
#
# for idx, word in enumerate(word_list):
#     print(f"{idx} - {word[:10]}")

"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

# ranking_list = [7, 5, 3, 3, 2]
#
# a = int(input("Введите натуральное число: "))
#
# smaller_index = 0
#
# for r in ranking_list:
#     if r < a:
#         smaller_index = ranking_list.index(r)
#         break
#
# ranking_list.insert(smaller_index, a)
#
# print(f'Полученный список - {ranking_list}, индекс - {smaller_index}')

"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
© geekbrains.ru 38
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя
"""

goods_list = []

while True:
    if input("Создать товар (y/n)") == 'y':
        good = {'название': str(input("Введите название: ")), 'цена': int(input("Введите цену: ")) ,'Количество': int(input("Введите количество: ")),
                'ед': str(input('Введите единицы измерения (по умолчанию "шт"): ') or 'шт')}
        goods_list.append((len(goods_list) + 1, good))
    else:
        print('\n')
        print(f'{"_" * 20} Отчет по товарам {"_" * 20} ')
        for g in goods_list:
            print(g)
        break
print('\n')
print(f'{"_" * 20} Аналитика {"_" * 20} ')


keys_for_analytics = list(goods_list[0][1].keys())

analytics_dict = {k: [] for k in keys_for_analytics}

for _, k in goods_list:
    for key_, value_ in k.items():
        if value_ not in analytics_dict[key_]:
            analytics_dict.get(key_).append(value_)


for analytics, values in analytics_dict.items():
    print(f'{analytics} - {values}')
