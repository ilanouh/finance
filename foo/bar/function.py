#!~/.brew/bin/python
from math import sqrt

# Final_value et initial_value sont deux montant en euro
def	profit_and_loss(final_value, initial_value):
	return final_value - initial_value

# Profit et initial_value sont deux montant en euro
def performance(profit, initial_value):
	return profit / initial_value

# Performance est un pourcentage de plus/moin value observe sur une periode
def annual_performance(performance):
	return (1 + performance) * (1 / 252) - 1

# X_list est une liste contenant des montants en euro, nb est le nombre de montants
def average(x_list, nb):
	total = 0
	for i in x_list:
		total += i
	return total / nb

# N est le nombre de performance quotidiennes, xbar est une moyenne des performances quotidiennes et 
# x_list est une liste de donnee a traite
def sum_perso(n, xbar, x_list):
	ret = 0
	for i in xrange(1 , n):
		ret += (x_list[i] - xbar) * (x_list[i] - xbar)
	return ret

# N est le nombre de performance quotidiennes, x_list est une liste de donnee a traite et nb est le nombre de donnee a traiteė
def volatility(n, x_list, nb):
	start = sqrt(1/(n-1))
	sump = sum_perso(n, average(x_list, nb), x_list)
	return sqrt((1 / (n - 1)) * sump) * sqrt(252)

# create random walk which I want to calculate maximum drawdown for:
# T = 50
# mu = 0.05
# sigma = 0.2
# S0 = 20
# dt = 0.01
# N = round(T / dt)
# t = np.linspace(0, T, N)
# W = np.random.standard_normal(size = N) 
# W = np.cumsum(W) * np.sqrt(dt)		 ### standard brownian motion ###
# x_list = (mu - 0.5 * sigma ** 2) * t + sigma * W 
# S = S0 * np.exp(x_list) ### geometric brownian motion ###
# plt.plot(S)

# X_list est une liste de donnee a traite
def maximum_drawdawn(x_list):
	max_dd = 0
	peak = x_list[0]
	for x in x_list:
		if x > peak:
			peak = x
		dd = (peak - x) / peak
		if dd > max_dd:
			max_dd = dd
	return max_dd

# Perf est un pourcentage reel et bench est le pourcentage de la simulation
def tracking_error(perf, bench):
	return perf - bench


