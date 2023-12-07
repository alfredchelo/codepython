#declaracion de objeto
class character:
  
    #metodo constructor
    def __init__(self, name,force, intelligence , defending, life):
        self.name = name
        self.force = force
        self.intelligence = intelligence
        self.defending = defending
        self.life = life

    def attributes(self):
        print(self.name, ":", sep="")
        print("force: ",self.force)
        print("intelligence: ",self.intelligence)
        print("defendig: ",self.defending)
        print("life: ",self.life)
    
    def leve_up(self,force, intelligence, defendig):
        self.force += force 
        self.intelligence += intelligence 
        self.defending += defendig 

me_character = character("alfred",10,1,5,100)
me_character.attributes()

me_character.leve_up(1,1,1)
me_character.attributes()
