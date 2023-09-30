# ! LİSTELER

# cities = ["İstanbul","Ankara","İzmir","Bursa","Sivas","Samsun","Eskişehir"]

# print(type(cities))
# print(cities[0])
# print(cities[len(cities)-1])
# print(cities[-1])
# print(cities[0:5:2])

# cities[0] = "Aydın"
# print(cities)

# ! Listenin sonuna eleman eklemek için;
# cities.append("Denizli")
# print(cities)

# cities.insert(1,"Sakarya")
# print(cities)

# cities.pop()
# print(cities)

# ! Uygulama
# dersler = ["matematik","kimya","biyoloji","tarih","fizik"]

# dersler.upper(2)
# print(dersler[2].upper())
# print(dersler)

# dersler[2] = "BİYOLOJİ"
# print(dersler)

# dersler[2] = dersler[2].upper()
# print(dersler)

# print(dersler[0], dersler[2])
# print(dersler[0:3:2])

# ! Uygulama
# dersler = ["matematik",["fizik","kimya"],"ingilizce","türkçe"]

# print(dersler[1][0],dersler[1][1])

# fizik = dersler[1][0]
# kimya = dersler[1][1]

# print(f"""
# {fizik}
# {kimya}
# """)

# dersler.append("edebiyat")
# print(dersler)

# dersler[1].append("biyoloji")
# print(dersler)

# ! TUPLE KULLANIMI
# dizi = ("ankara","berlin","londra","tahran","tokyo","roma")

# print(type(dizi))
# dizi[3] = "paris"

# dizi = list(dizi)
# print(type(dizi))
# dizi[3] = "paris"
# print(dizi)

# dizi = tuple(dizi)
# print(type(dizi))


# ! If-Else Kullanımı
# ! Kullanıcıdan bir sayı alalım. Sayı 10 dan küçükse güle güle desin 10dan büyükse hoşgeldiniz desin.

# sayi = int(input("Bir sayı giriniz:"))

# if sayi < 10:
#     print(f"Girdiğin sayı : {sayi}. Güle Güle")
# else:
#     print(f"Girdiğin sayı : {sayi}. Hoşgeldin")


# ! Uygulama

# vize = int(input("Vize değerini giriniz: "))
# final = int(input("Final değerini giriniz: "))

# ortalama = ((vize*0.4) + (final*0.6))
# print(type(ortalama))
# print(ortalama)
# if vize <= 100 and final <= 100:
#     if ortalama > 85 and ortalama <= 100:
#         print(f"Ortalamanız {ortalama} Harf notunuz: A")
#     elif ortalama > 70 and ortalama <= 85:
#         print(f"Ortalamanız {ortalama} Harf notunuz: B")
#     elif ortalama > 55 and ortalama <= 70:
#         print(f"Ortalamanız {ortalama} Harf notunuz: C")
#     elif ortalama > 45 and ortalama <= 55:
#         print(f"Ortalamanız {ortalama} Harf notunuz: D")
#     elif ortalama > 0 and ortalama <= 45:
#         print(f"Ortalamanız {ortalama} Harf notunuz: F")
# else:
#     print("Geçersiz not girdiniz.")


# ! Uygulama
# x = int(input("x değerini giriniz :"))
# y = int(input("y değerini giriniz :"))
# z = int(input("z değerini giriniz :"))

# if x > y and x > z:
#     print(f"Girmiş olduğunuz sayılar: X :{x} Y :{y} Z :{z} En büyük sayı {x}")
# elif y > x and y > z:
#     print(f"Girmiş olduğunuz sayılar: X :{x} Y :{y} Z :{z} En büyük sayı {y}")
# elif z > x and z > y:
#     print(f"Girmiş olduğunuz sayılar: X :{x} Y :{y} Z :{z} En büyük sayı {z}")


# ! Uygulama
# boy = int(input("Boyunuzu cm cinsinden giriniz :"))
# kilo = int(input("Kilonuzu giriniz :"))

# index = (kilo / (boy / 100) ** 2)

# if index < 18.5:
#     print(f"{index} Zayıf")
# elif index >= 18.5 and index < 24.9:
#     print(f"{index} Normal")
# elif index >= 25 and index < 29.9:
#     print(f"{index} Fazla Kilolu")
# elif index >= 30 and index < 39.9:
#     print(f"{index} Obez")
# elif index >= 40:
#     print(f"{index} Morbit Obez")



    



