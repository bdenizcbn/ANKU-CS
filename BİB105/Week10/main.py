cikis = 0
import os
import re
import time
from tabulate import tabulate

# Dosyaya Veri Aktarımı
ogrliste = []
# Eğer dosya yoksa, örnek verilerle oluştur
if not os.path.exists("ogrenci.txt"):
    with open("ogrenci.txt", "w") as ogrdosya:
        ogrdosya.write("OgrNO,Ad,Soyad,AraSinav\n")
        ogrliste = [
            {"OgrNO": "01010101", "Ad": "Dominic", "Soyad": "Solanke", "AraSinav": "85"},
            {"OgrNO": "01010102", "Ad": "Dejan", "Soyad": "Kulusevski", "AraSinav": "90"},
            {"OgrNO": "01010103", "Ad": "Pedro", "Soyad": "Porro", "AraSinav": "100"},
        ]
        # Örnek verileri dosyaya yaz
        for ogrbilgi in ogrliste:
            dosya_yazilacak_deger = f"{ogrbilgi['OgrNO']},{ogrbilgi['Ad']},{ogrbilgi['Soyad']},{ogrbilgi['AraSinav']}\n"
            ogrdosya.write(dosya_yazilacak_deger)
else:
    # Dosya varsa içeriği oku ve listeyi oluştur
    with open("ogrenci.txt", "r") as ogrdosya:
        satirlar = ogrdosya.readlines()
        for satir in satirlar[1:]:  # Başlık satırını atla
            veri = satir.strip().split(",")
            ogrliste.append({"OgrNO": veri[0], "Ad": veri[1], "Soyad": veri[2], "AraSinav": veri[3]})

# Giriş doğrulama için düzenli ifadeler
ogrno_oruntu = r"^\d{8}$"
metin_oruntu = r"^[A-Za-zÇçĞğİıÖöŞşÜü ]+$"
not_oruntu = r"^(0|0\d+|100|[1-9]\d?)(\.\d+)?$"

# Yeni bir öğrenci ekleme fonksiyonu
def ogrekle():
    global ogrliste
    # Kullanıcıdan öğrenci bilgilerini al
    ogrno = input("Öğrencinin numarasını giriniz (örn : 24050188) : ").strip()
    ograd = input("Öğrencinin adını giriniz (örn : Deniz) : ").strip()
    ogrsoyad = input("Öğrencinin soyadını giriniz (örn : Çoban) : ").strip()
    ogrnot = input("Öğrencinin notunu giriniz (örn : 89.96) : ").strip()

    degerler = [ogrno, ograd, ogrsoyad, ogrnot]

    # Girişler geçerliyse veriyi ekle
    if (re.match(ogrno_oruntu, degerler[0]) and 
        re.match(metin_oruntu, degerler[1]) and 
        re.match(metin_oruntu, degerler[2]) and
        re.match(not_oruntu, degerler[3])):
        with open("ogrenci.txt", "a") as ogrdosya:
            dosya_yazilacak_deger = f"{ogrno},{ograd},{ogrsoyad},{ogrnot}\n"
            ogrdosya.write(dosya_yazilacak_deger)
        # Listeye ekle
        ogrliste.append({"OgrNO": degerler[0], "Ad": degerler[1], "Soyad": degerler[2], "AraSinav": degerler[3]})
        print("Veriler başarıyla eklendi")
        time.sleep(0.25)
    else:
        print("İfadelerin içinde hatalı değer var")

# Öğrenci silme fonksiyonu
def ogrsil():
    ogryazdir()  # Mevcut verileri yazdır
    try:
        silinecekdeger = input("Silinecek öğrencinin Numarasını veya Adını veya Soyadını giriniz : ")
    except Exception:
        print(f"Bir hata oluştu: {e} Yönetici ilgileniyor!")
        time.sleep(0.25)
        menu()

    try:
        # Dosyayı oku ve silinecek veriyi atla
        with open("ogrenci.txt", "r") as file:
            
            dosyadaki_satirlar = file.readlines() # dosyayı okuma
            silmesayi = 0
            
            with open("ogrenci.txt", "w") as dosya:
                dosya.write("OgrNO,Ad,Soyad,AraSinav\n")
                for satir in dosyadaki_satirlar[1:]:
                    silme = True
                    veri = satir.split(",")
                    # Eşleşme varsa satırı yazma
                    for deger in veri:
                        if deger.strip() == silinecekdeger.strip():
                            silme = False
                            silmesayi = 1
                    if silme:
                        dosya_yazilacak_deger = f"{veri[0]},{veri[1]},{veri[2]},{veri[3]}"
                        dosya.write(dosya_yazilacak_deger)
                if silmesayi == 1:
                    print(f"'{silinecekdeger}' içeren satır başarıyla silindi!")
                    time.sleep(0.25)
                else:
                    print(f"'{silinecekdeger}' içeren bir satır yoktur")
                    time.sleep(0.25)

    except FileNotFoundError:
        print("Dosya mevcut konumda yer almamaktadır! Yönetici ile iletişime geçiniz.")
    except Exception as e:
        print(f"Bir hata oluştu: {e} Yönetici ilgileniyor!")

# Verileri yazdırma fonksiyonu
def ogryazdir():
    try:
        with open("ogrenci.txt", "r") as file:
            satirlar = file.readlines() #dosyayı oku

            basliklar = satirlar[0].split(",")  # Başlık satırını al
            hatasiz_ogr_veri = []
            hatali_ogr_veri = []

            # Her satırı kontrol et 
            for satir in satirlar[1:]:
                veri = satir.split(",")
                if (re.match(ogrno_oruntu, veri[0]) and 
                    re.match(metin_oruntu, veri[1]) and 
                    re.match(metin_oruntu, veri[2]) and
                    re.match(not_oruntu, veri[3])):
                   hatasiz_ogr_veri.append(veri)
                else:
                    hatali_ogr_veri.append(veri)

            print("Hatasız Veri Seti")
            print(tabulate(hatasiz_ogr_veri, headers=basliklar, tablefmt="grid"))

            #hatalı_ogr_veri listesi boş değilse yazdır, boşsa yazdırma
            if hatali_ogr_veri:
                print("Hatalı Veri Seti")
                print(tabulate(hatali_ogr_veri, headers=basliklar, tablefmt="grid"))

    except FileNotFoundError:
        print("Dosya mevcut konumda yer almamaktadır! Yönetici ile iletişime geçiniz.")
    except Exception as e:
        print(f"Bir hata oluştu: {e} Yönetici ilgileniyor!")
    time.sleep(1.50)

# Menü
def menu():
    global cikis
    try:
        islem = int(input("\n\nÖğrenci notları bilgi sistemi\n1-)Ögrenci verisi ekle\n2-)Öğrenci verisi sil\n3-)Öğrenci verilerini yazdır\n4-)Çıkış\nYapmak istediğiniz işlemi seçiniz (1/2/3/4): "))
    except Exception:
        print("---------------------------------\nHatalı değer girişi yapıldı")
        time.sleep(0.55)
        menu()
    match islem:
        case 1:
            ogrekle()
        case 2:
            ogrsil()
        case 3:
            ogryazdir()
        case 4: 
            cikis = 4
        case _:
            print("---------------------------------\nHatalı değer girişi yapıldı")
            time.sleep(0.55)
            menu()

# Program Döngüsü
while cikis != 4:
    menu()
