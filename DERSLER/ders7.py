# ! CLASSLAR

# ! Örnek
# class Movie:
#     def __init__(self, name , director):
#         self.name = name
#         self.director = director

# movie1 = Movie("Prestige" , "Christopher Nolan")
# movie2 = Movie("Babel", "Irrarutu")

# print(movie1)
# print(type(movie1))
# print(movie1.name)
# print(type(movie1.name))
# print(movie2.director)


# ! Örnek
# class Urun:
#     def __init__(self, isim , aciklama , fiyat):
#         self.isim = isim
#         self.aciklama = aciklama
#         self.fiyat = fiyat

#     def bilgi(self):
#         ürünBilgisi = self.isim , self.aciklama , self.fiyat
#         for i in range(len(ürünBilgisi)):
#             print(ürünBilgisi[i])

# ürün1 = Urun("Iphone14", "Cep Telefonu", "60000")
# ürün2 = Urun("Macbook Air", "Bilgisayar", "38000")

# ürün1.bilgi()
# print("-------")
# ürün2.bilgi()


# ! Örnek-3
class Car:
    def __init__(self, marka , model , yil , güc):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.güc = güc

    def markamodel(self):
        return f"{self.marka}{self.model}{self.yil},{self.güc}"
    
car1 = Car("Mercedes","C200", "2020","300")
car2 = Car("Audi","A5", "2020","200")
car3 = Car("BMW","M4", "2018","400")

# print(car1)
# print(car1.marka)
# print(car1.model)
# print(car1.yil)
# print(car1.markamodel())

# ! Örnek-3 Version-2
class Car:

    cars = []

    def __init__(self, marka , model , yil , güc):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.güc = güc
        Car.cars.append(self)

    def markamodel(self):
        return f"{self.marka}{self.model}{self.yil},{self.güc}"
    
car1 = Car("Mercedes","C200", "2020","300")
car2 = Car("Audi","A5", "2020","200")
car3 = Car("BMW","M4", "2018","400")
car4 = Car("Fiat","Egea","2023","150")

print(Car.cars)