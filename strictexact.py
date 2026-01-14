import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

def Boltzmann(z):
	s=set()
	l=1./(1.-z)
	m=np.random.poisson(l)
	for i in range(m):
		n=np.random.geometric(1.-z)
		if np.random.rand()<(np.log(1.+pow(z,n)))/pow(z,n):
			s.add(n)
	return sorted(s,reverse=True)
	
def BoltzmannExact(n):
	z=np.exp(-1./pow(n*pow(12.,0.5)/np.pi,0.5))
	part = Boltzmann(z)
	while sum(part)!=n:
		part = Boltzmann(z)
	return part
	
def limitshape(x):
	c=pow(12.,0.5)/np.pi
	return c*np.log(1.+np.exp(-x/c))

n=10000
z=np.exp(-1./pow(n*pow(12.,0.5)/np.pi,0.5))
part=BoltzmannExact(n)
N=sum(part)
partscale=part/np.sqrt(N)
yscale=np.linspace(0,len(part)/np.sqrt(N),len(part))
x=np.arange(0,8.,0.1)
y=limitshape(x)
plt.plot(x,y, '--')
plt.step(partscale,yscale)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.1)) 
plt.show()

