import random

randomSayi = (random.randint(1,100))
rakam = randomSayi
hak = int(input("Hak Sayısı Adedi: "))


hak1 = hak

x = 0

end = "Oyun Bitti, Harcayacak Hak Kalmadı :))" 

while hak >= 0:
    print(f" Mevcut Hak : {hak} ".center(30,"*"))
    if hak == 0:
        print(end)
        break
    soru = int(input("Bir Tahmin Giriniz: "))
    if soru == rakam:
        print("Doğruuuu!! Puan",(100 * hak) / hak1 )
        break
    elif soru != rakam and hak > 0:
        if soru > rakam:
            print(" İpucu: Aşağı ".center(100,"*"))
        elif soru < rakam:
            print(" İpucu: Yukarı ".center(100,"*"))
        hak -= 1
        
