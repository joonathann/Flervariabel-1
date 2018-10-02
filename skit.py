#%matplotlib inline
import matplotlib.pyplot as plt
import math 
import numpy as np

class Planet:
	    
   k=4*math.pi**2
    
   def __init__(self,x,y,vx,vy):
	   self.x = x
	   self.y = y
	   self.vx = vx
	   self.vy = vy
	   self.t = 0
                
	def doTimeStep(self,dt):
		self.vx = self.vx + -k * self.x / ((self.x **2 + self.y **2)**1.5) * dt #new vx using formula from 2.1
		self.vy = self.vy + -k * self.y / ((self.x **2 + self.y **2)**1.5) * dt #new vy
		self.x = self.x + self.vx * dt
		self.y = self.y + self.vy * dt
		self.t += dt #Endast plotfunktion
		# Complete in exercise 2.2
        
	def getPeriodAndAxis(self,dt):
		# COmplete in exercise 2.4
		
	def orbitPlot(self,stepSize,time):
		xlist = [self.x]
		ylist = [self.y]
		
		while self.t =< time:
			self.doTimeStep(stepSize)
			xlist.append(self.x)
			ylist.append(self.y)
			
		plt.plot(xlist,ylist)
			
			
