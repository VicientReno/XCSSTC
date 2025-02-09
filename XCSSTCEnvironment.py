import math
import random
import sys

from XCSSTCConfig import *

class XCSSTCEnvironment:
	def __init__(self):
		self.__k = conf.k
		self.__length = int(self.__k + math.pow(2, self.__k))
		self.effect_sum = 0

	def set_state(self):
		self.__state = []
		for i in range(self.__length):
			if random.randrange(2) == 0:
				self.__state.append(0)
			else:
				self.__state.append(1)
		addbit = self.__state[0:conf.k]
		refbit = self.__state[conf.k:]
		cal = ""
		for x in range(len(addbit)):
			cal += str(addbit[x])
		# int(x, base=10) -> integer
		#convert a number or string to an integer
		ans = int(cal, 2)
		self._ans = refbit[ans]

	def is_true(self, ans):
		if self._ans == ans:
			return True
		else:
			return False

	def get_state(self):
		return self.__state
	state = property(get_state)
