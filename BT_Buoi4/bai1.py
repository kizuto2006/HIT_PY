import random
a = []

n = int(input('Nhap so phan tu : '))
for i in range(n) :
    temp = random.randint(0,9)
    a.append(temp)

tuple1 = tuple(a)
print('Day tuple dau tien la : ',end ='')
print(tuple1)
tuple2 = tuple1
print('Day tuple thu hai la : ',end='')
print(tuple2)

sum = 0
for x in tuple2 :
    sum += x
print('Trung binh cong cac phan tu la :',float(sum/n))