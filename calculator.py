# ! Hesap Makinesi Örneği


giris = f"""
1 Topla
2 Çıkar
3 Çarp
4 Böl
5 Üssünü Hesapla
6 Karekökünü Hesapla
Q Exit
"""

print(giris)

while True:
    import math
    soru = (input("Yapmak istediğiniz işlemi seçin: "))
    

    if soru=="1":
        s1 = int(input("First Number: "))
        s2 = int(input("Second Number: "))
        answer = s1+s2
        print(f"Result : {answer}")

    elif soru=="2":
        n1 = int(input("First Number: "))
        n2 = int(input("Second Number: "))
        if n1>=n2:
            answer= n1-n2
            print(f"Result: {answer}")
        elif n2>n1:
            question=input("Your result gonna be negative are you sure: ")
            if question=="yes":
                answer=n1-n2
                print(f"Result= {answer}")
            elif question=="no":
                continue

    elif soru=="3":
        n1=float(input("First Number: "))
        n2=float(input("Second Number:"))

        answer=n1*n2
        print(f"Result: {answer}")

    elif soru=="4":
        n1=float(input("First Number: "))
        n2=float(input("Second Number: "))
        answer=n1/n2
        answer=str(answer)
        answer=answer.strip(".0")
        print(f"Result: {answer}")

    elif soru=="5":
        n1=int(input("First Number: "))
        n2=int(input("Second Number: "))
        answer=n1**n2
        print(f"Result: {answer}")

    elif soru=="6":
        n1=float(input("Number: "))
        answer=math.sqrt(n1)
        
        print(f"Result: {answer}")
    elif soru=="q":
        print("Çıkış yapılıyor...")
        break
