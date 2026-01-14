import numpy as np
import timeit
import statistics

def Boltzmann(z):
	s=set()
	l=1./(1.-z)
	m=np.random.poisson(l)
	for i in range(m):
		n=np.random.geometric(1.-z)
		if np.random.rand()<(np.log(1.+pow(z,n)))/pow(z,n):
			s.add(n)
	return sorted(s,reverse=True)
	
def tune(n):
	return np.exp(-1./pow(n*pow(12.,0.5)/np.pi,0.5))

def benchmark(f, x, repetitions=1000):
	times = timeit.repeat(
	stmt=lambda: f(x),
	repeat=repetitions,
	number=1)
	return statistics.mean(times), statistics.stdev(times)	

n=pow(10,6)
z=tune(n)

mean, std = benchmark(Boltzmann, z)

print(f"Mean: {mean*1000:.6e} ms")
print(f"Std:  {std*1000:.6e} ms")

