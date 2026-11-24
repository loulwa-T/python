class rectangle():
    def __init__(self,width,length):
     self.width=width
     self.length=length
    
    def display(self):
       print(self.width, self.length)
    def area(self):
           print(self.width * self.length)
    def parameter(self):
           print(self.width * 2 + self.length *2 )


s1=rectangle(5,2)
s1.display() 
s1.area()
s1.parameter()

s2=rectangle(4,3)
s2.display() 
s2.area()
s2.parameter()

s3=rectangle(6,8)
s3.display() 
s3.area()
s3.parameter()

