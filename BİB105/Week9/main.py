import re

# Email kontrol fonksiyonu
def emailkontrol(email):
    # Email için regex deseni
    mail_redex = r"^[a-zA-Z0-9ğüşöçıİĞÜŞÖÇ._%+-]+@[a-zA-Z0-9ğüşöçıİĞÜŞÖÇ.-]+\.[a-zA-ZğüşöçıİĞÜŞÖÇ]{2,}$"
    # Regex kontrolü lambda fonksiyonu
    email_kontrol_lambda = lambda email: re.match(mail_redex, email)
    # Eğer geçerli bir email ise True, değilse False döner
    return bool(email_kontrol_lambda(email))

# İsim kontrol fonksiyonu
def namekontrol(isim):
    # İsim için regex deseni
    isim_redex = r"^[a-zA-ZığüşöçİĞÜŞÖÇ]+$"
    # Regex kontrolü lambda fonksiyonu
    isim_kontrol_lambda = lambda isim: re.match(isim_redex, isim)
    # Eğer geçerli bir isim ise True, değilse False döner
    return bool(isim_kontrol_lambda(isim))

# Soyisim kontrol fonksiyonu
def soyisimkontrol(soyisim):
    # Soyisim için regex deseni
    soyisim_redex = r"^[a-zA-ZığüşöçİĞÜŞÖÇ]+$"
    # Regex kontrolü lambda fonksiyonu
    soyisim_kontrol_lambda = lambda soyisim: re.match(soyisim_redex, soyisim)
    # Eğer geçerli bir soyisim ise True, değilse False döner
    return bool(soyisim_kontrol_lambda(soyisim))

# Telefon numarası kontrol fonksiyonu
def numarakontrol(phone):
    # Telefon numarası için regex deseni
    phone_redex = r"^\+90 \d{3} \d{3} \d{4}$"
    # Regex kontrolü lambda fonksiyonu
    phone_kontrol_lambda = lambda phone: re.match(phone_redex, phone)
    # Eğer geçerli bir telefon numarası ise True, değilse False döner
    return bool(phone_kontrol_lambda(phone))

# Öğrenciler listesi
ogrenciler = [
    {"name": "Deniz", "surname": "Çoban", "email": "Deniz.Çoban@example.com", "phone": "+90 531 987 6543", "scores": [77, 84, 91]},
    {"name": "Rafa", "surname": "Silva", "email": "Rafa.Silva@example.com", "phone": "+90 554 321 4567", "scores": [85, 88, 92]},
    {"name": "Ciro", "surname": "İmmobile", "email": "Ciro.İmmobile@example.com", "phone": "+90 533 789 1234", "scores": [79, 80, 76]},
    {"name": "Dominic", "surname": "Solanke", "email": "Dominic.Solanke@example.com", "phone": "+90 546 222 3333", "scores": [91, 93, 95]},
    {"name": "Pape", "surname": "Sarr", "email": "Pape.Sarr@example.com", "phone": "+90 533 666 5555", "scores": [77, 81, 79]},
    {"name": "Kylian", "surname": "Mbappe", "email": "Kylian.Mbappe@example.com", "phone": "+90 552 444 2222", "scores": [92, 90, 89]},
    {"name": "Victor", "surname": "Gyökeres", "email": "Victor.Gyökeres@example.com", "phone": "+90 532 876 5432", "scores": [70, 75, 73]},
    {"name": "Gedson", "surname": "Fernandes", "email": "Gedson.Fernandes@example.com", "phone": "+90 555 345 6789", "scores": [88, 90, 85]},
    {"name": "Dejan", "surname": "Kulusevski", "email": "Dejan.Kulusevski@example.com", "phone": "+90 539 234 5678", "scores": [81, 78, 83]},
    {"name": "Vinicius", "surname": "Junior", "email": "Vinicius.Junior@example.com", "phone": "+0 534 987 6543", "scores": [92, 96, 94]}
]

# Öğrenciler üzerinde kontrol yapıyoruz
for ogrenci in ogrenciler:
        
        # İsim kontrolü
        control = False
        while control == False:
            control = namekontrol(ogrenci["name"])  # İsim doğruluğu kontrolü
            if control == False:  # Eğer geçerli değilse, kullanıcıdan yeni isim iste
                yeniisim = input(f"Hata: {ogrenci["name"]} İsimli Öğrencinin İsmi geçersiz, İsim yalnızca harflerden oluşmalı (Türkçe karakterler kabul edilir) : ")
                ogrenci["name"] = yeniisim
        
        # Soyisim kontrolü
        control = False
        while control == False:
            control = soyisimkontrol(ogrenci["surname"])  # Soyisim doğruluğu kontrolü
            if control == False:  # Eğer geçerli değilse, kullanıcıdan yeni soyisim iste
                yenisoyad = input(f"Hata: {ogrenci["surname"]} Soyisimli Öğrencinin Soyisimi geçersiz, Soyisim yalnızca harflerden oluşmalı (Türkçe karakterler kabul edilir) : ")
                ogrenci["surname"] = yenisoyad
        
        # Email kontrolü
        control = False
        while control == False:
            control = emailkontrol(ogrenci["email"])  # Email doğruluğu kontrolü
            if control == False:  # Eğer geçerli değilse, kullanıcıdan yeni email iste
                yeniemail = input(f"Hata: {ogrenci["email"]} Emailli Öğrencinin Emaili geçersiz , Lütfen geçerli bir e-posta adresi girin (örnek: kullanici@example.com) : ")
                ogrenci["email"] = yeniemail
        
        # Telefon numarası kontrolü
        control = False
        while control == False:
            control = numarakontrol(ogrenci["phone"])  # Telefon numarası doğruluğu kontrolü
            if control == False:  # Eğer geçerli değilse, kullanıcıdan yeni telefon numarası iste
                yeniphone = input(f"Hata: {ogrenci["phone"]} Telefon numaralı Öğrencinin Telefon numarası geçersiz. Format: +90 XXX XXX XXXX şeklinde olmalıdır : ")
                ogrenci["phone"] = yeniphone
            
        print("***************************************")
        # Öğrenci bilgilerini yazdırma
        print(ogrenci["name"], ogrenci["surname"])
        print(f"Email: {ogrenci['email']}")
        print(f"Telefon: {ogrenci["phone"]}")
        print(f"Notlar: {ogrenci['scores']}")
        
        # Ortalamayı hesaplama
        total = 0            
        for nots in ogrenci["scores"]:  # Her notu toplama
            total += nots
        ortalama = total / 3  # Toplamı, 3'e bölerek ortalamayı hesapla
        print(f"Ortalama: {ortalama}")