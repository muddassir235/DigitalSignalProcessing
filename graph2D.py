import pygame
from math import pi
import vector
from pygame.locals import *

class graph2D:
    fontFile="C:\Windows\Fonts\Arial.ttf"
    vectors=None
    points=None
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


    def _init_(self,vectors):
        self.vectors=vectors
        self.points=self.vectors.getVector()
        domain=self.vectors.getDomain()
        self.xStart=domain[0]
        self.xMid=domain[1]
        self.xEnd=domain[2]


        if(self.xStart!=self.xEnd):
            self.xStartPixel=self.size[0]/20
            self.xEndPixel=self.size[0]-self.size[0]/20
            if (self.xStart>=0):
                self.xPixeltoPointFactor=(float(self.xEnd-self.xStart)/float(self.xEndPixel-self.xStartPixel))/(float(self.xEnd-self.xStart)/float(self.xEnd))
                self.xOriginPixel=self.xStartPixel
            else:
                self.xPixeltoPointFactor=float(self.xEnd-self.xStart)/float(self.xEndPixel-self.xStartPixel)
                self.xOriginPixel=self.xStartPixel+ int(float(0-self.xStart) / float(self.xPixeltoPointFactor))
        else:
            self.xStartPixel=self.size[0]/20
            self.xOriginPixel=self.xStartPixel
            self.xEndPixel=self.size[0]-self.size[0]/20
            if(self.xStart!=0):
                self.xPixeltoPointFactor=float(self.xEnd)/float(self.xEndPixel-self.xStartPixel)
            else:
                self.xPixeltoPointFactor=float(1)/float(self.xEndPixel-self.xStartPixel)

        range=self.vectors.getRange()
        self.yStart=range[0]
        self.yMid=range[1]
        self.yEnd=range[2]

        if(self.yStart!=self.yEnd):
            self.yStartPixel=self.size[1]-self.xStartPixel
            self.yEndPixel=self.xStartPixel
            if(self.yStart>=0):
                self.yPixeltoPointFactor=float(self.yEnd-float(self.yStart))/float(-self.yEndPixel+self.yStartPixel)/(float(self.yEnd-self.yStart)/float(self.yEnd))
                self.yOriginPixel=self.yStartPixel
            else:
                self.yPixeltoPointFactor=float(self.yEnd-float(self.yStart))/float(-self.yEndPixel+self.yStartPixel)
                self.yOriginPixel=self.yStartPixel-int(float(0-self.yStart)/float(self.yPixeltoPointFactor))
        else:
            self.yStartPixel=self.size[1]-self.xStartPixel
            self.yOriginPixel=self.size[1]-self.xStartPixel
            self.yEndPixel=self.xStartPixel
            if self.yStart!=0:
                self.yPixeltoPointFactor=float(self.yStart)/float(self.yStartPixel-self.yEndPixel)
            else:
                self.yPixeltoPointFactor=float(1)/float(self.yStartPixel-self.yEndPixel)
        for point in self.points:
            xPixelCoordinate=self.xOriginPixel+int(float(point[0])/float(self.xPixeltoPointFactor))
            yPixelCoordinate=self.yOriginPixel-int(float(point[1])/float(self.yPixeltoPointFactor))
            self.pointToPixelCoordinates.add((xPixelCoordinate,yPixelCoordinate,point[0],point[1]))
        print "(xOrigin, yOrigin) : "+" "+"("+str(self.xOriginPixel)+", "+str(self.yOriginPixel)+")"
        print "(xPixeltoPoint, yPixeltoPoint) : "+" "+"("+str(self.xPixeltoPointFactor)+", "+str(self.yPixeltoPointFactor)+")"

    def draw(self):
        domain=self.vectors.getDomain()
        range=self.vectors.getRange()
        print "domain: " +str(domain[0])+" "+str(domain[1])+" "+str(domain[2])
        print "range: " +str(range[0])+" "+str(range[1])+" "+str(range[2])
        # Define the colors we will use in RGB format
        while not self.done:
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            self.clock.tick(10)

            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.done=True # Flag that we are done so we exit this loop

            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.

            # Clear the screen and set the screen background
            self.screen.fill(self.BLACK)

             # Draw on the screen a GREEN line from (0,0) to (50.75)
            pygame.init()
             # 5 pixels wide.
            pygame.draw.aaline(self.screen, self.WHITE, [self.xStartPixel, self.yOriginPixel],[self.xEndPixel, self.yOriginPixel], True)
            pygame.draw.aaline(self.screen, self.WHITE, [self.xOriginPixel,self.yStartPixel ],[self.xOriginPixel,self.yEndPixel], True)
            for pointToPixelCoordinate in self.pointToPixelCoordinates:
            #     xPixelCoordinate=self.xOriginPixel+int(float(point[0])*float(self.xPixeltoPointFactor))
            #     print xPixelCoordinate
            #     yPixelCoordinate=self.yOriginPixel+int(float(point[1])*float(self.yPixeltoPointFactor))
            #     print yPixelCoordinate
                  pygame.draw.aaline(self.screen,self.BLUE,[pointToPixelCoordinate[0],self.yOriginPixel],[pointToPixelCoordinate[0],pointToPixelCoordinate[1]],True)
                  # Draw a circle
                  pygame.draw.circle(self.screen, self.BLUE, [pointToPixelCoordinate[0], pointToPixelCoordinate[1]], 4)
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


