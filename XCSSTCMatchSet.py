import random
from XCSSTCConfig import *
from XCSSTCEnvironment import *
from XCSSTCClassifier import *
from XCSSTCClassifierSet import *

class XCSSTCMatchSet(XCSSTCClassifierSet):
	def __init__(self, pop, env, actual_time):
		XCSSTCClassifierSet.__init__(self, env, actual_time)
		self.pop = pop
		for cl in self.pop.cls:
			if self.does_match(cl):
				self.cls.append(cl)
		
		while self.num_of_different_actions() < conf.theta_mna:
			cond = {}
			clm = XCSSTCClassifier(cond, actual_time)
			for i in range(len(self.env.state)):
				if random.random() >= conf.p_sharp:
					cond[i] = self.env.state[i]
			clm.condition = cond
			clm.action = self.random_action()
			clm.experience = 0
			clm.time_stamp = actual_time
			clm.action_set_size = self.numerosity_sum() + 1
			clm.numerosity = 1
			self.pop.cls.append(clm)
			self.cls.append(clm)
			while self.pop.numerosity_sum() > conf.N:
				cl_del = pop.delete_from_population()
				if cl_del in self.cls:
					self.cls.remove(cl_del)

	def does_match(self, cl):
		for key in cl.condition.keys():
			if cl.condition[key] != self.env.state[key]:
				return False
		return True

	def num_of_different_actions(self):
		a_list = []
		for cl in self.cls:
			a_list.append(cl.action)
		return len(set(a_list))

	def random_action(self):
		if len(self.cls) == 0:
			return random.randrange(2)
		else:
			if self.cls[0].action == 1:
				return 0
			else:
				return 1


if __name__ == '__main__':
	env = XCSSTCEnvironment()
	env.set_state()
	x = XCSSTCClassifierSet(env, 1)
	y = XCSSTCMatchSet(x, env, 1)
	print(env.state)
	for cl in y.cls:
		print(cl.condition) 
