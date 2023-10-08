# ! Hesap Makinesi Örneği

# giris = f"""
# 1 Topla
# 2 Çıkar
# 3 Çarp
# 4 Böl
# 5 Üssünü Hesapla
# 6 Karekökünü Hesapla
# """

# print(giris)

# while True:
#     islem = input("Yapmak istediğiniz işlemi giriniz. (Çıkış yapmak için q:)")

#     if islem == "q":
#         print("Çıkış yapılıyor...")
#         break
#     elif islem == "1":
#         sayi1 = int(input("Toplama işlemi için ilk sayıyı giriniz:"))
#         sayi2 = int(input("Toplama işlemi için ikinci sayıyı giriniz:"))
#         sonuc = sayi1 + sayi2
#         print(f"Sonuc: {sonuc}")
#     elif islem == "2":
#         sayi1 = int(input("Çıkarma işlemi için ilk sayıyı giriniz:"))
#         sayi2 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz:"))
#         sonuc = sayi1 - sayi2
#         print(f"Sonuc: {sonuc}")
#     elif islem == "3":
#         sayi1 = int(input("Çarpma işlemi için ilk sayıyı giriniz:"))
#         sayi2 = int(input("Çarpma işlemi için ikinci sayıyı giriniz:"))
#         sonuc = sayi1 * sayi2
#         print(f"Sonuc: {sonuc}")
#     elif islem == "4":
#         sayi1 = int(input("Bölme işlemi için ilk sayıyı giriniz:"))
#         sayi2 = int(input("Bölme işlemi için ikinci sayıyı giriniz:"))
#         sonuc = sayi1 / sayi2
#         print(f"Sonuc: {sonuc}")
#     elif islem == "5":
#         sayi1 = int(input("Üs alma işlemi için ilk sayıyı giriniz:"))
#         sayi2 = float(input("Üs alma işlemi için ikinci sayıyı giriniz:"))
#         sonuc = sayi1 ** sayi2
#         print(f"Sonuc: {sonuc}")
#     elif islem == "6":
#         sayi1 = int(input("Karekök alma işlemi için ilk sayıyı giriniz:"))
#         sonuc = sayi1 ** 0.5
#         print(f"Sonuc: {sonuc}")
#     else:
#         print("Geçerli bir işlem giriniz")


# ! ATM UYGULAMASI
def atm():
    hesabım = "Furkan"
    sifrem = "1234"
    bakiye = 5000
    borc = 3000
    hak = 3

    while True:
        hak = hak - 1
        print(f"Kalan hakkınız {hak}")
        kullanici = input("Kullanıcı adınızı giriniz:")
        sifre = input("Şifrenizi giriniz:")
        if kullanici == hesabım and sifre == sifrem:
            print(f"Bakiyeniz : {bakiye}₺")
            while True:
                print(f"""

Hoşgeldiniz. Yapabileceğiniz İşlemler:
1-Para Çekme
2-Para Yatırma
3-Para Gönderme
4-Şifre Değiştirme
5-Bakiye Sorgulama
6-Borç Sorgulama
7-Çıkış                     
                      
""")
                islem = int(input("Yapacağınız işlemi giriniz:"))
                if islem == 1:
                    print(f"Bakiyeniz : {bakiye}₺")
                    cek = int(input("Çekmek istediğiniz tutarı giriniz:"))
                    if bakiye > cek:
                        bakiye = bakiye - cek
                        print(f"Para çekme işleminiz başarıyla gerçekleştirildi. Güncel bakiyeniz : {bakiye}₺ ")
                    else:
                        print("Bakiyeniz yetersiz")

                elif islem == 2:
                    yatir = int(input("Yatırmak istediğiniz tutarı giriniz:"))
                    bakiye = bakiye + yatir
                    print(f"Para yatırma işleminiz başarılı. Güncel bakiyeniz : {bakiye}₺")
                
                elif islem == 3:
                    print(f"Güncel bakiye {bakiye}₺")
                    gönder = int(input("Gönderilecek tutarı giriniz:"))
                    if bakiye >= gönder:
                        bakiye -= gönder
                        print(f"İşlem başarılı. Kalan bakiyeniz: {bakiye}₺")
                    else:
                        print("Bakiyeniz yetersiz")
                
                elif islem == 4:
                    while True:
                        mevcutSifre = input("Mevcut şifrenizi giriniz:")
                        if mevcutSifre == sifrem:
                            yeniSifre = input("Yeni şifrenizi giriniz:")
                            sifrem = yeniSifre
                            print(f"Şifreniz değiştirildi. Yeni şifreniz {sifrem}")
                            break
                        else:
                            print("Hatalı şifre")
                elif islem == 5:
                    print(f"Mevcut bakiyeniz: {bakiye}₺")
                elif islem == 6:
                    print(f"Borcunuz : {borc}₺")
                elif islem == 7:
                    print("Çıkış yappılıyor...")
                    break
        elif hak == 1:
            print("Hakkınız dolmuştur.")
            break                
atm()
