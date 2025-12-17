#1-misol
sonlar = [1, 2, 3, 4, 5]

kvadratlar = list(map(lambda x: x**2, sonlar))
print(kvadratlar)

#2-misol
sozlar = ["salom", "dunyo", "python"]

katta = list(map(str.upper, sozlar))
print(katta)

#3-misol
sonlar = [3, 5, 7, 9]

ikki_baravar = list(map(lambda x: x * 2, sonlar))
print(ikki_baravar)

#4-misol
sozlar = ["olma", "banan", "anor"]

uzunliklar = list(map(len, sozlar))
print(uzunliklar)

#5-misol
a = [1, 2, 3]
b = [4, 5, 6]

yigindi = list(map(lambda x, y: x + y, a, b))
print(yigindi)

#6-misol
sonlar = [-5, 3, -2, 7]

modullar = list(map(abs, sonlar))
print(modullar)

#7-misol
sozlar = ["salom", "kitob", "python"]

teskari = list(map(lambda x: x[::-1], sozlar))
print(teskari)
