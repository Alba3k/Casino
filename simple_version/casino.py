# импорт необходимых библиотек
from terminaltables import AsciiTable, DoubleTable, SingleTable
from colorama import Fore, Back, Style
from colorama import init
from art import *
import random

init(autoreset=True)

################## печать экранной заставки и меню ############################ 
Art = text2art(" Casino Royal ","colossal")

print()
print(Style.BRIGHT + Fore.YELLOW + Art)
user_balance = float(input('ВНЕСИТЕ ПЕРВОНАЧАЛЬНЫЙ ДЕПОЗИТ, $ >>> '))

table_data = [
    ['№ ', 'Варианты ставок', 'Описание', 'Коэффициент 1 $ к ...'],
    ['1', 'Low-High', 'на числа от 1 до 18, от 19 до 36', 2],
    ['2', 'Red-Black', 'на поле конкретного цвета', 2],
    ['3', 'Even-Odd', 'на чет или нечет', 2],
    ['4', 'Dozens', 'на дюжины (1, 2, 3) от 1 до 12, 13-24, 25-36', 3],
    ['5', 'Columns', 'на столбцы 1: 1 4 7 ... 2: 2 5 8 ... 3: 3 6 9 ...', 3],
    ['6', 'Zero', 'на zero', 36],
    ['7', 'Straight', 'на любой номер', 36],
]
table = DoubleTable(table_data)
table.inner_row_border = True
table.justify_columns[3] = 'center'
print(table.table)

################## компьютерная логика ########################################
lucky_color_text = ''
result_game = 0

########## для статистики игровой #############################################
total_games = 0
win_games = []
lost_games = []

################## игоровое меню ##############################################
while user_balance > 0:
# генерация компьютерного шарика для рулетки казино ########################### 
	lucky_number = random.randint(1,37)
	lucky_color = random.randint(1,2)

	if lucky_number == 37:
		lucky_color_text = 'zero'
	elif lucky_color == 1:
		lucky_color_text = 'красный'
	elif lucky_color == 2:
		lucky_color_text = 'черный'

	print(f'''\nВведите номер ставки и значение через пробел, к примеру:
	1 L  (L на числа 1-18, H на числа 19-36)
	2 R  (red или black) 
	3 E  (odd или even) 
	4 2  (номер дюжины 1, 2, 3) 
	5 1  (номер столбца 1, 2, 3) 
	6 Z  (ставка на zero) 
	7 18 (номер любого числа от 1 до 36)''')

	user_commands = input('>>> ')

# распарсим пользовательский ввод на два элемента #############################
	user_commands = user_commands.split(' ')
	user_item_1 = int(user_commands[0].strip())
	user_item_2 = user_commands[1].strip()

	print(f'\nСумма Вашей ставки в $:')
	user_bet = float(input('>>> '))

# проверка достаточности на балансе денег при недостатке уведомление ##########
	if user_bet <= user_balance:
		user_balance = user_balance - user_bet

# проверка результата совпадения у игрока с рулеткой ##########################
# проверка больше меньше ######################################################
		if user_item_1 == 1:
			if (user_item_2 == 'L') and (lucky_number > 0 and lucky_number < 19): 
				result_game = user_bet * 2
				win_games.append(1)
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			elif (user_item_2 == 'H') and (lucky_number > 18 and lucky_number < 37):
				result_game = user_bet * 2
				win_games.append(1)
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			else:
				result_game = 0
				lost_games.append(1)
				print(Style.BRIGHT + Fore.RED + 'ИГРОК ПРОИГРАЛ ;-(')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
				print(f'Выигрышная комбинация: НОМЕР >>> {str(lucky_number)} ЦВЕТ >>> {lucky_color_text}')

## проверка красное черное ####################################################
		elif user_item_1 == 2:
			if (user_item_2 == 'R') and (lucky_color == 1):
				result_game = user_bet * 2
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			elif (user_item_2 == 'B') and (lucky_color == 2):
				result_game = user_bet * 2
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			else:
				result_game = 0
				print(Style.BRIGHT + Fore.RED + 'ИГРОК ПРОИГРАЛ ;-(')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
				print(f'Выигрышная комбинация: НОМЕР >>> {str(lucky_number)} ЦВЕТ >>> {lucky_color_text}')

## проверка на четное и нечетное ##############################################
		elif user_item_1 == 3:
			if (user_item_2 == 'E') and (lucky_number % 2 == 0):
				result_game = user_bet * 2
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			elif (user_item_2 == 'O') and (lucky_number % 2 != 0) and lucky_number != 37:
				result_game = user_bet * 2
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			else:
				result_game = 0
				print(Style.BRIGHT + Fore.RED + 'ИГРОК ПРОИГРАЛ ;-(')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
				print(f'Выигрышная комбинация: НОМЕР >>> {str(lucky_number)} ЦВЕТ >>> {lucky_color_text}')

# проверка на дюжины ##########################################################
		elif user_item_1 == 4:
			user_item_2 = int(user_item_2)
			if (user_item_2 == 1) and (0 < lucky_number < 13):
				result_game = user_bet * 3
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			elif (user_item_2 == 2) and (12 < lucky_number < 25):
				result_game = user_bet * 3
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			elif (user_item_2 == 3) and (24 < lucky_number < 37):
				result_game = user_bet * 3
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			else:
				result_game = 0
				print(Style.BRIGHT + Fore.RED + 'ИГРОК ПРОИГРАЛ ;-(')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
				print(f'Выигрышная комбинация: НОМЕР >>> {str(lucky_number)} ЦВЕТ >>> {lucky_color_text}')

# проверка на столбцы #########################################################
		elif user_item_1 == 5:
			user_item_2 = int(user_item_2)
			if (user_item_2 == 1) and (lucky_number in [1,4,7,10,13,16,19,22,25,28,31,34]):
				result_game = user_bet * 3
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			elif (user_item_2 == 2) and (lucky_number in [2,5,8,11,14,17,20,23,26,29,32,35]):
				result_game = user_bet * 3
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			elif (user_item_2 == 3) and (lucky_number in [3,6,9,12,15,18,21,24,27,30,33,36]):
				result_game = user_bet * 3
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			else:
				result_game = 0
				print(Style.BRIGHT + Fore.RED + 'ИГРОК ПРОИГРАЛ ;-(')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
				print(f'Выигрышная комбинация: НОМЕР >>> {str(lucky_number)} ЦВЕТ >>> {lucky_color_text}')

# проверка на ZERO ############################################################
		elif user_item_1 == 6:
			if (user_item_2 == 'Z') and lucky_number == 37:
				result_game = user_bet * 36
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			else:
				result_game = 0
				print(Style.BRIGHT + Fore.RED + 'ИГРОК ПРОИГРАЛ ;-(')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
				print(f'Выигрышная комбинация: НОМЕР >>> {str(lucky_number)} ЦВЕТ >>> {lucky_color_text}')

### проверка на стрит ставку, произвольное число ##############################
		elif user_item_1 == 7:
			user_item_2 = int(user_item_2)
			if (user_item_2 == lucky_number):
				result_game = user_bet * 36
				print(Style.BRIGHT + Fore.GREEN + 'ИГРОК ВЫЙГРАЛ :-) $$$ !')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
			else:
				result_game = 0
				print(Style.BRIGHT + Fore.RED + 'ИГРОК ПРОИГРАЛ ;-(')
				print('````````````````````````````````````````````````````````````````````````````````````````````````````')
				print(f'Выигрышная комбинация: НОМЕР >>> {str(lucky_number)} ЦВЕТ >>> {lucky_color_text}')

	else:
		print(f'\nУ Вас не достаточно денег на балансе ;-(')
		continue

# подсчет финансового результата после игры ###################################
	user_balance = user_balance + result_game
	total_games = total_games + 1
	win = len(win_games)
	lost = len(lost_games)
	
	print(f'ВАШ БАЛАНС {user_balance}\n')
	print('Игровая статистика: всего игр >>> {} 100 %, побед >>> {} {:.2%} поражений >>> {} {:.2%}'.format(total_games,win,(win/total_games),lost,(lost/total_games)))
	print('````````````````````````````````````````````````````````````````````````````````````````````````````')

# для контроля ################################################################
	# print(lucky_number)
	# print(lucky_color)
###############################################################################

else:
	print(Style.BRIGHT + Fore.YELLOW + 'ИГРА ОКОНЧЕНА !')
	print('````````````````````````````````````````````````````````````````````````````````````````````````````')

		


















