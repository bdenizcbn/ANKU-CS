import random
def seviye(zorluk):
    if zorluk == "kolay":
        return (random.randint(1,5),random.randint(1,5))
    elif zorluk == "orta":
        return (random.randint(5,10),random.randint(5,10))
    elif zorluk == "zor":
        return (random.randint(10,15),random.randint(10,15))
    elif zorluk == "çok zor":
        return (random.randint(15,20),random.randint(15,20))
seçim =0
while (seçim != "-1"):
    seçim = input("kolay: (1,5) arasında\nOrta (5,10) arasında\nZor (10,15) arasında\nÇok zor (15,20) arasında\nçıkmak için -1 yazınız : ").lower()
    if seçim == "-1":
        break
    dogrusayisi = 0
    sorusayi = 1
    while (dogrusayisi<5):
        sayi1 ,sayi2 = seviye(seçim)
        sonuc = sayi1*sayi2
        
        kullanıcıcevap = int(input(f"{sorusayi}. soru {sayi1} x {sayi2} : "))
        if kullanıcıcevap == sonuc:
            dogrusayisi +=1
            print("doğru bilme sayınız : ",dogrusayisi)
            sorusayi +=1
        else:
            print("cevap yanlış doğru sayınız sıfırlanıyor")
            dogrusayisi = 0
        devam = input("çıkış için -1 , devam etmek istiyorsanız herhangi bir şey yazınız : ")
        if devam == "-1":
            seçim = "-1"
            break
    if dogrusayisi == 5:
        print("Tebrikler! 5 doğru cevap verdiniz")