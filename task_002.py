'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""'''

import random

def motion(player_1, player_2, count):
    if count % 2 == 0:
        return player_2
    else:
        return player_1

name_1 = input('Введите имя первого игрока: ')
name_2 = input('Введите имя второго игрока: ')

rnd = random.randrange(1, 3)

if rnd == 1:
    player_1 = name_1
    player_2 = name_2
else:
    player_1 = name_2
    player_2 = name_1

candy = 221
count = 1

while candy != 0:
    take = int(input(f"Ход {motion(player_1, player_2, count)}. На столе {candy} конфет. Вы можете взять"
                        f" не больше 28 конфет. Сколько вы возьмете? "))
    if 0 < take < 29 and take <= candy:
        candy -= take
        count += 1

        if candy == 0:
            print(f'Ура!!! Победа {motion(player_1, player_2, count - 1)}')
    else:
        print('Вы ввели неверное количество')

