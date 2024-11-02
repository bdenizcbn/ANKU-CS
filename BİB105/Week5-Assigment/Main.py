def toplama(dizi):
    tpm = 0
    for i in range(len(dizi)):
        tpm += dizi[i]
    return tpm
def cikarma(dizi):
    dizi.sort(reverse=True)
    sayi= 1
    ckr =dizi[0]
    while sayi < len(dizi):
        ckr -= dizi[sayi]
        sayi +=1
    return ckr
def carpma(dizi):
    crp = 1
    for i in range(len(dizi)):
        crp *= dizi[i]
    return crp
def bolme(dizi):
    if 0 in dizi:
        return "bir sayı sıfıra bölünemez"
    else :
        dizi.sort(reverse=True)
        sayi = 1
        blm = dizi[0]
        while sayi <len(dizi):               
            blm /= dizi[sayi]
            sayi+= 1 
        return blm
print("işlem seçiniz :")
print("1.toplama")
print("2.çıkarma")
print("3.çarpma")
print("4.bölme")
print("5.faktoriyel")
print("6.dizi içerisinde arama")
    
seçim = input("seçiniz : (1/2/3/4/5/6/q) : ")
#FAKTORİYEL HESAP
if seçim == "5":
    faksayi = int(input("faktoriyelini almak istediğiniz sayıyı giriniz : "))
    if faksayi == 0:
        print("faktoriyel sonuc : 1")
    elif faksayi>0:
        carp = 1
        while faksayi>0:
            carp *= faksayi
            faksayi -= 1
        print("faktoriyel sonuc : ", carp )
    else:
        print("geçersiz sayı girdiniz")
else:
    while True:
        seçim in ('1','2','3','4','6','q')
        if seçim == "q" :
            break
        try:
            dizi = []
            sayi =int(input("kaç sayı gireceksiniz : "))
            for i in range(sayi):
                dizi.append(float(input('Sayıyı giriniz : ')))
        except ValueError:
            print("geçersiz giriş. bir sayı giriniz:")
            continue
        if seçim == '1':
            print("toplam : ",toplama(dizi))
        elif seçim == '2' :
            print("çıkarma sonucu:" , cikarma(dizi))
        elif seçim == '3' :
            print("çarpım sonucu : ",carpma(dizi))
        elif seçim == '4' :
            print("bölüm sonuç : ", bolme(dizi))
        elif seçim == '6' :
            aramasayi = float(input("aramak istediğiniz sayıyı giriniz : "))
            if aramasayi in dizi:
                print(f"{aramasayi} dizide bulundu.")
            else:
                print(f"{aramasayi} dizide bulunamadı.")
        islemdevam = input("işleme devam ediyor muyuz? (e/h)")
        if islemdevam == "h" :
            break
        elif islemdevam =="e" :
            continue
        else:
            print("geçersiz giriş")