#Cau 3
a = [5,6,11]
b = []
i = 0
n = int(input('Nhap so phan tu :'))
if (n<=100 and n>=1) :
    while i < n :
        temp = int(input('Nhap so :'))
        if(temp > 0) :
            b.append(temp)
            i += 1
        else :
            break

for i in range(len(b)-1) :
    if(b[i] < b[i+1]) :
        kq = 'tot'
    else : 
        break
if kq == 'tot' :
    print(b[0])