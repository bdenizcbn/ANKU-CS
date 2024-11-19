araclar = {"mercedes":{"araç türü":"tır","stok durumu":"var","kira durumu":"kiralanabilir"},"volvo":{"Araç türü":"tır","Stok durumu":"var","Kira durumu": "kiralanabilir"}}

def aracgoruntelemehepsi():
    print(araclar)    
def aracgoruntelememodel(model):
    print(araclar[model])
    
def arackiralama(model):
    araclar[model]["kira durumu"] = "kiralanamaz"
    araclar[model]["stok durumu"] = "yok"
    print("aracı kiraladınız")
    print("aracın yeni durumu",araclar[model])

def aracekleme(model,tür,stokdurumu,kiradurumu):
    araclar.update({model: {"araç türü":tür,"stok durumu":stokdurumu,"kira durumu":kiradurumu} })
    
def araciade(model):
    araclar[model]["kira durumu"] = "kiralanabilir"
    araclar[model]["stok durumu"] = "var"
    print("aracı iade ettiniz")
    print("aracın yeni durumu",araclar[model])

def aracsil(silinecekmodel):
    araclar.pop(silinecekmodel)
    print("araç silinmiştir")
    print("yeni liste")
    print(araclar)
secim = 0
while secim !=6:
    secim = int(input(("1-)Araç Listesini görüntüle \n 2-)Araç kiralama\n 3-)Araç İade \n 4-)Yeni araç ekleme \n 5-)araç silme \n6-)Çıkış\n İşlem seçiniz (1/2/3/4/5/6) : ")))
    match secim:
        case 1:
            goruntule = input("hepsini mi görüntülemek istiyorsunuz modele göremi (hepsi/model): ").lower()
            if goruntule == "hepsi":
                aracgoruntelemehepsi()
            elif goruntule == "model":
                model = input("hangi modeli görüntülemek istiyorsunuz : ")
                aracgoruntelememodel(model)
        case 2:
            arac = input("hangi aracı kiralamak istiyorsunuz : ")
            arackiralama(arac)
        case 3:
            iade = input("Hangi aracı iade edeceksiniz : ")
            araciade(iade)
        case 4:
            model = input("Aracın modeli : ").lower()
            tür = input("Aracın türü : ")
            stokdurumu = input("Stok durumu (var/yok) : ")
            kiradurumu = input("kira durumu (kiralanabilir/kiralanamaz) :")
            aracekleme(model,tür,stokdurumu,kiradurumu)
        case 5:
            model = input("hangi modeli silmek istiyorsunuz : ")
            aracsil(model)
        case 6:
            break