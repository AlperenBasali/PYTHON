
# ! İf-Else Örnek
# sayi = int(input("Bir sayı giriniz : "))

# if sayi % 2 == 0 and sayi > 0:
#     print(f"Girmiş olduğunuz sayı {sayi} Bu sayı çift bir sayıdır")
# elif sayi == 0:
#     print(f"Girmiş olduğunuz sayı {sayi} Sonucu sıfırdır.")
# elif sayi % 2 != 0 and sayi > 0:
#     print(f"Girmiş olduğunuz sayı {sayi} Sayı pozitif tek sayıdır")


# ! DÖNGÜLER
# ! 1'den 10'a kadar olan sayıları yazdıralım

# for i in range(1,11,1):
#     print(i)

# isimler = ["abdullah","ahmet","selim","eren"]
# f
# u
# r
# k
# a
# n

# for i in range(len(isim)):
#     print(isim[i])

# for isim in isimler:
#     for harf in isim:
#         print(harf)


# ! Örnek
# Merhaba
# Merhaba Merhaba
# Merhaba Merhaba Merhaba
# Merhaba Merhaba Merhaba Merhaba
# Merhaba Merhaba Merhaba Merhaba Merhaba

# for i in range(1,6,1):
#     print(i * " Merhaba")


# ! Örnek
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# for i in range(1,6,1):
#     print("*" * i)
# for i in range(6,0,-1):
#     print("*" * i)


# ! Örnek
# ***************(15 adet)
# *
# *
# *
# **********(10 adet)
# *
# *
# *
# *
# *

# for i in range(1,11):
#     if i == 1:
#         print("*" * 15)
#     elif i == 5:
#         print("*" * 10)
#     elif i < 5 or i > 5:
#         print("*" * 1)


# print("*"*15)
# for i in range(1,3):
#     print("*" * 1)
# print("*" * 10)
# for i in range(1,5):
#     print("*" * 1)


# ! Örnek
# isimler = ["Mehmet","Ahmet","Hasan","Selim","Süleyman","Kerem","Enes","Berk"]

# for isim in isimler:
#     if len(isim) > 5:
#         print(isim.upper())



# ! WHİLE DÖNGÜSÜ
notu = 0
while notu < 60:
    print("Öğrenci başarısız")
    notu = int(input("Notunuzu giriniz:"))  
print("öğrenci başarılı oldu.")






