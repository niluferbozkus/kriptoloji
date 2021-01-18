import math 

sifre = input("Şİfrelemek istediğiniz metni girin: ").lower()  #şifreküçük harflerden oluşsun

text = sifre.replace(" ","")  #şifredeki kelimeler arası boşluk olmasın.

x = len(text)

m = math.ceil(math.sqrt(x))  #textin uzunluğu tamkare değilse karekökten çıkan sayı bir üste yuvarlansın

liste = []

for i in range(m):    # matrisin satır sayısına göre harfler yukarıdan aşağı sıralansın
    for j in range(m): 
        if (m*j + i)  < len(text):              
            liste.append(text[m*j + i])      #oluşan matristen harfler satır sırasıyla alınsın ve listeye eklensin

sifrelitext = str()   #oluşan listedeki karekterler tek bir kelime gibi duracak şekilde birleştirilsin
for b in liste:
    sifrelitext = sifrelitext + str(b)

print(sifrelitext)
