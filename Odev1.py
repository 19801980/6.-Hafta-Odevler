##ODEV 1: Sayi Tahmin
##-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
##-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
##-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi 
## sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin 
## ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
##-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
##-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)
##
##Ornek:
##
##         Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece 
##         aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz. 
##         Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)
##
##         Pc'nin tahmini = 89
##         Kullanicinin inputu = -
##         Pc'nin tahmini = 45
##         Kullanicinin inputu = +
##         Pc'nin tahmini = 56
##         Kullanicinin inputu = "Enter"
import random
baslik="SAYI TAHMIN OYUNU"
print(baslik.center(80,"*"))
baslangic=input("""Sayin kullanici lutfen aklinizdan 0-100 arasinda bir sayi tutunuz.
-Tahminim tuttugunuz sayidan buyuk ise lutfen '-' basiniz.
-Tahminim tuttugunuz sayidan kucuk ise lutfen '+'                                           
-Tahminim dogru ise lutfen 'BRAVO' yaziniz.
Hadi baslayalim...
Hazir oldugunuzda bir tusa basiniz:""")                                 # kullaniciya oyun hakkinda bilgilendirme yapiliyor. 
ilk_sayi=0
ikinci_sayi=101
sayac=0
tahminler=[]                                                            # tahminler bu listeye kayit edilecek.
while True:
    sayac+=1
    pc_tahmin=random.randrange(ilk_sayi,ikinci_sayi)                    # randrange fonksiyonu ile bilgisayardan verilen aralikta bir sayi istiyoruz.
    print("Tahminim:",pc_tahmin)
    degerlendirme=input("Kullanici degerlendiriyor:")                   # kullanicidan tahminin fazla mi az mi yoksa dogrumu degerlendirmesi aliniyor.
    degerlendirme=degerlendirme.lower()                                 # bu islem bravo yazisini her kombinasyonda dogru sonuc vermesi icin kullanildi.
    if pc_tahmin in tahminler:                                          # burda bilgisayarin ayni tahmini yapmasi durumunda toplam tahmin sayisini etkilemesi engellendi.
        print("Bu sayiyi soylemisim")
        sayac-=1
        continue
    else:                                                               
        tahminler.append(pc_tahmin)                                     # tahmin listeye eklendi.
        print(tahminler)
        if degerlendirme=="-":                                          # eyer kullanici - isaretini girerse randrange modulunun ikinci parametresi tahmin oldu.
            ikinci_sayi=pc_tahmin                                       # boylelikle bir sonraki tahmin bir onceki tahminden buyuk olamaz.
        elif degerlendirme=="+":                                        # eyer kullanici + isaretini girerse randrange modulunun ikinci parametresi tahmin oldu.
            ilk_sayi=pc_tahmin                                          # boylelikle bir sonraki tahmin bir onceki tahminden kucuk olamaz.
        elif degerlendirme=="bravo":
            print("Afferim bana {}. denemede bildim".format(sayac))
            break
        else:
            print("Oyle kafana gore her seyi yazmamalisin!\n '-' veya '+' veya 'bravo' yazmalisin")
            sayac-=1
            continue


      
