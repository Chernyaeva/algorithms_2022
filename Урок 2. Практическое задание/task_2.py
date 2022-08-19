"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def recurs_count_odd_even_numbers(number, odd_num = 0, even_num = 0):

    if number:
        rem = number % 10
        number = number // 10
        if rem % 2 == 0:
            return recurs_count_odd_even_numbers(number, odd_num, even_num + 1)
        else:
            return recurs_count_odd_even_numbers(number, odd_num + 1, even_num)
    else:
        return even_num, odd_num

a = input('Введите число: ')
print(f'Количество четных и нечетных цифр в числе равно: {recurs_count_odd_even_numbers(int(a))}')