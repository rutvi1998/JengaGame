import os
import time
import sys

class JengaGame:
	def __init__(self):
		self.__players = None
		self.__number_of_players = None
		self.__moves = None
		self.__who_moves_before = None
		self.__who_moves = None
		self.__who_moves_next = None
		self.__stop_words = ('stop', 'ыещз', 'стоп', 'cnjg')
		self.__game_over = False
	
	def start_game(self):
		message = 'Введите имена игроков через запятую: '
		players = [name for name in input(message).split() if name]
		players = map(str.strip, players)
		self.__players = list(players)
		self.__number_of_players = len(self.__players)
		self.clear_console()
		print('Участников: {}'.format(self.__number_of_players))
		print('Имена участников:')
		for _ in self.__players:
			print('\t', _, sep='')
		print('Если игрок сломает башню, введите "stop" во время его хода\n')
		self.__moves = 0
		self.__who_moves_before = -2
		self.__who_moves = -1
		self.__who_moves_next = 0
		while not self.__game_over:
			self.__do_move()
		self.__show_results()

	def clear_console(self):
		platform = sys.platform
		if platform == 'win32':
			os.system('cls')
		else:
			os.system('clear')

	def __do_move(self):
		self.__moves += 1
		self.__choose_player()
		move_number = self.__moves
		who_moves = self.__players[self.__who_moves]
		who_moves_next = self.__players[self.__who_moves_next]
		message = ('Ход №{}. Ходит {}. {} готовится - '
				   .format(move_number, who_moves, who_moves_next))
		print(message, end='')
		if input().lower() in self.__stop_words:
			self.__finish_game()
	
	def __choose_player(self):
		self.__who_moves_before = self.__who_moves
		self.__who_moves = self.__who_moves_next
		if self.__who_moves_next == self.__number_of_players - 1:
			self.__who_moves_next = 0
		else:
			self.__who_moves_next += 1	

	def __finish_game(self):
		self.__game_over = True
		self.clear_console()

	def __show_results(self):
		message = 'Игра окончена. Ходов сделано: {}. '.format(self.__moves)
		print(message, sep='', end='')
		if self.__moves == 1:
			player = self.__players[self.__who_moves]
			print('\n{}, ну ты и рукожоп!!!'.format(player))
			return
		elif self.__moves < 20:
			print('Да вы просто раки!!!')
		elif self.__moves < 30:
			print('Что-то не очень (:')
		elif self.__moves < 40:
			print('Хорошая игра!')
		else:
			print('Потрясающе!!!')

		winner = self.__players[self.__who_moves_before]
		loser = self.__players[self.__who_moves]
		print('Победитель: {}'.format(winner))
		print('Проигравший: {}'.format(loser))



Jenga = JengaGame()

Jenga.start_game()
input()