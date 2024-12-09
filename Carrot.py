# Klasse Moehre
# Attribute:
# sorte
# ruebenlaenge
# Funktionalität:
# wachsen() => ruebenlaenge nimmt zu
# wird_gefressen(menge) => ruebenlaenge nimmt in Abhängigkeit der menge ab

class Carrot:
    def __init__(self, sort="red_delicious", taproot_length=10):
        self.sort = sort
        self.taproot_length = taproot_length
    def __str__(self):
        return f"Möhre[sort = {self.sort}, length = {self.taproot_length}]"


    @property
    def sort(self):
        return self.__sort

    @sort.setter
    def sort(self, value):
        self.__sort = value

    @property
    def taproot_length(self):
      return self.__taproot_length

    @taproot_length.setter
    def taproot_length(self, value):
       self.__taproot_length = value

    def grow(self):
        self.taproot_length = self.taproot_length + 5

    def get_eaten(self, amount):
        self.taproot_length = self.taproot_length - amount