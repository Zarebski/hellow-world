import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

def beta(N):
	"""beta as described on page 32 of "Mathematical Epidemiology"
	Args:
		N is the size of the population
	"""
	# # Michaelis-Menton
	# a,b = 0.01,1
	# result = a*N/(1. + b*N)

	# mass action
	# b = 0.01
	# result = b

	# standard incidence
	l = 0.01
	result = l
	return result

def f(y,t,beta,alpha,f=1):
	"""function required as the first arg of scipy.integrate.odeint()
	Args:
		y is an array for the state of the system
		t is the time 
		beta is a callable 
		alpha is a float parameter
		f is a float parameter 
	"""
	f1 = -beta(y[2])*y[0]*y[1]
	f2 = -f1 -alpha*y[1]
	f3 = -(1 - f)*alpha*y[1]
	return np.array([f1,f2,f3])

def main():
	alpha = 3
	Time = np.linspace(0,5,100) # the time mesh to return the solution on
	yInit = np.array([998.,2.,1000.])	# the initial condition
	Y = odeint(f,yInit,Time,args=(beta,alpha,0.9))	# command to solve the system
	# just a few lines of code to plot the solution
	plt.figure()
	plt.plot(Time,Y[:,0],label='Susceptables')
	plt.plot(Time,Y[:,1],label='Infectious')
	plt.plot(Time,Y[:,2]-Y[:,1]-Y[:,0],label='Recovered')
	plt.legend()
	plt.xlabel('Time')
	plt.ylabel('Number')
	plt.show()

	return None

if __name__ == '__main__':
	main()
