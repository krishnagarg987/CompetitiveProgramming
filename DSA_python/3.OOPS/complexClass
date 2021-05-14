class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def printComplex(self):
        if self.real==0 and self.imag==0:
            print(0)
        elif self.real==0:
            print(self.imag,"i")
        elif self.imag==0:
            print(self.real)
        else:
            if self.imag>0:
                print(self.real,'+',self.imag,'i')
            else:
                print(self.real,self.imag,'i')
                
    def addComplex(self,otherComplex):
        self.real+=otherComplex.real
        self.imag+=otherComplex.imag
    
    def subtractComplex(self,otherComplex):
        self.real-=otherComplex.real
        self.imag-=otherComplex.imag
    
    def multiplyComplex(self,otherComplex):
        newReal=self.real*otherComplex.real+(self.imag*otherComplex.imag*(-1))
        newImag=(self.real*otherComplex.imag)+(self.imag*otherComplex.real)
        self.real=newReal
        self.imag=newImag
    
    def conjugateComplex(self):
        if self.imag==0:
            return
        else:
            self.imag*=(-1)

c1=complex(2,3)
c2=complex(4,-5)
c1.subtractComplex(c2)
c1.printComplex()
        
        
