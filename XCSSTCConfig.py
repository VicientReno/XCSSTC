class XCSSTCConfig:
	k = 2
	N = 600
	max_iterations = 3000
	max_experiments = 10
	MUX = True

	alpha = 0.1
	beta = 0.2
	gamma = 0.71
	delta = 0.1
	myu = 0.04
	nyu = 5
	chi = 0.8

	epsilon_0 = 10

	theta_ga = 25
	theta_del = 20
	theta_sub = 20
	theta_mna = 2

	p_sharp = 0.33
	p_explr = 1.0

	doGASubsumption = True
	doActionSetSubsumption = True

XCSSTCConfig = XCSSTCConfig()
conf = XCSSTCConfig