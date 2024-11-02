liste = []

while true:
   sayı = input("bir sayı girin (çıkmak için q) : ")
   if sayı == "q":
        break
    sayı = int(sayı)
    if sayı not in liste:
        print("girilen sayı dizide var")
    else:
        dizi.append(sayı)
