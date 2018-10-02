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
		self.x += self.vx * dt
		self.y += self.vy * dt
		self.t += dt
	
	def orbitPlot(self,stepSize,time):
		xlist = [self.x]
		ylist = [self.y]
		
		while self.t <= time:
			self.doTimeStep(stepSize)
			xlist.append(self.x)
			ylist.append(self.y)
		
		plt.plot(xlist,ylist)
		plt.plot(0,0,'r*')
		plt.axis('equal')

	