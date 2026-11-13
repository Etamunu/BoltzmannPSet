import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

def Boltzmann(z):
	s=set()
	l=z/(1.-z)
	m=np.random.poisson(l)
	for i in range(m):
		n=np.random.geometric(1.-z)
		t=pow(z,n)
		if np.random.rand()<(np.log1p(t)/t if t else 1.):
			s.add(n)
	return sorted(s,reverse=True)
	
def BoltzmannExact(n):
	z=np.exp(-np.pi/np.sqrt(12.*n))
	part = Boltzmann(z)
	while sum(part)!=n:
		part = Boltzmann(z)
	return part
	
def limitshape(x):
	c=pow(12.,0.5)/np.pi
	return c*np.log(1.+np.exp(-x/c))

n=10000
part=BoltzmannExact(n)
N=sum(part)
partscale=part/np.sqrt(N)
yscale = np.arange(1, len(part) + 1) / np.sqrt(N)
x=np.arange(0,8.,0.1)
y=limitshape(x)
plt.plot(x,y, '--')
plt.step(partscale, yscale, where="post")
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.1)) 
plt.show()

