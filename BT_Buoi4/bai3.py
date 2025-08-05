A = {0,1,2.3,6,1,3,2,3,8}
B = {2,2,7,8,3,2,7,8,4,9,2,2,3,8,9,6}
Happiness = 0

n = int(input('Nhap so luong so ban muon nhap : '))

for i in range(n) :
    urnum = int(input('Nhap so : '))
    if urnum in A :
        Happiness += 1
    if urnum in B :
        Happiness -= 1

print('So diem hanh phuc cua ban la : ',Happiness)