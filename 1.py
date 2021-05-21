#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.

if __name__ == '__main__':
    school = {'1а': 20, '1б': 17, '2а': 18, '2б': 23, '3a': 24, '3б': 22, '4а': 25, "4б": 27}
    while True:
        print('change - Изменилось количество учеников:')
        print('new - В школе появился новый класс')
        print('remove - В школе был расформирован (удален) класс')
        print('print - Выгрузка данных')
        print('sum - Число учеников')
        print('exit - Выход')
        n = input('Введите название операции >>> ')
        if n == 'change':
            school.update({input(f'Название изменяемого класса: '):
                        int(input(f'Количество учеников изменяемого класса: '))})
        elif n == 'new':
            school.update({input(f'Название класса №: '): int(input(f'Количество учеников класса №: '))})
        elif n == 'remove':
            del school[input(f'Название расформировываемого класса: ')]
        elif n == 'print':
            print(school)
        elif n == 'sum':
            print(sum(school.values()))
        elif n == 'exit':
            break

