a = []
n = int(input('Nhập số phần tử : '))
for i in range(n) :
    temp = input('Nhap so : ')
    a.append(temp)
b = tuple(a)
print('Tuple b :',b)
count = 0
for x in b :
    if x.isdigit() :
        count += 1
print('So phan tu co dang so trong b la : ',count)
