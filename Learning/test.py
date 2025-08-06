a = {9:"Xuat sac",8:'Gioi'}
diem = float(input("Nhap diem ktra cua ban :"))
for key in a :
    if diem >= key :
        print("Nang luc: ",a[key])
        break
    if diem <8 :
        print('Nang luc: tam on')
        break
