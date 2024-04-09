# # # class Osoba:
# # #     def __init__(self, jmeno, prijmeni):
# # #         self.jmeno = jmeno
# # #         self.prijmeni = prijmeni
# # #
# # #     def __str__(self):
# # #         return f"{self.jmeno} {self.prijmeni}"
# # #
# # # class Žák(Osoba):
# # #     def __init__(self, jmeno, prijmeni, trida, prumer):
# # #         super().__init__(jmeno, prijmeni)
# # #         self.trida = trida
# # #         self.prumer = prumer
# # #
# # #     def __str__(self):
# # #         return f"{super().__str__()} je žák třídy {self.trida} s průměrem {self.prumer}"
# # #
# # #     def __gt__(self, other):
# # #         return self.prumer > other.prumer
# # #
# # #     def __lt__(self, other):
# # #         return self.prumer < other.prumer
# # #
# # #     def __eq__(self, other):
# # #         return self.prumer == other.prumer
# # #
# # # # Příklad použití třídy
# # # žák1 = Žák("Jan", "Novák", "3A", 3.8)
# # # žák2 = Žák("Eva", "Svobodová", "3B", 4.2)
# # #
# # # print(žák1)  # Vypíše: Jan Novák je žák třídy 3A s průměrem 3.8
# # # print(žák2)  # Vypíše: Eva Svobodová je žák třídy 3B s průměrem 4.2
# # #
# # # if žák1 > žák2:
# # #     print(f"{žák1} má lepší průměr než {žák2}.")
# # # elif žák1 < žák2:
# # #     print(f"{žák1} má ho
# # #
# class Auto:
#     def __init__(self, rychlost, váha):
#         self.rychlost = rychlost
#         self.váha = váha
#
#     def checkSpeedLimitObec(self):
#         if self.rychlost > 50:
#             print("Auto překračuje povolenou rychlost v obci.")
#         else:
#             print("Auto je v souladu s povolenou rychlostí v obci.")
#
#     def checkSpeedLimitDálnice(self):
#         if self.váha <= 3500:
#             if self.rychlost > 130:
#                 print("Auto překračuje povolenou rychlost na dálnici.")
#             else:
#                 print("Auto je v souladu s povolenou rychlostí na dálnici.")
#         else:
#             if self.rychlost > 80:
#                 print("Auto překračuje povolenou rychlost na dálnici.")
#             else:
#                 print("Auto je v souladu s povolenou rychlostí na dálnici.")
#
# # Příklad použití třídy
# auto1 = Auto(60, 2000)  # Auto s rychlostí 60 km/h a váhou 2000 kg
# auto2 = Auto(140, 4000) # Auto s rychlostí 140 km/h a váhou 4000 kg
#
# print("Kontrola rychlosti v obci:")
# auto1.checkSpeedLimitObec()  # Vypíše: Auto překračuje povolenou rychlost v obci.
# auto2.checkSpeedLimitObec()  # Vypíše: Auto je v souladu s povolenou rychlostí v obci.
#
# print("\nKontrola rychlosti na dálnici:")
# auto1.checkSpeedLimitDálnice()  # Vypíše: Auto je v souladu s povolenou rychlostí na dálnici.
# auto2.checkSpeedLimitDálnice()  # Vypíše: Auto překračuje povolenou rychlost na dálnici.
#
# class Kamion(Auto):
#     def __init__(self, rychlost, váha, zatížení):
#         super().__init__(rychlost, váha)
#         self.zatížení = zatížení
#
#     def checkSpeedLimitObec(self):
#         if self.rychlost > 50:
#             print("Kamion překračuje povolenou rychlost v obci.")
#         else:
#             print("Kamion je v souladu s povolenou rychlostí v obci.")
#
#     def checkSpeedLimitDálnice(self):
#         if self.váha + self.zatížení <= 3500:
#             if self.rychlost > 80:
#                 print("Kamion překračuje povolenou rychlost na dálnici.")
#             else:
#                 print("Kamion je v souladu s povolenou rychlostí na dálnici.")
#         else:
#             if self.rychlost > 80:
#                 print("Kamion překračuje povolenou rychlost na dálnici.")
#             else:
#                 print("Kamion je v souladu s povolenou rychlostí na dálnici.")
#


class Book:
    def __init__(self,title,author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showInfo(self):
        print (f'Title: {self.title} Author: {self.author} Pages: {self.pages}')

    def __str__(self):
        return (f'Title: {self.title} Author: {self.author} Pages: {self.pages}')


book1 = Book("Python Crash Course","Eric Matthes",624)
book2 = Book("JavaScript: The Good Parts","Douglas Crockford",170)

#print(book1+book2)
print(book1)
book1.showInfo()