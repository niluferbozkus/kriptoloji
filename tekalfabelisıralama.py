alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"  # 29 harf Türk alfabesi

shift = int(input("Kaç harf kaydırmak istiyorsunuz: "))
shift = shift % 29 #harf sayısından uzun bir sayı girilirse modunu alsın

şifre = input("Şifrelemek istediğiniz metni girin: ").lower()
şifre = şifre.replace(" ","")  #metindeki boşluklar görmezden gelinsin


shifted = alfabe[shift:] + alfabe[:shift] # alfabe[2:] + alfabe[:2]

table = str.maketrans(alfabe, shifted)

encrypted = şifre.translate(table)

print(encrypted)
