# ! Dictionary 

# karakter = {
#     "isim":"Furkan",
#     "soyisim":"İlaslan",
#     "yas":26,
#     "meslek":"Eğitmen",
# }

# print(karakter)
# print(type(karakter))
# print(len(karakter))
# print(karakter["isim"])
# karakter["medeni durum"] = "bekar"
# print(karakter)
# karakter["isim"] = "Ahmet"
# print(karakter)
# print(karakter.keys())
# print(karakter.values())
# print(karakter.items())

# ! Hem key hem de value değerini güncellemek için
# karakter.update({"isim": "Ali" , "kan grubu": "A Rh+"})
# print(karakter)

# ! İstediğim elemanı silmek için
# karakter.pop("meslek")
# print(karakter)

# ! Dictionary İle Döngü Kullanımı

# for i in karakter:
#     print(i)
# key değerlerini döndürürü

# for i in karakter:
#     print(karakter[i])
# value değerlerini döndürür.

# for i,j in karakter.items():
#     print(i,j)
# Hem key hem de value değerlerini döndürür.


# ! Örnek-1
# ! Aşağıda verilen notlardan 50 ve üzeri olanları geçti diğerlerini kaldı olarak belirleyelim.

# notlar = {"Ahmet": 30, "Selim": 58, "Hüseyin": 75, "Hasan":44}

# print(notlar.items())

# for ad,puan in notlar.items():
#     if puan > 50:
#         print(f"Öğrenci Adı: {ad}, Öğrenci Puanı : {puan} GEÇTİ")
#     else:
#         print(f"Öğrenci Adı: {ad}, Öğrenci Puanı : {puan} KALDI")
        

# ! Örnek-2
# kelime_sozlugu = {
#     "hello": "Merhaba",
#     "book" : "Kitap",
#     "read" : "Okumak",
#     "good night" : "İyi geceler",
# }

# kelime = input("Bir kelime giriniz :").lower()

# while True:
#     if kelime in kelime_sozlugu:
#         print(f"{kelime} : {kelime_sozlugu[kelime]} ")
#         break
#     else:
#         print("Bu kelimenin sözlükte karşılığı yok. Kontrol ederek tekrar yazınız.")
#         kelime = input("Başka bir kelime giriniz :").lower()


# ! Örnek-3

# ogrenci_notları = {}

# while True:
#     ogrenci_ad = input("Öğrenci adını giriniz (Çıkmak için q tuşuna basınız :)")

#     if ogrenci_ad == "q":
#         break

#     ogrenci_notu = int(input("Notunuzu giriniz:"))
#     ogrenci_notları[ogrenci_ad] = ogrenci_notu

# aranan_ogrenci = input("Notunu görmek istediğiniz öğrencinin adını giriniz:")
# if aranan_ogrenci in ogrenci_notları:
#     print(f"{aranan_ogrenci}'nin notu : {ogrenci_notları[aranan_ogrenci]}")
#     ogrenci_listesi = list(ogrenci_notları.items())
#     print(ogrenci_listesi)
# else:
#     print("Öğrenci kayıtlı değildir.")


# ! Örnek-4

# veri = {"Ahmet": 30 , "Mehmet": 40, "Kerem": 20}

# veri_listesi = list(veri.keys())
# print(veri_listesi)


# ! Örnek-5
envanter = {}

menu = """
1 Ürün Eklemek
2 ürün Çıkarmak
3 Envanteri Listelemek
4 Çıkış
"""

while True:
    print(menu)

    secim = input("Yapmak istediğiniz işlemi seçiniz: ")

    if secim == "1":
        urun = input("Eklemek istediğiniz ürünü giriniz: ")
        miktar = int(input(f"Eklenecek {urun} miktarını giriniz : "))

        if urun in envanter:
            envanter[urun] += miktar
        else:
            envanter[urun] = miktar
    
    elif secim == "2":
        urun = input("Çıkarmak istediğiniz ürünü giriniz: ")
        miktar = int(input(f"Çıkarılacak {urun} miktarını giriniz : "))

        if urun in envanter:
            if envanter[urun] >= miktar:
               envanter[urun] -= miktar 
               print(f"{miktar} adet {urun} envanterden çıkarıldı.")
            else:
                print(f"Envanterde yeterli {urun} yok.")
    elif secim == "3":
        print("Güncel Envanter Durumu")
        for key , value  in envanter.items():
            print(f"{key} : {value} adet vardır.")

    elif secim == "4":
        break 
    else:
        print("Yanlış değer girdiniz")
        
