from bauernhofsimulator.Schwein import Pig
from bauernhofsimulator.Carrot import Carrot
from bauernhofsimulator.Piglet import Piglet

p = Pig("Guido", 85)
pp = Piglet("Hans", 35)
c = Carrot("red_delicious", )



p.gobble(20, c)
pp.gobble(20, c)
print(p)
print(pp)
print(c)

for i in range(12):
    p.walk(10)
    pp.walk(22)
    c.grow()
    print(p)
    print(pp)
    print(c)
    print("\n \n")
    p.gobble(2, c)
    pp.gobble(2, c)
    print(p)
    print(pp)
    print(c)

# p.walk(25)
# print(p)
# c.grow(5)
# p.gobble(30)
# print(p)
#
#
# print(p.gobble)





#
# 25
# ​#------------------------[Bauernhofsimulator.py]------------------------
# from bauernhofsimulator.Schwein import Schwein
#
# s = Schwein()
# print(s)
# s.laufen(50)
# print(s)
# s.fressen(100)
# print(s)
# ​#------------------------[Schwein.py]------------------------
# # Klasse Schwein
# # Attribute:
# #     name
# #     gewicht
# # Funktionalität:
# #     laufen(schritte)        =>  gewicht nimmt in Abhängigkeit der schritte ab
# #     fressen(bissen)         =>  gewicht nimmt in Abhängigkeit der bissen zu
#
#
#
# class Schwein():
#     def __init__(self, name="Standardschwein", gewicht=200):
#         self.name = name
#         self.gewicht = gewicht
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def gewicht(self):
#         return self.__gewicht
#
#     @gewicht.setter
#     def gewicht(self, value):
#         self.__gewicht = value
#
#     def __str__(self):
#         return f"Schwein[name={self.name}, gewicht={self.gewicht}]"
#
#     def laufen(self, schritte):
#         self.gewicht = self.gewicht - schritte
#
#     def fressen(self, bissen):
#         self.gewicht = self.gewicht + bissen