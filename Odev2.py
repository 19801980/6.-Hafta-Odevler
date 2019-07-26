##Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu 
##kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz 
##algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini 
##saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim: 
##                        X O _  
##                        _ X _   
##                        _ _ _
##
##seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O" 
##koymalidir.
##
##
##Farkli bir ihtimal:
##                        O X X 
##                        O _ X 
##                        _ _ _ 
##
##boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak 
##oyunu bitirmelidir.
baslik=" XOX OYUNUNA HOSGELDINIZ "
print(baslik.center(80,"*"))
import random                                                               # random modulu cagirildi. ilerleyen satirlarda bazi fonksiyonlari kullanilacak.
tahta=[["---","---","---"],                                                 # oyun tahtasi liste halinde olusturuldu.
       ["---","---","---"],
       ["---","---","---"]]
print("\n"*1)
for i in tahta:
    print("\t".expandtabs(40),*i,end="\n"*2)                                # tahta ekrana bastirildi.
    
kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],                              # oyunun hangi kosullarda kazanilacagi llistesi olusturuldu.
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]
konum=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]               # tahtanin tum konumlarini iceren bir dosya olusturuldu.
kullanici_durum=[]                                                          # kullanicinin sececegi konumlari depolayacak bos bir liste olusturuldu.
bilgisayar_durum=[]                                                         # bilgisayarin sececegi konumlari depolayacak bos bir liste olusturuldu.

sira=2
while True:
    if sira%2==0:                                                           # buradaki if, else blogunda sira kimde ise onun ismi ekrana bastirildi.
        isaret="X".center(3)
    else:
        isaret="O".center(3)

    print("ISARET: {}\n".format(isaret))
    if sira%2==0:                                                           # sira kullanicida oldugunda iki input alindi.
        x=input("Yukaridan asagiya [1, 2, 3]\t:")
        y=input("Soldan saga [1, 2, 3]\t\t:")
        if x!= "1" and x!="2" and x!="3":                                   # bu inputlar 1,2,3 den farkli ise kullanici uyarildi.
            print("Lutfen giris degerlerinizi kontrol ediniz.")
            continue
        if y!= "1" and y!="2" and y!="3":
            print("Lutfen giris degerlerinizi kontrol ediniz.")
            continue
        x=int(x)-1                                                          # listede ilk oge sifirdan basladigi icin kullanicinin girdigi rakamlardan 1 cikarildi.
        y=int(y)-1
        if tahta[x][y]=="---":                                              # kullanicin girdigi konum bos ise oraya 'x' yazdirildi.
            tahta[x][y]=isaret
            kullanici_durum+=[[x,y]]                                        # bu konum kullanici_durum listesine eklendi.
            konum.remove ([x,y])                                            # girilen deger konum listesinden cikarildiki bilgisayarin o konumu secmesi engellendi.
        else:
            print("Lutfen baska bir yer secin burasi dolu")                 # secilen konum bos degil ise kullanici uyarildi.
            continue
    elif sira%2==1:                                                          
        if konum==[]:                                                       # bilgisayar sirasi geldiginde eyer konum listesinde secilecek konum yok ise oyun berabere yazdirildi.
            print("oyun berabere bitmistir!!!")
            break
############################################################################# bu bloklarda bilgisayara iki 'o' nun yan yana oldugu anda oyunu bitirebilmesi saglandi. 
        
        elif tahta[0][0]==" O " and tahta[0][1]==" O " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])
        elif tahta[0][0]==" O " and tahta[0][2]==" O " and tahta[0][1]=="---":
                tahta[0][1]=" O "
                bilgisayar_durum+=[[0,1]]
                konum.remove([0,1])
        elif tahta[0][2]==" O " and tahta[0][1]==" O " and tahta[0][0]=="---":
                tahta[0][0]=" O "
                bilgisayar_durum+=[[0,0]]
                konum.remove([0,0])        
        elif tahta[1][0]==" O " and tahta[1][1]==" O " and tahta[1][2]=="---":
                tahta[1][2]=" O "
                bilgisayar_durum+=[[1,2]]
                konum.remove([1,2])
        elif tahta[1][0]==" O " and tahta[1][2]==" O " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[1][2]==" O " and tahta[1][1]==" O " and tahta[1][0]=="---":
                tahta[1][0]=" O "
                bilgisayar_durum+=[[1,0]]
                konum.remove([1,0])        
        elif tahta[2][0]==" O " and tahta[2][1]==" O " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
        elif tahta[2][0]==" O " and tahta[2][2]==" O " and tahta[2][1]=="---":
                tahta[2][1]=" O "
                bilgisayar_durum+=[[2,1]]
                konum.remove([2,1])
        elif tahta[2][2]==" O " and tahta[2][1]==" O " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])        
        elif tahta[0][0]==" O " and tahta[1][0]==" O " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])
        elif tahta[0][0]==" O " and tahta[2][0]==" O " and tahta[1][0]=="---":
                tahta[1][0]=" O "
                bilgisayar_durum+=[[1,0]]
                konum.remove([1,0])
        elif tahta[2][0]==" O " and tahta[1][0]==" O " and tahta[0][0]=="---":
                tahta[0][0]=" O "
                bilgisayar_durum+=[[0,0]]
                konum.remove([0,0])             
        elif tahta[0][1]==" O " and tahta[1][1]==" O " and tahta[2][1]=="---":
                tahta[2][1]=" O "
                bilgisayar_durum+=[[2,1]]
                konum.remove([2,1])
        elif tahta[0][1]==" O " and tahta[2][1]==" O " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[2][1]==" O " and tahta[1][1]==" O " and tahta[0][1]=="---":
                tahta[0][1]=" O "
                bilgisayar_durum+=[[0,1]]
                konum.remove([0,1])        
        elif tahta[0][2]==" O " and tahta[1][2]==" O " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
        elif tahta[2][2]==" O " and tahta[1][2]==" O " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])
        elif tahta[0][2]==" O " and tahta[2][2]==" O " and tahta[1][2]=="---":
                tahta[1][2]=" O "
                bilgisayar_durum+=[[1,2]]
                konum.remove([1,2])    
        elif tahta[0][0]==" O " and tahta[1][1]==" O " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
        elif tahta[0][0]==" O " and tahta[2][2]==" O " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[2][2]==" O " and tahta[1][1]==" O " and tahta[0][0]=="---":
                tahta[0][0]=" O "
                bilgisayar_durum+=[[0,0]]
                konum.remove([0,0])
        elif tahta[0][2]==" O " and tahta[1][1]==" O " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])
        elif tahta[0][2]==" O " and tahta[2][0]==" O " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[2][0]==" O " and tahta[1][1]==" O " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])

################################################################################### bu bloklarda bilgisayara iki 'x' in yan yana oldugu durumlarda bir sonraki bosluga 'o' koymasi soylendi.
      
        elif tahta[0][0]==" X " and tahta[0][1]==" X " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])
        elif tahta[0][0]==" X " and tahta[0][2]==" X " and tahta[0][1]=="---":
                tahta[0][1]=" O "
                bilgisayar_durum+=[[0,1]]
                konum.remove([0,1])
        elif tahta[0][2]==" X " and tahta[0][1]==" X " and tahta[0][0]=="---":
                tahta[0][0]=" O "
                bilgisayar_durum+=[[0,0]]
                konum.remove([0,0])        
        elif tahta[1][0]==" X " and tahta[1][1]==" X " and tahta[1][2]=="---":
                tahta[1][2]=" O "
                bilgisayar_durum+=[[1,2]]
                konum.remove([1,2])
        elif tahta[1][0]==" X " and tahta[1][2]==" X " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[1][2]==" X " and tahta[1][1]==" X " and tahta[1][0]=="---":
                tahta[1][0]=" O "
                bilgisayar_durum+=[[1,0]]
                konum.remove([1,0])        
        elif tahta[2][0]==" X " and tahta[2][1]==" X " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
        elif tahta[2][0]==" X " and tahta[2][2]==" X " and tahta[2][1]=="---":
                tahta[2][1]=" O "
                bilgisayar_durum+=[[2,1]]
                konum.remove([2,1])
        elif tahta[2][2]==" X " and tahta[2][1]==" X " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])        
        elif tahta[0][0]==" X " and tahta[1][0]==" X " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])
        elif tahta[0][0]==" X " and tahta[2][0]==" X " and tahta[1][0]=="---":
                tahta[1][0]=" O "
                bilgisayar_durum+=[[1,0]]
                konum.remove([1,0])
        elif tahta[2][0]==" X " and tahta[1][0]==" X " and tahta[0][0]=="---":
                tahta[0][0]=" O "
                bilgisayar_durum+=[[0,0]]
                konum.remove([0,0])             
        elif tahta[0][1]==" X " and tahta[1][1]==" X " and tahta[2][1]=="---":
                tahta[2][1]=" O "
                bilgisayar_durum+=[[2,1]]
                konum.remove([2,1])
        elif tahta[0][1]==" X " and tahta[2][1]==" X " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[2][1]==" X " and tahta[1][1]==" X " and tahta[0][1]=="---":
                tahta[0][1]=" O "
                bilgisayar_durum+=[[0,1]]
                konum.remove([0,1])        
        elif tahta[0][2]==" X " and tahta[1][2]==" X " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
        elif tahta[2][2]==" X " and tahta[1][2]==" X " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])
        elif tahta[0][2]==" X " and tahta[2][2]==" X " and tahta[1][2]=="---":
                tahta[1][2]=" O "
                bilgisayar_durum+=[[1,2]]
                konum.remove([1,2])    
        elif tahta[0][0]==" X " and tahta[1][1]==" X " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
        elif tahta[0][0]==" X " and tahta[2][2]==" X " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[2][2]==" X " and tahta[1][1]==" X " and tahta[0][0]=="---":
                tahta[0][0]=" O "
                bilgisayar_durum+=[[0,0]]
                konum.remove([0,0])
        elif tahta[0][2]==" X " and tahta[1][1]==" X " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])
        elif tahta[0][2]==" X " and tahta[2][0]==" X " and tahta[1][1]=="---":
                tahta[1][1]=" O "
                bilgisayar_durum+=[[1,1]]
                konum.remove([1,1])
        elif tahta[2][0]==" X " and tahta[1][1]==" X " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])         
        else:                                                           # bu else blogunda eyer oyunu bitirme durumu yoksa bilgisayara rastgele bir yer secilmesi soylendi.
            secim=random.choice(konum)                              
            if tahta[secim[0]][secim[1]]=="---":                        # burada konum dosyasindan secilen bir degerin ilk index sayisi ve ikinci index sayisina bakilip tahtaya 'o' isareti konuldu.
                tahta[secim[0]][secim[1]]=isaret
                bilgisayar_durum+=[[secim[0],secim[1]]]
                konum.remove(secim)
            else:
                continue
    sira+=1
    for i in tahta:
        print("\t".expandtabs(40),*i,end="\n"*3)
    for i in kazanma_olcutleri:                                         # burayi bende tam anlamadim. :)
        o=[z for z in i if z in bilgisayar_durum]                       
        x=[z for z in i if z in kullanici_durum]
        
        if len(o)==len(i):
            print("O KAZANDI!")
            quit()
        if len(x)==len(i):
            print("X KAZANDI!")
            quit()
               
        
    
    
