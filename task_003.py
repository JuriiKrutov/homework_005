'''Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале,
игроки ходят поочередно, необходимо вывести карту
(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента,
каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка,
на которую мы хотим поставить крестик или нолик, и проверку на победу
( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)'''

import random
def draw_board(board):
   for i in range(3):
        print(board[0 + i *3], board[1 + i *3], board[2 + i *3])

def motion(player_1, player_2, count):
    if count % 2 == 0:
        return player_2
    else:
        return player_1

def vicktory(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[4] == board[7] or board[0] == board[4] == board[8] or board[2] == board[4] ==board[6]:
        return True



name_1 = input('Введите имя первого игрока: ')
name_2 = input('Введите имя второго игрока: ')

rnd = random.randrange(1,3)
board = [i for i in range(1,10)]

if rnd == 1:
    player_1 = name_1
    char_1 = 'X'
    player_2 = name_2
    char_2 = 'O'
else:
    player_1 = name_2
    char_1 = 'X'
    player_2 = name_1
    char_2 = 'O'

count = 1

while vicktory(board) != True:

    draw_board(board)

    hod = int(input(f'Ход {motion(player_1, player_2, count)}. Куда поставить {char_1 if motion(player_1, player_2, count) == player_1 else char_2}? '))
    if 0 < hod < 10 and board[hod - 1] != 'X' and board[hod - 1] != 'O':
        if motion(player_1, player_2, count) == player_1:
            board[hod - 1] = char_1
            count += 1
            if vicktory(board) == True:
                print(f'Ура!!! Победа {player_1}')
        else:
            board[hod - 1] = char_2
            count += 1
            if vicktory(board) == True:
                print(f'Ура!!! Победа {player_2}')
    else:
        print('Вы ввели неверное значение')
