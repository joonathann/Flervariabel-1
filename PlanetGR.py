# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:08:33 2018

@author: Harald Öhrn
"""

import matplotlib.pyplot as plt
import math 
import numpy as np

class PlanetGR:
	
	k = 4*math.pi**2
	
	def __init__(self,x,y,vx,vy,alpha2):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.t = 0
		self.alpha2 = alpha2
		
	def doTimeStep(self,dt):
		self.vx = self.vx + -self.k * self.x / ((self.x **2 + self.y **2)**1.5) * (1+(self.alpha2/(self.x **2 + self.y **2))) * dt #new vx using formula from 2.1
		self.vy = self.vy + -self.k * self.y / ((self.x **2 + self.y **2)**1.5) * (1+(self.alpha2/(self.x **2 + self.y **2))) * dt #corected for GR
		self.x += self.vx * dt #calculates the new coordinates
		self.y += self.vy * dt
		self.t += dt #total time elapsed
	
    # Returns distance in AU from the planet to the Sun.
	def getR(self):
		return math.sqrt(self.x**2 + self.y**2)
	
	# Returns the angle between the position of the planet and the positive
    # x-axis in the range [0, 2 pi)
	def getAngle(self):
			x = self.x
			y = self.y
			theta = math.atan2(y,x)
			if theta<0:
				theta += 2.*math.pi
			return theta

	def orbitPlot(self,stepSize,time,findPerihelion = False): #method to simplily ploting
		self.xlist = [self.x]
		self.ylist = [self.y]
		
		while self.t <= time: #time is the total time to simulate
			self.doTimeStep(stepSize) #stepSize is the doTimeStep dt
			if findPerihelion == True:
				if (self.x**2 + self.y**2) > (self.xlist[-1]**2 + self.ylist[-1]**2) and (self.xlist[-1]**2 + self.ylist[-1]**2) < (self.xlist[-2]**2 + self.ylist[-2]**2):
					plt.plot(self.xlist[-1], self.ylist[-1], 'rx')
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
#3.4
		# alpha^2 = 0
mercury1 = PlanetGR(0.47,0,0,8.2,0)
mercury1.orbitPlot(0.000001,2)

#%%
# alpha^2 = 10^-2
mercury2 = PlanetGR(0.47,0,0,8.2,1e-2)
mercury2.orbitPlot(0.000001,2)

#%%
# alpha^2 = 10^-3
mercury3 = PlanetGR(0.47,0,0,8.2,1e-3)
mercury3.orbitPlot(0.000001,2)

#%%
# alpha^2 = 10^-4
mercury4 = PlanetGR(0.47,0,0,8.2,1e-4)
mercury4.orbitPlot(0.000001,2)