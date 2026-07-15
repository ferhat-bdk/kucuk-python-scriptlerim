from random import randint


while True:
    i = 0
    while True: # Temel Sorular
        try:

            Tkatilan = int(input("Toplam Kaç Kişi Katılacak: "))
            sira = int(input(("Kaçıncı Sırada Olmak İstesiniz: ")))
            break

        except ValueError:
            print("Doğru Bir Değer Giriniz.")


    while True: # Sonuç
        seçenek = randint(1, int(Tkatilan))
        i += 1

        if seçenek == sira:

            print(f"{i}. Sırada Çekilişi Kazandınız.")
            break

    rst = input("Tekrar? (e/h) :").lower()

    if rst == "e":
        continue
    elif rst == "h":
        break
