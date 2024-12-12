cikis = 0
import time
from tabulate import tabulate
import csv
ogrliste = []
with open("data.csv","r") as ogrdata:
    satirlar = ogrdata.readlines()
    for satir in satirlar:
        ogrliste.append(satir.strip().split(";"))
        
def ogrnoarama():
    
    try:
        no = input("Aramak istediğiniz öğrencinin numarasını giriniz : ")
    except Exception:
        print("Hatalı değer girişi yapıldı. Tekrar Deneyiniz!")
        ogrnoarama()
    ogrno = []
    
    with open("data.csv","r") as ogrdata:
        satirlar = ogrdata.readlines()
        
        for satir in satirlar[1:]:
            var = True
            numara = satir.split(";")[0]
            
            if numara == no:
                var = False
                ogrno.append(satir.split(";"))
                basliklar = satirlar[0].split(";")
                print(tabulate(ogrno,headers=basliklar,tablefmt="grid"))
                time.sleep(1)
                break
                
        if var:
            print("\nAradğınız Değer listede yok")
            time.sleep(0.50)
            
def alanarama():
    
    try:
        alan = input("Aramak istediğiniz alanı giriniz (AU/AT/EKB/PER/DK/OK/KCK/K_KKT/DCK/D_KKT) : ").upper()
    except Exception:
        print("Hatalı değer girişi yapıldı. Tekrar deneyiniz!")
        alanarama()
    with open("data.csv","r") as ogrdata:
        okuma = csv.DictReader(ogrdata,delimiter=";")
        veriler = list(okuma)
        liste = []
        if alan in veriler[0]:
            basliklar = ["Öğrenci", alan]
            for veri in veriler:
                liste.append([veri["Ogrenci"], veri[alan]])
            print(tabulate(liste,headers=basliklar,tablefmt="grid"))
            time.sleep(1)
        else:
             print("\nAlan bulunamadı lütfen geçerli bir alan giriniz")
             time.sleep(0.50)
             
             
def menu():
    global cikis
    try:
        islem = int(input("\n\nÖğrenci notları bilgi sistemi\n1-)Ögrenci numarasına göre arama\n2-)Belirli alana göre arama\n3-)Çıkış\nYapmak istediğiniz işlemi seçiniz (1/2/3): "))
    except Exception:
        print("---------------------------------\nHatalı değer girişi yapıldı")
        time.sleep(0.55)
        menu()
    match islem:
        case 1:
            ogrnoarama()
        case 2:
            alanarama()
        case 3:
            cikis = 3
        case _:
            print("---------------------------------\nHatalı değer girişi yapıldı")
            time.sleep(0.55)
            menu()
while cikis !=3:
    menu()