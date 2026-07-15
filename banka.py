
import datetime

acc = {
    "32412421" : {
        "Adı" : "Ferhat",
        "Soyadı" : "Budak",
        "D.T" : "2002",
        "Mail" : "ferhatbudak075@gmail.com",
        "Şifre" : "Abc!23",
        "Bakiye" : 0,
        "EkBakiye" : 0
    },
    "32412422" : {
        "Adı" : "Ali",
        "Soyadı" : "Veli",
        "D.T" : "2001",
        "Mail" : "ali1001@gmail.com",
        "Şifre" : "Abc!2423",
        "Bakiye" : 0,
        "EkBakiye" : 0

    }
}

def Cashİn(cash,userID):
    """
    Tanim: Para Girişi
    """
    global acc
    return cash + (acc[userID]["Bakiye"])


def CashOut(cash,userID):
    """
    Tanim: Para Çikişi
    """
    global acc
    return acc[userID]["Bakiye"] - cash



def Borc(miktar,userID):
    """
    Tanim: Ek Bakiye
    """
    global acc
    return miktar + (acc[userID]["EkBakiye"])

while True:
    

    while True:

        
        print(datetime.datetime.now())
        userİD = input("İD Giriniz: ")
        passwd = input("Şifrenizi Giriniz: ")

        if userİD == "32412421" :
            if passwd == "Abc!23":
                print("Hoş Geldiniz")
                break
            elif passwd != "Abc!23":
                print("Şifre Hatalı, Tekrar Deneyiniz")
        elif userİD != "32412421":
            print("İD Hatalı, Tekrar Deneyiniz")
            continue

        else:
            print("Kullanıcı Tanınamadı")

    while True:

        print(" Hoş Geldiniz ".center(20,"-"))
        print("1- Ana Menü \n2- Bakiye Çekme \n3- Ek Bakiye Başvuru \n4- Bakiye Yatırma \n5- Bakiye Sorgu \n6- Çıkış")
        print(" ".center(21,"-"))
        prms = int(input(" Bir Değer Giriniz: "))

        if prms == 1:
            continue
        if prms == 2:
            miktar = int(input("Çekilecek Tutar: "))
            
            if miktar <= acc["32412421"]["Bakiye"]:
                acc["32412421"]["Bakiye"] = CashOut(miktar, "32412421")
                print(f"Paranızı Çektiniz, Güncel Bakiyeniz: {acc["32412421"]["Bakiye"]}")
                continue
            elif miktar > acc["32412421"]["Bakiye"]:
                print("Bakiye Yetersiz!")
                EkB = input("Borç İster Misiniz? (e/h): ")


                if EkB == "e" or EkB == "E":

                    tutar = int(input("Borç İstenilen Tutar: "))
                    acc["32412421"]["EkBakiye"] = Borc(tutar, "32412421")

                    print("İşlem başarılı, Ana menüye yönlendiriliyorsunuz..")
                else:
                    continue

        if prms == 4:
            miktar = int(input("Yatırılacak Tutar: "))
            acc["32412421"]["Bakiye"] = Cashİn(miktar, "32412421")
            print(f"Paranızı Yatırdınız, Güncel Bakiyeniz: {acc["32412421"]["Bakiye"]}")
            continue
        if prms == 3:
            tutar = int(input("Borç İstenilen Tutar: "))
            acc["32412421"]["EkBakiye"] = Borc(tutar, "32412421")
            print("İşlem başarılı, Ana menüye yönlendiriliyorsunuz..")
            continue
        
        if prms == 5:
            print(f"Bakiye: {acc['32412421']['Bakiye']} | Ek Bakiye: {acc['32412421']['EkBakiye']}")
            continue
        
        if prms == 6:
            break
