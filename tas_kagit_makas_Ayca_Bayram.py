import random

def tas_kagit_makas_AYCA_BAYRAM():
    print("Merhaba.Bayraminglerin tas kagit makas oyununa hosgeldiniz!")
    print("Bu oyun her tas kagit makas oyununa benzemez. Burada bayraminglerin kurallari gecerlidir! :) \nOyun kurallari sunlardir:\n")

    karakter_1="Burhan Altintop"
    karakter_2="Polat Alemdar"
    karakter_3="Sahika Kocarslanli"
    karakter_4="Bihter Ziyagil"

    kural_1=" 1.Oyunda toplam iki tur kazanan oyunun galibi olacaktir.\n"
    kural_2="2.Oyun 2 kisi oynanacaktir. Sen ve rakibin bilgisayar.\n"
    kural_3="3.Oyuna baslamadan once bir karakter secmelisin. Karakterini belirttigimiz numaralar ile  secebilirsin: \n" + "  1:" + karakter_1 + "\n  2:" + karakter_2 + "\n  3:" + karakter_3 + "\n  4:" + karakter_4 + "\n"
    kural_4="4.Oyuna baslamak icin tas, kagit veya makas yazmalisin. Oyundan cikmak icin 'cikis' yazmalisin. \n"
    kural_5="5.-Tas makasi yener. \n   -Makas kagidi yener. \n   -Kagit tasi yener."

    print (kural_1 , kural_2, kural_3, kural_4, kural_5) #kuralları yazdırdım.

    karakterler=[karakter_1, karakter_2, karakter_3, karakter_4] #karakter listesi
    secim=["tas","kagit","makas","cikis"] #secim listesi
    cevap=["Evet", "Hayir"] #bilgisayar oyuna devam etmek istiyor mu derken kullandık

    #Karakter seçimi yapmasını istiyoruz. Sonra hangi karakteri seçtiğini print edip oyuna başlıyoruz.
    karakter_secim=input("Hangi karakteri secmek istersin: ").strip() #karakter seçmesini istedik.

    while True: #karakter secimi gerçekleşene kadar dönsün
        if karakter_secim == "1":
            karakter=karakterler[0] #karakter listesindeki seçime uygun olan değeri atadık.
            print(karakter + " karakterini sectin yievrum. :) Oyun baslasin.")
            break
        elif karakter_secim == "2":
            karakter=karakterler[1]
            print(karakter + " karakterini sectin. Racona hazir ol! :) Oyun baslasin.")
            break
        elif karakter_secim == "3":
            karakter=karakterler[2]
            print(karakter + " karakterini sectin bobogom, sasirdim! :) Oyun baslasin.")
            break
        elif karakter_secim == "4":
            karakter=karakterler[3]
            print(karakter + " karakterini sectin. Oluyorum anlasana! :) Oyun baslasin.")
            break
        else :
            print("Hatali giris yaptin. Lutfen giris yaparken karakter numaralarini kullaniniz. Tekrar karakter secmeye ne dersin?")
            karakter_secim=input("Hangi karakteri secmek istersin: ")

    oyuncu_galibiyet=0 
    bilgisayar_galibiyet=0 #oyuncu galibiyet ve bilg galibiyet 0 tanımladık oyun başında
    tur_sayac=1 
    oyun_sayac=1 #oyun sayacını ve tur sayacını 1 tanımladık

    while True: #oyunun devam etmesi için gereken döngü

        if bilgisayar_galibiyet == 2 or oyuncu_galibiyet == 2: #eğer bilgisayar ya da oyuncu 2 galibiyete ulaşırsa oyun biter ve yeni oyun isteyip istemediği sorulur
            if bilgisayar_galibiyet > oyuncu_galibiyet: #kimin kazandığını yazdırmak için if oluşturduk.
                print("Bilgisayar kazandi. Ha ha :) Bir sonraki sefere artik...")
            else:
                print(karakter + " kazandi! Tebrikler :)")

            while True:  # Oyuna devam etmek ister misin sorusuna e ve h den başka cevap gelirse diye while ve if oluşturduk
                cevap_1 = input("Oyuna devam etmek ister misin? E/H:").upper().strip()
                if cevap_1 in ("E", "H"):
                    break
                else:
                    print("E veya H secenegini girmeliydiniz. Tekrar girin lutfen...")

            cevap_2 = random.choice(cevap) # bilgisayardan random cevap istedik oyuna devam etme durumunu if içinde sonuclandırdık
            if cevap_1 == "E" and cevap_2 == "Evet":
                print("Bilgisayarin cevabi: " + cevap_2)
                print("Oyun devam ediyor. Hadii devam edelim.")
                oyun_sayac += 1
                tur_sayac = 1
                oyuncu_galibiyet = 0
                bilgisayar_galibiyet = 0
            else:
                print("Bilgisayarin cevabi: " + cevap_2)
                print("Oyunculardan en az biri devam etmek istemedigi icin oyun bitti. Bir dahakine gorusuruz.")
                break

        while True:

            print("--- Oyun " + str(oyun_sayac) + " tur " + str(tur_sayac) + " ---") #oyun sayısı ve tur sayısı yazdırdık.
            oyuncu_cevap=input("Tas, Kagit, Makas ya da Cikis: ").lower().strip() #oyuncudan secim yapmasını istedik ve yazdırdık
            #bilgisayar_cevap=random.choice(secim[0:3]) #bilgdan random secim yapmasını istedik
            #print("Bilgisayar secimi: " + bilgisayar_cevap) #bilgisayarın seçimini yazdırdık.

            if oyuncu_cevap in secim[0:3]: #oyuncu seçimi seçim listesinin içindeyse
                bilgisayar_cevap=random.choice(secim[0:3]) #bilgdan random secim yapmasını istedik
                print("Bilgisayar secimi: " + bilgisayar_cevap) #bilgisayarın seçimini yazdırdık.

                tur_sayac+=1 #tur sayacını artırdık

                if oyuncu_cevap == bilgisayar_cevap: #oyuncu ve bilg seçimi aynı ise
                    print("Bu tur berabere! Hadi devam edelim.")
                    print("Skor-> Bilgisayar: " + str(bilgisayar_galibiyet) + " " + karakter + ": " + str(oyuncu_galibiyet)) #skor yazdırdık.
                    break

                elif oyuncu_cevap == secim[0] and bilgisayar_cevap == secim[1]:
                    print("Ben kazandim! Uzulme " + karakter + " bir gun kazanirsin elbet. :)")
                    bilgisayar_galibiyet+=1 #kim kazanıyorsa onun galibiyetini artırdık.
                    print("Skor-> Bilgisayar: " + str(bilgisayar_galibiyet) + " " + karakter + ": " + str(oyuncu_galibiyet)) #skor yazdırdık.
                    break # içteki while dan çıktık

                elif oyuncu_cevap == secim[0] and bilgisayar_cevap == secim[2]:
                    print(karakter + " kazandin. Sanslisin, bir sonraki turda gorusuruz.")
                    oyuncu_galibiyet+=1
                    print("Skor-> Bilgisayar: " + str(bilgisayar_galibiyet) + " " + karakter + ": " + str(oyuncu_galibiyet))
                    break

                elif oyuncu_cevap == secim[1] and bilgisayar_cevap == secim[0]:
                    print(karakter + " kazandin! Kagit tasi sarar, off gorusecegiz.")
                    oyuncu_galibiyet+=1
                    print("Skor-> Bilgisayar: " + str(bilgisayar_galibiyet) + " " + karakter + ": " + str(oyuncu_galibiyet))
                    break

                elif oyuncu_cevap == secim[1] and bilgisayar_cevap == secim[2]:
                    print("Ben kazandim, makas kagiti keser! " + karakter + " devam edelim.")
                    bilgisayar_galibiyet+=1
                    print("Skor-> Bilgisayar: " + str(bilgisayar_galibiyet) + " " + karakter + ": " + str(oyuncu_galibiyet))
                    break

                elif oyuncu_cevap == secim[2] and bilgisayar_cevap == secim[0]:
                    print("Ben kazandim! " + karakter + " hadii onumuzdeki maclara bakalim.")
                    bilgisayar_galibiyet+=1
                    print("Skor-> Bilgisayar: " + str(bilgisayar_galibiyet) + " " + karakter + ": " + str(oyuncu_galibiyet))
                    break

                elif oyuncu_cevap == secim[2] and bilgisayar_cevap == secim[1]:
                    print("Kazandin " + karakter + " Bazen sen de kazanmalisin. :)")
                    oyuncu_galibiyet+=1
                    print("Skor-> Bilgisayar: " + str(bilgisayar_galibiyet) + " " + karakter + ": " + str(oyuncu_galibiyet))
                    break
                
                break #dıştaki while dan çıktık.

            elif oyuncu_cevap == secim[3] and tur_sayac == 1 and  oyun_sayac == 1: #oyuncu çıkışı seçtiyse
                print("Ilk turdan cikmak istedigine inanamadim. Dalga mi geciyosun :( ")
                return

            elif oyuncu_cevap == secim[3]: #oyuncu çıkışı seçtiyse
                cikis_cevap=input("Cikis yapmak istedigine emin misin? E/H:").upper() # emin olup olmadığını sorduk.
                if cikis_cevap == "E": #cevap evetse
                    print("Kaciyor musun? Saka saka, tekrar oynamak istediginde gorusuruz. O zamana kadar pratik yapmaya devam edelim. :)")
                    return
                else: #cevap hayırsa
                    print("Oley! Oyun devam ediyor.")
                    break

            else: #oyuncunun seçimi yanlışsa
                print ("Yanlis bir secim yaptiniz. Lutfen Tas, Kagit, Makas yada Cikis'tan birini seciniz.")
                break
                #oyuncu_cevap=input("Tas, Kagit, Makas ya da Cikis: ").lower() #tekrar seçim yapmaya gönderdik.
 
tas_kagit_makas_AYCA_BAYRAM()

