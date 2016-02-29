from mudamath import funcPoints
#from scipy.signal import cos
import math
function=funcPoints([(-2,-2),(-1,-2),(0,1),(1,2),(2,3)])
print function.getPs()
print function.getInds()
print function.getVals()
print function.getDom()
print function.getRan()
print function.getYforX(0)
print function.getEven()
print function.getOdd()
print function.conv([(-2,-1),(-1,5),(0,3)],[(-1,1),(0,2),(1,3),(2,4)])
print function.fourier(List=[(0,1),(1,0),(2,1),(3,0),(4,1),(5,0),(6,1),(7,0),(8,1),(9,0),(10,1)],fs=1)
list1=[]
i=0
incr=0.01
while i<2:
    list1.append((i,math.cos(i*2*math.pi)))
    i=i+incr
function.draw(List=list1)

four=function.fourier(List=list1,fs=100)
function.draw(List=four)
ifour=function.idft(List=four,fs=100)
print ifour
function.draw(List=ifour)

#list=function.conv([(-2,-1),(-1,5),(0,3)],[(-1,1),(0,2),(1,3),(2,4)])
#function.draw(List=function.fourier(List=[(0,1),(1,2),(2,3),(3,2),(4,1),(5,0),(6,1),(7,2),(8,3),(9,2),(10,1)],fs=1))

#function.draw('even')
#function.draw('all')