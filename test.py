import graph2D
import vector

graph=graph2D.graph2D()
v=vector.functionPoints()
v.addZeros([0,1,5])
v.addOnes([6,1,10])
v.addPoints(3,[11,1,15])

graph._init_(v.getVector())
graph.draw()