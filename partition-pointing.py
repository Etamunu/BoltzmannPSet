import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

def row(n,r,h,ax):
	for k in range(n):
		if k>r:
			ax.add_patch(Rectangle((k,h),1,1,edgecolor='blue',facecolor='white'))
	for k in range(n):
		if k<=r:
			ax.add_patch(Rectangle((k,h),1,1,edgecolor='red',facecolor='white'))

def diagram(s,ax):
	for i in range(len(s)):
		row(s[i,0],s[i,1],i,ax)
	ax.relim()
	ax.autoscale_view()
	ax.set_aspect('equal')

def boltzmann(z,plotmode):
	fig,ax=plt.subplots()
	s=set()
	N=0
	l=z/(1.-z)**2.
	m=np.random.poisson(l)
	for i in range(m):
		n=np.random.geometric(1.-z)+np.random.geometric(1.-z)+1
		if np.random.rand()<(np.log(1.+pow(z,n)))/pow(z,n):
			s.add((n,np.random.randint(0,n)))
			N=N+n
	s=sorted(s,key=lambda x:x[1],reverse=True)
	s=sorted(s,key=lambda x:x[0],reverse=True)
	s=np.array(list(s))
	print('N=',N)
	print('M=', len(s))
	print('Max=', s[0,0])
	print('M/Max=', len(s)/s[0,0])
	if plotmode:
		diagram(s,ax)
	else:
		plt.plot(s[:,0],range(0,len(s)))

	plt.show()
	return(s)

s=boltzmann(0.9,1)
