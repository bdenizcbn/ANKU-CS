import random
import time
puan = 0
kazanmasayisi = 0
kaybetmesayisi = 0
cikis = 0
def zar():
    global toplam
    toplam = 0
    zar1 = random.randint(1,6)
    zar2 = random.randint(1,6)
    toplam = zar1 +zar2
    time.sleep(0.50)
    print("---------------------------------")
    print(f"1.zar : {zar1} , 2.zar : {zar2}")
    

def kontrol():
    global toplam
    global puan
    global kazanmasayisi
    global kaybetmesayisi
    if toplam in (7,11):
        print(f"Attığınız zar {toplam} olduğu için Kazandınız!")
        kazanmasayisi += 1
    elif toplam in (2,3,12):
        print(f"Attığınız zar {toplam} olduğu için Kaybettiniz")
        kaybetmesayisi +=1
    elif toplam in (4,5,6,8,9,10):
        print(f"Attığınız zar {toplam} (bu sizin puanınız olur)")
        puan += toplam 
        print(f"Kazanmak için aynı zarı atana kadar tekrar atın (Eğer 7 atarsanız kaybedersiniz)")
        tekrar()
        
def tekrar():
    global toplam
    global puan
    global kazanmasayisi
    global kaybetmesayisi
    try:
        tkrdevam = input("Tekrar zar atmak istiyormusunuz? (e/h) : ")
    except Exception:
        print("hatalı değer girişi yapıldı")
        tekrar()
    match tkrdevam:
        case "e":
            print("Zar Atılıyor...")
            time.sleep(0.50)
            zar()
            if toplam == puan:
                print(f"Aynı zarı attığınız için Kazandınız!")
                kazanmasayisi += 1
                puan = 0
            elif toplam == 7:
                print(f"7 attığınız için Kaybettiniz!")
                kaybetmesayisi +=1
                puan = 0
            else:
                print(f"{toplam} Attınız")
                tekrar()
        case "h":
            yazdirma()
        case _:
            print("hatalı değer girişi yapıldı")
            tekrar()

def yazdirma():

    print(f"Kazanma sayınız : {kazanmasayisi} \nKaybetme sayınız : {kaybetmesayisi} \nSistemden çıkılıyor...")
    time.sleep(0.50)
    global cikis
    cikis = 1

def main():
    try:
        baslama = input("oynamak istiyormusunuz (e/h) : ")
    except Exception:
        print("hatalı değer girişi yapıldı")
        main()
    match baslama:
        case "e":
            zar()
            kontrol()
        case "h":
            yazdirma()
            global cikis
            cikis = 1
        case _:
            print("hatalı değer girişi yapıldı")
            main()
while cikis != 1:
    main()
