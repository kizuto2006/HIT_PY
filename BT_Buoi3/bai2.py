#1
k = int(input('Nhập số phần tử k : '))
lst = []
for i in range(k) :
    num = int(input(f'Nhập phần tử thứ {i+1} : '))
    lst.append(num)
n = int(input('Nhập số dòng của ma trận : '))
m = int(input('Nhập số cột của ma trận : '))

#2
if(k < n*m) :
    print('NO')
else :
    for i in range(m) :
        for x in range(n) :
            print(lst[x + 3*i],end = " ")
        print("")
        