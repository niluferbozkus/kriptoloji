import random

def randomvigenere():
    alfabe= ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
    
    vigenere_square=[]     
    
    for i in range(len(alfabe)): 
        for j in range(len(alfabe)):
            x = random.randrange(len(alfabe))  #0 dan alfabe uzunluğuna kadar random bir sayı alıyoruz
            vigenere_square.append(alfabe[x])  #alfabenin x. indexindeki harfi vigenere_square listemize ekliyoruz.
            alfabe.pop(x)       # listeye eklediğimiz harfi alfabe listesinden çıkarıyoruz ki aynı satırda iki defa olmasın.              
        
        alfabe= ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
        print(*vigenere_square)
        vigenere_square=[] 

randomvigenere()
