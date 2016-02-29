
class matrix:
    mats=[()]

    def __init__(self):
        pass

    def add(self,matrices):
        self.mats.pop(0)
        for matric in matrices:
            self.mats.append(matric)

    def show(self):
        print "{"
        for mat in self.mats:
            print " ",
            for x in range(0,len(mat)):
                print str(mat[x])+" ",
            print ""
        print "}"

    def zeros(self,indices):
        x=indices[0]
        tupl=[()]
        tupl.pop(0)
        while x<=indices[2]:
            tupl.append(0)
            x=x+indices[1]
        self.mats.append(tupl)

    def ones(self,indices):
        x=indices[0]
        tupl=[()]
        tupl.pop(0)
        while x<=indices[2]:
            tupl.append(1)
            x=x+indices[1]
        self.mats.append(tupl)

    def scaledPoint(self,magnitude,indices):
        x=indices[0]
        tupl=[()]
        tupl.pop(0)
        while x<=indices[2]:
            tupl.append(magnitude)
            x=x+indices[1]
        self.mats.append(tupl)

    def getRow(self,rowNo):
        return self.mats.__getitem__(rowNo)

    def getColumn(self,colomnNo):
        tuple=[()]
        tuple.pop(0)
        for mat in self.mats:
            tuple.append(mat[colomnNo])
        return tuple

    def getValueAt(self,x,y):
        return self.mats.__getitem__(y).__getitem__(x)

