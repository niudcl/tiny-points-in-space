
from sys import argv
from array import array
from sympy import *
import sys

#---------------------COMMAND LINE ARGUMENT LIST-------------------------------
#argv(1) = minX
#argv(2) = maxX
#argv(3) = minY
#argv(4) = maxY
#argv(5) = resolution
#argv(6) = function
#------------------------------------------------------------------------------


#sympy requirements
x = symbols('x')               #create sympy symbols for expressions
y = symbols('y')
z = symbols('z') 


	
try:
	minX = float(argv[1]) 
except ValueError:
	resultList = open("temp.txt","w")
	resultList.write("Error in minX");
	resultList.close();
	sys.exit()
	
try:
	maxX = float(argv[2])
except ValueError:
	resultList = open("temp.txt","w")
	resultList.write("Error in maxX");
	resultList.close();
	sys.exit()
try:
	minY = float(argv[3])
except ValueError:
	resultList = open("temp.txt","w")
	resultList.write("Error in minY");
	resultList.close();
	sys.exit()
try:
	maxY = float(argv[4])
except ValueError:
	resultList = open("temp.txt","w")
	resultList.write("Error in maxY");
	resultList.close();
	sys.exit()	
try:
	resolution = int(argv[5])
except ValueError:
	resultList = open("temp.txt","w")
	resultList.write("Error in resolution");
	resultList.close();
	sys.exit()

try:
	expr = sympify(argv[6])        #convert argument function to usable sympy expr
except ValueError:
	resultList = open("temp.txt","w")
	resultList.write("Error in expression");
	resultList.close();
	sys.exit()


#find the actual ranges of the x and y axes
rangeX = maxX - minX
rangeY = maxY - minY
 
#find the increments of the x and y axes
incrementX = rangeX / (resolution - 1)  # (-1) because you're splitting the distance to 1 less
incrementY = rangeY / (resolution - 1)  # parts than the resolution (EX. 4 sections between 5 points)
 
#initialize array of X values
arrayX = array('d',[0] * resolution)      #empty array of size (resolution)
for i in range(0, resolution):
    arrayX[i] = minX + (i * incrementX)  #re-draw array with required points
     
#initialize array of Y values
arrayY = array('d',[0] * resolution)      #empty array of size (resolution)
for i in range(0, resolution):
    arrayY[i] = minY + (i * incrementY)   

resultList = open("temp.txt","w")

inter = integrate(expr,y)
for i in range(0,resolution):
		for j in range(0,resolution):
        
			#Printing results for purpose of debugging.
			#print "x: " + str(arrayX[i])
			#print "y: " + str(arrayY[j])
			#print "z: " + str(expr.subs([(x,arrayX[i]),(y,arrayY[j])]))
             
			#write the results to file (Format "x,y,z\n")
			resultList.write(str(arrayX[i]) + "," + str(arrayY[j]) + ',' + str(inter.subs([(x,arrayX[i]),(y,arrayY[j])])) + '\n')
	
	
	
#close file
resultList.close()  