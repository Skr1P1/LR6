#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Использовать словарь, содержащий следующие ключи: название начального пункта
# маршрута; название конечного пункта маршрута; номер маршрута. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть упорядочены по номерам маршрутов;
# вывод на экран информации о маршруте, номер которого введен с клавиатуры; если таких
# маршрутов нет, выдать на дисплей соответствующее сообщение.

import sys

if __name__ == '__main__':
    # Список .
    station = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные .
            finish = input("Название пункта назначения рейса ")
            number = input("Номер рейса ")
            start = input("Начального пункта ")

            # Создать словарь.
            st = {
                'finish': finish,
                'number': number,
                'start': start,
            }

            # Добавить словарь в список.
            station.append(st)
            # Отсортировать список в случае необходимости.
            if len(station) > 1:
                station.sort(key=lambda item: item.get('finish', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20}'.format(
                    "No",
                    "Пункт",
                    "Начало",
                )
            )
            print(line)

            # Вывести данные о всех рейсах.
            for idx, stations in enumerate(station, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} |'.format(
                        number,
                        stations.get('finish', ''),
                        stations.get('start', ''),
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])

            count = 0
            for stations in station:
                if stations.get('finish') == sel:
                    count = number
                    print(
                        '{:>4}: {}'.format(count, stations.get('start', ''))
                    )
                    print('Номер рейса:', stations.get('number', ''))
                    print('Пункт:', stations.get('finish', ''))

            # Если счетчик равен 0, то рейсы не найдены.
            if count == 0:
                print("Рейс не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <товар> - информация о рейсе;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)
