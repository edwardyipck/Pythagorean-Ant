from math import *
from random import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time


def read_data(file_name):
    start = time.time() # Starts the timer
    list = [100,1000,10000,100000,1000000] #The different values of N
    for i in list:
        N=i
        global x1 #This is the probability value for each ant
        global L  #L is used to store the greatest probability
        global S  #S is used to store the lowest probability
        x1, L, S = 0, -1, 1
        global X  #X is used to store a list of all probabilities
        X=[]
        infile = open(file_name,'r')
        for line in infile:
            A, B, C = 0. ,0. ,0.  #The counter for each side starts at 0 for each triangle
            lloc=[]
            strlist=line.split()
            for i in range(len(strlist)):
                lloc.append(float(strlist[i])) # For each line in the data, a list is made storing the side lengths
            a=lloc[0] # The sides of each triangle is read off the position in the list
            b=lloc[1]
            c=lloc[2]
            for i in range (1,N+1):
                x=a*random() # A random x position is chosen
                y=b*random() # A random y position is chosen
                while (((-b*x)/a)+b)<y: # If the position chosen is outside of the triangle, another position is chosen
                    x=a*random()
                    y=b*random()
                theta = 2*pi*random() # A random diection is chosen
                dire = atan(y/x) # This is the angle between the origin of the triangle to the position of the ant
                alpha = atan(x/(b-y)) # This is the angle between the ant and a corner of the triangle
                beta = atan(y/(a-x))  # This is the angle between the ant and a corner of the triangle
                if ((2*pi)-beta)<theta<2*pi or 0<theta<(alpha+(0.5*pi)): # The value of theta can be between 3 ranges, the count for each side increases depending on the angle
                    C=C+1
                if (pi+dire)<theta<((2*pi)-beta):
                    A=A+1
                if ((0.5*pi)+alpha)<theta<(pi+dire):
                    B=B+1
            x1=C/N
            X.append(x1)
            if x1>L: # The probaility is compared to the largest probability, if greater then the list and the probability is stored
                L = x1
                global Lmat # This is used to store the list of side lengths 
                Lmat = lloc
            if x1<S: # The probaility is compared to the lowest probability, if smaller then the list and the probability is stored
                S = x1
                global Smat # This is used to store the list of side lengths 
                Smat = lloc
        print( '''N : %i
        Max Probability: %f from %s
        Min Probability: %f from %s
        ''' % (N,L,Lmat,S,Smat))
        if N==1000000:
            print('''The maximum probability is %f from the %s triangle 
                     The minimum probability is %f from the %s triangle
                     The approximate value for the [3,4,5] triangle is %f
                     Given value is 0.3916721504
                     Margin of error is %f''' % (L,Lmat,S,Smat,X[0],0.3916721504-X[0]))
            plt.hist(X, 5, facecolor='green',edgecolor='black', linewidth=1.2) # Plots the Histrogram
            plt.xlabel('Probabilities')
            plt.ylabel('Number of Triangles')
            plt.title('Histogram of exit probabilities')
            plt.axis([0.36, 0.48, 0, 30])
            plt.grid(True)
            plt.show()
    infile.close()
            
    end = time.time()
    print('Time taken is %f seconds' %(end - start))

if __name__ == '__main__':
     read_data('triangle_triples.data')
    
