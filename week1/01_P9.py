"""
import math
class processing:
	def __init__(self,weight,height):
		self.weight=weight
		self.height=height
	def Mosteller(self):
		return ((self.weight*self.height)**(1/2))/60
	def Haycock(self):
		return 0.024265*(self.weight**0.5378)*(self.height**0.3964)
	def Boyd(self):
		return 0.0333*(self.weight**(0.6157-0.0188*math.log10(self.weight)))*(self.height**0.3)
x1=float(input())
x2=float(input())
b1=processing(x1,x2)
print(processing.Mosteller(b1))
print(processing.Haycock(b1))
print(processing.Boyd(b1))
"""
#simple code below
import math

weight=float(input())
hight=float(input())
print(((weight*hight)**(1/2))/60)
print(0.024265*(weight**0.5378)*(hight**0.3964))
print(0.0333*(weight**(0.6157-0.0188*math.log10(weight)))*(hight**0.3))