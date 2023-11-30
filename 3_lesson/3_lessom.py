# Урок 3. Функции

"""

1. Реализовать функцию, принимающую два числа (позиционные аргументы) 
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
 обработку ситуации деления на ноль.

"""

def div():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    try:
        return a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    
"""
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как 
 именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

def user_data(name, surname, year, city, email, phone):   
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {city}, Email: {email}, Телефон: {phone}")
    

"""
3. Реализовать функцию my_func(), которая принимает 
три позиционных аргумента, и
 возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    return a + b + c - min(a, b, c)

"""
4. Программа принимает действительное положительное
 число x и целое отрицательное число y. Необходимо 
 выполнить возведение числа x в степень y. 
 Задание необходимо реализовать в виде функции
   my_func(x, y). При решении задания необходимо обойтись без 
   встроенной функции возведения числа в степень.
"""

def my_func_power(x, y):
    if y < 0 and float(x):
        p  = x
        for _ in range(1, abs(y)):
            x *= p
        print(f"Test: {pow(x, abs(y))}]")
        return round(1/x, 4) 
    else:
        print("Ошибка вводы")

"""
5. Программа запрашивает у пользователя строку чисел, 
разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать
   Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
     Но если вместо числа вводится специальный символ, выполнение программы 
     завершается. Если специальный символ введен после нескольких чисел, 
     то вначале нужно добавить сумму этих чисел к полученной ранее сумме 
     и после этого завершить программу.
"""
 
def sum_numbers():
    total_sum = 0
    proxy_sum = []
    while True:
        list_of_numbers = input("Введите числа через пробел: ").split()
        if 'q' in list_of_numbers:     
            break
        else:
            int_list_of_numbers = list(map(int, list_of_numbers))
            total_sum += sum(int_list_of_numbers)
            proxy_sum = sum(int_list_of_numbers)
            print(f"Промежуточная Сумма: {proxy_sum}Сумма чисел: {total_sum}")
 

"""
 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и в
 озвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
 пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной 
 строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать
   написанную ранее функцию int_func().
 """

def int_func():

    def check_word(word):
        for w in word:
            if ord(w) > 96 and ord(w) < 123:
                continue
            else:
                return False
        return True
    
    text =  list(input("Введите слово из маленьких латинских букв: ").split())
    return str([a.capitalize() for a, b in zip(text, list(map(check_word, text))) if b])

