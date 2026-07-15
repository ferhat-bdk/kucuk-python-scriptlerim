import random
import datetime

status = ["Açık","Kapalı","Fitrelenmiş"]

print("SENTINEL-X  Başlatılıyor....")

operator_name = input("Kullanıcı İsim Bilgisi: ")

while True:
    try:
        security_level = int(input("Güvenlik Seviyesi (1-5) : "))
        if 1 <= security_level <= 5:                                         #security_level >= 1 and security_level <= 5:   -Yeni Öğrendim
            break
        else:
            print("Böyle bir değer yok")
    except ValueError:
        print("Doğru Bir Değer Giriniz..")



print(f"Merhaba {operator_name}, Güvenlik yetki seviyesi {security_level}")

def ScanPort(target_port):
    status1 = random.choice(status)
    with open("logs.txt","a") as file:
        file.write(f"\n{target_port} Numaralı Port Tarandı. Durum {status1}. Taranma Zamanı : {datetime.datetime.now().time()}")       
        
    print(f" {target_port} Numaralı Port Tarandı..")
"""
def ScanPort():                                     # İf above  working, then don't touch this
    global activity_log
    activity_log.append("Port Taraması Yapıldı")
    print("Tamamlandı..")n =
"""

def VisitTheLogs():
    
    if security_level >= 3:
        with open("logs.txt","r") as file:
            print(file.read())
    elif security_level < 3:
        print("Düşük Güvenlik Seviyesinde Erişim Sağlanamaz..")
    return
def CloseSystem():
    return (f"Sistem Kapatılıyor | Güvenli Günler {operator_name} ")

def delete_log_history():
    with open("logs.txt","w") as file:
        file.write("")
        file.close()
        print("Log Geçmişi Silindi..")

while True:
    


    print("1- Port Taraması \n2- Logları İncele \n3- Sistemi Kapat \n4- Log Geçmişini Sil")
    islem = int(input("Yapmak istenilen işlem: "))  
    


    if islem == 1:
        #
        while True:
            try:
                result = int(input("Sorgulamak İstediğiniz Port: "))
            
                if result <= 60000 and result >= 1:
                    ScanPort(result)
                    break
                else:
                    print("1 ile 60.000 arasında bir port numarası giriniz..")
            except ValueError:
                print("Doğru Bir Değer Giriniz..")

    elif islem == 2:
        VisitTheLogs()
        continue
    elif islem == 3:
        print(CloseSystem())
        break
    elif islem == 4:
        print(delete_log_history())
        pass
    else:
        print("Hatalı Seçim, Menüye Yönlendiriliyorsunuz...")
        continue
    
