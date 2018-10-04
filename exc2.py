import matplotlib.pyplot as plt
import math 
import numpy as np

class Planet:
	
	k = 4*math.pi**2
	
	def __init__(self,x,y,vx,vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.t = 0
	
	def doTimeStep(self,dt):
		self.vx = self.vx + -self.k * self.x / ((self.x **2 + self.y **2)**1.5) * dt #new vx using formula from 2.1
		self.vy = self.vy + -self.k * self.y / ((self.x **2 + self.y **2)**1.5) * dt #new vy
		self.x += self.vx * dt #calculates the new coordinates
		self.y += self.vy * dt
		self.t += dt #total time elapsed
	
	def orbitPlot(self,stepSize,time): #method to simplily ploting
		self.xlist = [self.x]
		self.ylist = [self.y]
		
		while self.t <= time: #time is the total time to simulate
			self.doTimeStep(stepSize) #stepSize is the doTimeStep dt
			self.xlist.append(self.x)
			self.ylist.append(self.y)
		
		#ploting and formatin
		plt.plot(self.xlist,self.ylist)
		plt.plot(0,0,'r*')
		plt.axis('equal')
		plt.legend()
		self.getPeriodAndAxis(stepSize) #Calculates and prints SMA and period for every orbit.
		
	def getPeriodAndAxis(self,dt):
		SMA = (abs(min(self.xlist)) + abs(max(self.xlist)))/2  #Semi Major Axis
		stepnr = 0  #stepcounter starting value
		
		for n in self.ylist:
			stepnr += 1  # stepcounter
			if n < 0:
				break     # When the planet has reached the opposite side of the star, wrt starting positions, break the loop
				
		print('Period is ')
		print(2*stepnr*dt)  #double stepnumber times stepsize is the period
		print('SMA is ')
		print(SMA)
		print('T^2/a^3=')
		print((2*stepnr*dt)**2/SMA**3)   #Numerical aroximation of Keplers third Law
#%%
		
print("Diffrent orbits starting at the same point but with different initial velocity (in the y direction)")
ex1 = Planet(5000,0,0,0.03)
ex1.orbitPlot(2,500000)

ex2 = Planet(5000,0,0,0.075)
ex2.orbitPlot(2,500000)

ex3 = Planet(5000,0,0,0.1)
ex3.orbitPlot(2,700000)

ex4 = Planet(5000,0,0,0.11)
ex4.orbitPlot(2,1200000)
#%%
print("Same orbits but change in dt")
print("dt = 1")
ex1 = Planet(5000,0,0,0.075)
ex1.orbitPlot(1,500000)

print("dt = 100")
ex2 = Planet(5000,0,0,0.075)
ex2.orbitPlot(100,500000)

print("dt = 10000")
ex3 = Planet(5000,0,0,0.075)
ex3.orbitPlot(10000,1500000)

print("dt = 50000")
ex4 = Planet(5000,0,0,0.075)
ex4.orbitPlot(50000,700000)