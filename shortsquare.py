import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import math
from scipy.special import gamma
from scipy.stats import gamma as gammadist

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
	
def BoltzmannExact(n):
	z=np.exp(-1./pow(n*pow(12.,0.5)/np.pi,0.5))
	part = Boltzmann(z)
	while sum(part)!=n:
		part = Boltzmann(z)
		print(sum(part))
	return part
	
def calibration(m,n,q=2):
	kappa = pow(m,q+1.)/n
	return np.exp(-m/(q*n)) , pow(kappa,1./q)/(pow(q,1./q)*gamma(1.+1./q))
	
def scaling(m,n,q=2):
	return q*n/m , m
	
def limitshape(x,q=2):
	return 1.-gammadist.cdf(x,a=1/q,scale=1)

m=100
n=pow(10.,12.)
z1 , z2 = calibration(m,n)
A, B = scaling(m,n)
part=Boltzmann(z1,z2)
N=sum(part)
partscale=np.array(part)/A
y=np.linspace(0,len(part)/B,len(part))
xlim=np.arange(0,3.,0.1)
ylim=limitshape(xlim)
plt.plot(xlim,ylim, '--')
plt.step(partscale,y)
plt.show()
