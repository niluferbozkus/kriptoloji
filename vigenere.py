def vigenere(metin,anahtar):
    
    alfabe= ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
    
    metin = metin.replace(" ","").lower()
    anahtar=anahtar.lower()
    
    metin = list(metin)
    anahtar = list(anahtar)
    
    anahtar_index = []
    metin_index = []
    new_anahtar_index=[]   
   
    for i in range (len(anahtar)):
        anahtar_index.append(alfabe.index(anahtar[i]))  
        
    for j in range (len(metin)):
        metin_index.append(alfabe.index(metin[j]))     
        new_anahtar_index.append(anahtar_index[j % len(anahtar)])     
   
    for x in range(len(metin)):
        new_anahtar_index[x] = int(new_anahtar_index[x]) + int(metin_index[x])
        #şifre.append(alfabe[new_anahtar_index[x]])

    print("\nŞifrelenmiş metniniz: ")
    for i in new_anahtar_index:
        print(alfabe[i % 29],end="")
