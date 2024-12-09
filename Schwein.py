

# Klasse Schwein
# Attribute:
# name
# gewicht
# Funktionalität:
# laufen(schritte) => gewicht nimmt in Abhängigkeit der schritte ab
# fressen(bissen) => gewicht nimmt in Abhängigkeit der bissen zu

class Pig:
    def __init__(self, name="standardpig", weight=0):
        self.name = name
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def weight(self):
      return self.__weight

    @weight.setter
    def weight(self, value):
      self.__weight = value


    def __str__(self):
        return f"Pig [Name = {self.name}, Weight = {self.weight}]"

    def walk(self, steps):
        self.weight = self.weight - steps
        return print (f"The {self.__class__.__name__} {self.name} walks {steps} steps and is getting more hungry. \n {self.name} weighs now {self.weight} ")

    def gobble(self, bites, food):
        self.weight = self.weight + bites
        food.get_eaten(bites)
        return print(f"The {self.__class__.__name__} {self.name} gobbles up the carrot {food.sort}")