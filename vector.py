
class functionPoints:
    vectors=[(0,0)]
    indices=[]
    domainMin=100000000000
    domainMax=-100000000000
    rangeMin=100000000000
    rangeMax=-100000000000

    def __init__(self):
        self.vectors.pop(0)
        pass

    def addAll(self,vectors):
        for vector in vectors:
            self.indices.append(vector[0])
            self.vectors.append(vector)

    def add(self,vector):
        self.indices.append(vector[0])
        self.vectors.append(vector)

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
                self.indices.append(i)
                self.vectors.append((i,magnitude))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]<0 and SSSEargs[2]<SSSEargs[0]):
            print "Negative Step"
            while i>=SSSEargs[2]:
                self.indices.append(i)
                self.vectors.append((i,magnitude))
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
                self.indices.append(i)
                self.vectors.append((i,0))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]<0 and SSSEargs[2]<SSSEargs[0]):
            print "Negative Step"
            while i>=SSSEargs[2]:
                self.indices.append(i)
                self.vectors.append((i,0))
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
                self.indices.append(i)
                self.vectors.append((i,1))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]<0 and SSSEargs[2]<SSSEargs[0]):
            print "Negative Step"
            while i>=SSSEargs[2]:
                self.indices.append(i)
                self.vectors.append((i,1))
                i=i+SSSEargs[1]
        elif (SSSEargs[1]==0):
            print "Step Size Must be None-Zero!"

        elif (SSSEargs[1]<0):
            print "End point must be less that Start for Negative steps"

        else:
            print "End point must be greater than Start for Positive steps"

    def getYforX(self,x):
        something = [vector[1] for vector in self.vectors if vector[0] == x]
        return something

    def doesListContain(self,list,vec):
        item=0.0
        for item in list:
            if(item is vec):
                return True

        return False

    def splitIntoEvenAndOdd(self):
        even=[(0,0)]
        odd=[(0,0)]
        even.pop(0)
        odd.pop(0)
        print self.indices
        for indice in self.indices:
            if(indice!=float(0)):
                if(indice):
                    if -indice in self.indices:
                        print "contains works"
                        even.append((indice,float(self.getYforX(indice)+self.getYforX(-indice))/float(2)))
                    else:
                        print str(-indice)+" is not a valid index"
                        even.append((indice,float(self.getYforX(indice))/float(2)))
                        even.append((-indice,float(self.getYforX(indice))/float(2)))
        if 0 in self.indices:
            even.append((0,float(self.getYforX(0))))
        else:
            even.append((0,0))

        for indice in self.indices:
            if(indice):
                if -indice in self.indices:
                    print "contains works"
                    odd.append((indice,float(self.getYforX(indice)-self.getYforX(-indice))/float(2)))
                else:
                    odd.append((indice,-float(self.getYforX(indice))/float(2)))
                    odd.append((-indice,-float(self.getYforX(indice))/float(2)))

        return [even,odd]

    def clear(self):
        self.vectors=[(0,0)]
        self.vectors.pop(0)