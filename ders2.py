

# ! Listeler

cities = ["İstanbul","Ankara","İzmir","Bursa","Sivas","Samsun","Eskişehir"]

# print(type(cities))
# print(cities[0])
# print(cities[len(cities)-1])
# print(cities[-1])
# print(cities[2:6])


#! Listenin Sonuna eleman eklemek için
# cities.append("Denizli")
# print(cities)

#! Eklemek İçin
# cities.insert(1,"Sakarya")
# print(cities)


#! Kaldırmak için
# cities.pop(0)
# print(cities)

#? Uygulama
# dersler = ["mat","kimya","biyoloji","tarih","fizik"]


# ! Uygulama
dersler = ["mat",["fizik","kimya"],"ingilizce","türkçe"]

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


#! TUPLE KULLANIMI(değişime kapalı veriler)

dizi = ("ankara","berlin","londra","tahran","tokyo","roma")
# print(type(dizi))
# dizi[3] = "paris"

dizi = list(dizi)
print(type(dizi))
dizi[3] = "paris"
print(dizi)

dizi = tuple(dizi)
print(type(dizi))

