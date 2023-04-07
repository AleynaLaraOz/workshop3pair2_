#1.kısım

liste = []
for n in range(0,9):
    sayi = int(input('Sayı Giriniz: '))
    liste.append(sayi)
 
en_buyuk = max(liste)
 
print("Liste İçindeki En Büyük Sayı :", en_buyuk )

#2.kısım

x = int(input("Bir üst limit değeri giriniz: "))

for v in range(0, x+2 ,2):
  print(v)

#3.kısım

a = int(input("Bir üst limit değeri giriniz: "))
y = int(input("Bir alt limit değeri giriniz: "))

for i in range(y, a):
    if i%2 == 0:
        print(i)

