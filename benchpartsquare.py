import math
from scipy.special import gamma
from scipy.stats import gamma as gammadist
import numpy as np
import timeit
import statistics

def perfect_square(n):
	if n < 0:
		return False
	r = math.isqrt(n)
	return r*r == n

def Boltzmann(z1,z2):
	s=set()
	l=z2/(1.-z1)
	m=np.random.poisson(l)
	for i in range(m):
		n=np.random.geometric(1.-z1)
		if perfect_square(n)  and np.random.rand()<(np.log(1.+z2*pow(z1,n)))/(z2*pow(z1,n)):
			s.add(n)
	return sorted(s,reverse=True)
	
def calibration(m,n,q=2):
	kappa = pow(m,q+1.)/n
	return np.exp(-m/(q*n)) , pow(kappa,1./q)/(pow(q,1./q)*gamma(1.+1./q))

def benchmark(f, x,y, repetitions=1000):
	times = timeit.repeat(
	stmt=lambda: f(x,y),
	repeat=repetitions,
	number=1)
	return statistics.mean(times), statistics.stdev(times)

n=pow(10,6)
m=20
z1 , z2 = calibration(m,n)
mean, std = benchmark(Boltzmann, z1,z2)

print(f"Mean: {mean*1000:.6e} ms")
print(f"Std:  {std*1000:.6e} ms")

