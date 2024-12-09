from bauernhofsimulator.Schwein import Pig


class Piglet(Pig):
    def __init__(self, name="Hans", weight=35, color="yellow"):
        super().__init__(name, weight)
        self.name = name
        self.weight = weight
        self.color = color

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #
    # @property
    # def weight(self):
    #     return self.__weight
    #
    # @name.setter
    # def weight(self):
    #     self.__weight = value

    def __str__(self):
        return f"Piglet [name={self.name}, weight={self.weight}, color={self.color}]"
