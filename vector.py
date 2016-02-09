
class functionPoints:
    vectors={(0,0)}
    domainMin=100000000000
    domainMax=-100000000000
    rangeMin=100000000000
    rangeMax=-100000000000

    def __init__(self):
        pass

    def addAll(self,vectors):
        for vector in vectors:
            self.vectors.add(vector)

    def add(self,vector):
        self.vectors.add(vector)

    def getDomain(self):
        for vector in self.vectors:
            if(vector[0]>self.domainMax):
                self.domainMax=vector[0]

            if(vector[0]<self.domainMin):
                self.domainMin=vector[0]
        if(self.domainMin==100000000000):
            self.domainMin=0
        if(self.domainMax==-100000000000):
            self.domainMax=1

        return (self.domainMin,(self.domainMin+self.domainMax)/2,self.domainMax)



    def getRange(self):
        for vector in self.vectors:
            if(vector[1]>self.rangeMax):
                self.rangeMax=vector[1]

            if(vector[1]<self.rangeMin):
                self.rangeMin=vector[1]
        if(self.rangeMin==100000000000):
            self.rangeMin=0
        if(self.rangeMax==-100000000000):
            self.rangeMax=1

        return (self.rangeMin,(self.rangeMin+self.rangeMax)/2,self.rangeMax)

    def getVector(self):
        return self.vectors

    def addPoints(self,magnitude,SSSEargs):
        i=float(SSSEargs[0])
        if(SSSEargs[1]>0 and SSSEargs[0]<SSSEargs[2]):
            print "positive Step"
            while i<=SSSEargs[2]:
                self.vectors.add((i,magnitude))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]<0 and SSSEargs[2]<SSSEargs[0]):
            print "Negative Step"
            while i>=SSSEargs[2]:
                self.vectors.add((i,magnitude))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]==0):
            print "Step Size Must be None-Zero!"

        elif (SSSEargs[1]<0):
            print "End point must be less that Start for Negative steps"

        else:
            print "End point must be greater than Start for Positive steps"

    def addZeros(self,SSSEargs):
        i=float(SSSEargs[0])
        if(SSSEargs[1]>0 and SSSEargs[0]<SSSEargs[2]):
            print "positive Step"
            while i<=SSSEargs[2]:
                self.vectors.add((i,0))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]<0 and SSSEargs[2]<SSSEargs[0]):
            print "Negative Step"
            while i>=SSSEargs[2]:
                self.vectors.add((i,0))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]==0):
            print "Step Size Must be None-Zero!"

        elif (SSSEargs[1]<0):
            print "End point must be less that Start for Negative steps"

        else:
            print "End point must be greater than Start for Positive steps"

    def addOnes(self,SSSEargs):
        i=float(SSSEargs[0])
        if(SSSEargs[1]>0 and SSSEargs[0]<SSSEargs[2]):
            print "positive Step"
            while i<=SSSEargs[2]:
                self.vectors.add((i,1))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]<0 and SSSEargs[2]<SSSEargs[0]):
            print "Negative Step"
            while i>=SSSEargs[2]:
                self.vectors.add((i,1))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]==0):
            print "Step Size Must be None-Zero!"

        elif (SSSEargs[1]<0):
            print "End point must be less that Start for Negative steps"

        else:
            print "End point must be greater than Start for Positive steps"

