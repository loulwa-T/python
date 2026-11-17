class animal():
    def __init__(self,name,species):
     self.name=name
     self.species=species
    
    def display(self):
       print(self.name, self.species)

animal1=animal("buddy","dog")
animal1.display()
animal2=animal("muffin","cat")
animal2.display()