class shapes():
    def __init__(self,name,numbersides,colour):
     self.name=name
     self.numbersides=numbersides
     self.colour=colour
    
    def display(self):
       print(self.name, self.numbersides,self.colour)

s1=shapes("triangle","3","pink")
s1.display() 
s2=shapes("square","4","blue")
s2.display() 
s3=shapes("hexagon","6","green")
s3.display() 