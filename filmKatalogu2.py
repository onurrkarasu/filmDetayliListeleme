filmler=[
    ("Kara Korsanın Laneti",1987,8.2,"Korku"),
    ("Sineğin İntikamı",2987,1.2,"Belgesel"),
    ("Yılan Rüzgarı",2009,5.2,"Korku")
]

def filmleriListele(filtre=None,deger=None):
    for film in filmler:
        if not filtre and not deger:
            print("Filmin Adı  :  {}({}) ------ : {} ------- Tür: {}".format(film[0],film[1],film[2],film[3]))
        elif filtre=="Film Adı":
            if deger.lower() == film[0].lower():
                print("Filmin Adı  :  {}({}) ------ : {} ------- Tür: {}".format(film[0], film[1], film[2], film[3]))
        elif filtre=="Yapım Yılı":
            if deger == film[1]:
                print("Filmin Adı  :  {}({}) ------ : {} ------- Tür: {}".format(film[0], film[1], film[2], film[3]))
        elif filtre=="Imdb":
            if deger == film[2]:
                print("Filmin Adı  :  {}({}) ------ : {} ------- Tür: {}".format(film[0], film[1], film[2], film[3]))
        elif filtre=="Tür":
            if deger.lower() == film[3].lower():
                print("Filmin Adı  :  {}({}) ------ : {} ------- Tür: {}".format(film[0], film[1], film[2], film[3]))
    print("\n")
    input("Devam etmek için bir tuşa basın.")


menu="""
        Filmi Hangi kıstasa Göre aramak İsterseniz ?
        
        [1] Film Adı
        [2] Yapım Yılı
        [3] Imdb Puanı
        [4] Türü
        [5] Hepsini Getir
        [0] Çıkış Yap
    """
while True:
    print(menu)
    secim=int(input("Lütfen Seçiminizi Yapınız : !!!    "))

    if secim==1:
        mesaj="Film Adını girin : "
        filtre="Film Adı"
    elif secim==2:
        mesaj="Yapım yılını girin : "
        filtre="Yapım Yılı"
    elif secim==3:
        mesaj="Imdb Puanını girin : "
        filtre="Imdb"
    elif secim==4:
        mesaj="Film Türünü girin : "
        filtre="Tür"

    if secim==1 or secim==4:
        deger=input(mesaj)
        filmleriListele(filtre,deger)
    elif secim==2:
        deger=int(input(mesaj))
        filmleriListele(filtre,deger)
    elif secim==3:
        deger=float(input(mesaj))
        filmleriListele(filtre,deger)
    elif secim==5:
        filmleriListele()
    elif secim==0:
        quit()
