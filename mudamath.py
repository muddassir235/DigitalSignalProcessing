import numpy as np
import pygame
from math import pi
from pygame.locals import *
import math
import cmath
from scipy.signal import freqz
from scipy.fftpack import rfft,irfft,fftfreq,ifftn,dct


class funcPoints:

    points=[]
    indices=[]
    values=[]

    #works
    def __init__(self,points):
        for point in points:
            self.points.append(point)
            self.indices.append(point[0])
            self.values.append(point[1])

    #works
    def append(self,points,List=None):
        if type(List) is list:
            if(type(points) is list):
                for point in points:
                    if(point[0] in self.getInds(List=List) ):
                        print "a value already exists at "+str(point[0])
                    else:
                        List.append(point)
            else:
                if(points[0] in self.getInds(List=List)):
                    print "a value already exists at"+str(points[0])
                else:
                    List.append(points)
        else:
            if(type(points) is list):
                for point in points:
                    if(point[0] in self.indices ):
                        print "a value already exists at "+str(point[0])
                    else:
                        self.points.append(point)
                        self.indices.append(point[0])
                        self.values.append(point[1])

            else:
                if(points[0] in self.indices):
                    print "a value already exists at"+str(points[0])
                else:
                    self.points.append(points)
                    self.indices.append(points[0])
                    self.values.append(points[1])

    #works
    def getDom(self,List=None):
        minimumIndex=0
        maximumIndex=0
        if type(List) is list:
            minimumIndex=min(float(s) for s in self.getInds(List=List))
            maximumIndex=max(float(s) for s in self.getInds(List=List))
        else:
            minimumIndex=min(float(s) for s in self.indices)
            maximumIndex=max(float(s) for s in self.indices)
        return [minimumIndex,maximumIndex]

    #works
    def getRan(self,List=None):
        minimumIndex=0
        maximumIndex=0
        if type(List) is list:
            minimumIndex=min(float(s) for s in self.getVals(List=List))
            maximumIndex=max(float(s) for s in self.getVals(List=List))
        else:
            minimumIndex=min(float(s) for s in self.values)
            maximumIndex=max(float(s) for s in self.values)
        return [minimumIndex,maximumIndex]

    #works
    def getPs(self):
        return self.points

    #works
    def getInds(self,List=None):
        if type(List) is list:
            indices=[item[0] for item in List]
            return indices
        else:
            return self.indices

    #works
    def getVals(self,List=None):
        if type(List) is list:
            values=[item[1] for item in List]
            return values
        else:
            return self.values

    #works
    def addPs(self,magnitude,range):
        i=range[0]
        if(range[0]<range[2] and range[1]>0):
            while i<=range[2]:
                if i in self.indices:
                    print "a value already exists at "+str(i)
                else:
                    self.indices.append(i)
                    self.values.append(magnitude)
                    self.points.append((i,magnitude))
                i=i+range[1]
        elif (range[2]<range[0] and range[1]<0):
            while i>=range[2]:
                if i in self.indices:
                    print "a value already exists at "+str(i)
                else:
                    self.indices.append(i)
                    self.values.append(magnitude)
                    self.points.append((i,magnitude))
                i=i+range[1]
        elif (range[1]==0):
            print "Step Size Must be None-Zero!"

        elif (range[1]<0):
            print "End point must be less that Start for Negative steps"

        else:
            print "End point must be greater than Start for Positive steps"

    #works
    def zeros(self,range):
        self.addPs(0,range)

    #works
    def ones(self,range):
        self.addPs(1,range)

    def update_in_alist(self,alist, key, value):
        return [(k,v) if (k != key) else (key, value) for (k, v) in alist]

    def insertInList(self,alist, key, value):
        alist[:] = self.update_in_alist(alist, key, value)

    def insert(self,key, value):
        self.points[:] = self.update_in_alist(self.points, key, value)

    #works
    def getYforX(self,x,List=None):
        if type(List) is list:
            Ys = [point[1] for point in List if point[0] == x]
            return Ys
        else:
            Ys = [point[1] for point in self.points if point[0] == x]
            return Ys

    #works
    def getEven(self):
        even=[]
        for indice in self.indices:
            if(indice!=float(0)):
                if(indice):
                    if -indice in self.indices:
                        print "contains works"
                        even.append((indice,float(self.getYforX(indice)[0]+self.getYforX(-indice)[0])/float(2)))
                    else:
                        print str(-indice)+" is not a valid index"
                        even.append((indice,float(self.getYforX(indice)[0])/float(2)))
                        even.append((-indice,float(self.getYforX(indice)[0])/float(2)))
            else:
                even.append((0,float(self.getYforX(0)[0])))

        return even

    #works
    def getOdd(self):
        odd=[]
        for indice in self.indices:
             if(indice):
                 if -indice in self.indices:
                     print "contains works"
                     odd.append((indice,float(self.getYforX(indice)[0]-self.getYforX(-indice)[0])/float(2)))
                 else:
                     odd.append((indice,float(self.getYforX(indice)[0])/float(2)))
                     odd.append((-indice,-float(self.getYforX(indice)[0])/float(2)))

        return odd

    #works
    def draw(self,what=None,List=None):

        fontFile="C:\Windows\Fonts\Arial.ttf"
        pointsToDraw=[]
        pointToPixelCoordinates={(0,0,0,0)}
        BLACK = (  0,   0,   0)
        WHITE = (255, 255, 255)
        BLUE =  (39,141,207)
        GREEN = (102, 255, 102)
        RED =   (255, 115, 115)

         #given points in the x axis
        xStart=None
        xMid=None
        xEnd=None
        xOrigin=0

        #points on the screen in the x axis
        xStartPixel=None
        xOriginPixel=None
        xEndPixel=None

        #how may points does a pixel contain in the x direction
        xPixeltoPointFactor=0.00000000000

        #given points in the y direction
        yStart=None
        yMid=None
        yEnd=None
        yOrigin=0

        #points on the screen in the y direction
        yStartPixel=None
        yOriginPixel=None
        yEndPixel=None

        #how many points does a pixel contain in the y direction
        yPixelToPointFactor=0.00000000000

        # Set the height and width of the screen
        size = [1000, 562]
        screen = pygame.display.set_mode(size)

        #Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()






        domain=None
        range=None
        if type(List) is list:
            print "trying to draw list"
            pointsToDraw=List
        else:
            if what is 'all':
                pointsToDraw=self.points
            elif what is 'even':
                pointsToDraw=self.getEven()
            elif what is 'odd':
                pointsToDraw=self.getOdd()
            else:
                pointsToDraw=self.points

        domain=self.getDom(List=pointsToDraw)
        range=self.getRan(List=pointsToDraw)
        xStart=domain[0]
        xEnd=domain[1]
        yStart=range[0]
        yEnd=range[1]

        if(xStart!=xEnd):
            xStartPixel=size[0]/20
            xEndPixel=size[0]-size[0]/20
            if (xStart>=0):
                xPixeltoPointFactor=(float(xEnd-xStart)/float(xEndPixel-xStartPixel))/(float(xEnd-xStart)/float(xEnd))
                xOriginPixel=xStartPixel
            else:
                xPixeltoPointFactor=float(xEnd-xStart)/float(xEndPixel-xStartPixel)
                xOriginPixel=xStartPixel+ int(float(0-xStart) / float(xPixeltoPointFactor))
        else:
            xStartPixel=size[0]/20
            xOriginPixel=xStartPixel
            xEndPixel=size[0]-size[0]/20
            if(xStart!=0):
                xPixeltoPointFactor=float(xEnd)/float(xEndPixel-xStartPixel)
            else:
                xPixeltoPointFactor=float(1)/float(xEndPixel-xStartPixel)

        if(yStart!=yEnd):
            yStartPixel=size[1]-xStartPixel
            yEndPixel=xStartPixel
            if(yStart>=0):
                yPixeltoPointFactor=float(yEnd-float(yStart))/float(-yEndPixel+yStartPixel)/(float(yEnd-yStart)/float(yEnd))
                yOriginPixel=yStartPixel
            else:
                yPixeltoPointFactor=float(yEnd-float(yStart))/float(-yEndPixel+yStartPixel)
                yOriginPixel=yStartPixel-int(float(0-yStart)/float(yPixeltoPointFactor))
        else:
            yStartPixel=size[1]-xStartPixel
            yOriginPixel=size[1]-xStartPixel
            yEndPixel=xStartPixel
            if yStart!=0:
                yPixeltoPointFactor=float(yStart)/float(yStartPixel-yEndPixel)
            else:
                yPixeltoPointFactor=float(1)/float(yStartPixel-yEndPixel)
        for point in pointsToDraw:
            xPixelCoordinate=xOriginPixel+int(float(point[0])/float(xPixeltoPointFactor))
            yPixelCoordinate=yOriginPixel-int(float(point[1])/float(yPixeltoPointFactor))
            pointToPixelCoordinates.add((xPixelCoordinate,yPixelCoordinate,point[0],point[1]))

        while not done:
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(10)

            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop

            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.

            # Clear the screen and set the screen background
            screen.fill(WHITE)

             # Draw on the screen a GREEN line from (0,0) to (50.75)
            pygame.init()
             # 5 pixels wide.
            pygame.draw.aaline(screen, BLACK, [xStartPixel, yOriginPixel],[xEndPixel, yOriginPixel], True)
            pygame.draw.aaline(screen, BLACK, [xOriginPixel,yStartPixel ],[xOriginPixel,yEndPixel], True)
            for pointToPixelCoordinate in pointToPixelCoordinates:
            #     xPixelCoordinate=self.xOriginPixel+int(float(point[0])*float(self.xPixeltoPointFactor))
            #     print xPixelCoordinate
            #     yPixelCoordinate=self.yOriginPixel+int(float(point[1])*float(self.yPixeltoPointFactor))
            #     print yPixelCoordinate
                  pygame.draw.aaline(screen,BLACK,[pointToPixelCoordinate[0],yOriginPixel],[pointToPixelCoordinate[0],pointToPixelCoordinate[1]],True)
                  # Draw a circle
                  pygame.draw.circle(screen, BLUE, [pointToPixelCoordinate[0], pointToPixelCoordinate[1]], 1)
                  # font=pygame.font.SysFont(self.fontFile,20)
                  # text= font.render("("+str(pointToPixelCoordinate[2])+", "+str(pointToPixelCoordinate[3])+")",True,self.RED)
                  # textXPos=pointToPixelCoordinate[0]-text.get_width()/2
                  # textYPos=10
                  # if(pointToPixelCoordinate[3]>=0):
                  #     textYPos=pointToPixelCoordinate[1]-text.get_height()-10
                  # else:
                  #     textYPos=pointToPixelCoordinate[1]+text.get_height()
                  # self.screen.blit(text,(textXPos,textYPos))
            # # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
        # Be IDLE friendly
        pygame.quit()

    def width(self,List=None):
        domain=None
        if type(List) is list:
            domain=self.getDom(List=List)
        else:
            domain=self.getDom()
        width=domain[1]-domain[0]+1
        return width

    def conv(self,x,h):
        width_h = self.width(List=h)
        width_x = self.width(List=x)

        if width_h < width_x:
            "x is greater in length"
        else:
            h, x = x, h
            width_h, width_x = width_x, width_h

        indices_x=self.getInds(List=x)
        indices_h=self.getInds(List=h)
        domain_h = [int(self.getDom(List=h)[0]),int(self.getDom(List=h)[1])]
        domain_x = [int(self.getDom(List=x)[0]),int(self.getDom(List=x)[1])]
        domain = [int(domain_x[0]+domain_h[0]),int(domain_x[0]+domain_h[0]+(width_x+width_h-2))]

        self.append([(i,0) for i in range(domain_h[0],domain_h[1]+1,1) if not i in indices_h],List=h)
        self.append([(i,0) for i in range(domain_x[0],domain_x[1]+1,1) if not i in indices_x],List=x)
        conv=[(i,0) for i in range(domain[0],domain[1]+1,1)]

        print x
        print h

        increment=0
        for i in range(domain_h[0],domain_h[1]+1,1):
            start=domain[0]+increment
            end=start+width_x
            indexx=domain_x[0]
            for n in range(int(start),int(end),1):
                self.insertInList(conv,n,self.getYforX(n,List=conv)[0]+self.getYforX(i,List=h)[0]*self.getYforX(indexx,List=x)[0])
                indexx=indexx+1
            increment=increment+1
        return conv

    def fourier(self,List=None,fs=1):
        if type(List) is list:
            indices=self.getInds(List=List)
            if 0 not in indices:
                List.append((0,0))
            domain=[int(self.getDom(List=List)[0]),int(self.getDom(List=List)[1])]

            for i in range(domain[0],domain[1]+1,1):
                if i not in  indices:
                    List.append((i,0))

            indices=self.getInds(List=List)
            values=self.getVals(List=List)
            f_indices,f_values=freqz(values,indices,worN=2000)
            f_indices=f_indices*(fs * 0.5 / np.pi)
            f_List=[]
            f_indices=list(f_indices)
            values_copy=f_values.copy()
            values_copy=list(values_copy)
            f_values=list(f_values)
            i=0
            for value in f_values:
                f_List.append((f_indices[i],float(np.real(f_values[i]))))
                i=i+1
            return f_List
        else:
            List=self.points
            indices=self.getInds(List=List)
            if 0 not in indices:
                List.append((0,0))
            domain=[int(self.getDom(List=List)[0]),int(self.getDom(List=List)[1])]
            for i in range(domain[0],domain[1]+1,1):
                if i not in  indices:
                    List.append((i,0))

            indices=self.getInds(List=List)
            values=self.getVals(List=List)
            f_indices,f_values=freqz(values,indices,worN=2000)
            f_indices=f_indices*(fs * 0.5 / np.pi)
            f_List=[]
            f_indices=list(f_indices)
            values_copy=f_values.copy()
            values_copy=list(values_copy)
            f_values=list(f_values)
            i=0
            for value in f_values:
                f_List.append((f_indices[i],float(np.real(f_values[i]))))
                i=i+1
            return f_List

    def ifourier(self,List=None,fs=1):
        if type(List) is list:
            pass
        else:
            List=self.points

        indices=self.getInds(List=List)
        domain=[int(self.getDom(List=List)[0]),int(self.getDom(List=List)[1])]
        values=self.getVals(List=List)
        for i in range(domain[0],domain[1]+1,1):
                if i not in  indices:
                    List.append((i,0))
        indices=self.getInds(List=List)
        values=self.getVals(List=List)
        t_values=(values)
        i=float(0)
        t_List=[]
        for value in t_values:
            t_List.append((i,value))
            i=i+(float(1)/float(fs))
        return t_List

    def idft(self,List=None,fs=1):
        t=self.getVals(List=List)
        x = []
        N = len(t)
        for n in range(N):
            a = 0
            for k in range(N):
              a += t[k]*cmath.cos(2*cmath.pi*k*n*(1/N))
            a /= N
            print "a: "+str(a)
            x.append(a)
        i=float(0)
        print fs
        t_List=[]
        print x
        for value in x:
            t_List.append((i,float(np.real(value))))
            i=i+float(float(1)/float(fs))
        return t_List



'''
    import cmath
    # Discrete fourier transform
    def dft(x):
        t = []
        N = len(x)
        for k in range(N):
            a = 0
            for n in range(N):
                a += x[n]*cmath.exp(-2j*cmath.pi*k*n*(1/N))
            t.append(a)
        return t
    # Inverse discrete fourier transform
    def idft(t):
        x = []
        N = len(t)
        for n in range(N):
            a = 0
            for k in range(N):
                a += t[k]*cmath.exp(2j*cmath.pi*k*n*(1/N))
            a /= N
            x.append(a)
        return x
'''

