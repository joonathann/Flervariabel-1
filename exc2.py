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
	
	def orbitPlot(self,stepSize,time, plot = True): #method to simplily ploting
		self.xlist = [self.x]
		self.ylist = [self.y]
		
		while self.t <= time: #time is the total time to simulate
			self.doTimeStep(stepSize) #stepSize is the doTimeStep dt
			self.xlist.append(self.x)
			self.ylist.append(self.y)
		
		if plot == True:
			plt.plot(self.xlist,self.ylist)
			plt.plot(0,0,'r*')
			plt.axis('equal')
			
		elif plot == False: 
			return xlist

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
		print((2*stepnr*dt)**2/SMA**3)   #Keplers Law
		