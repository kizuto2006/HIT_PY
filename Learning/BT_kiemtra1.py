#Cau 1
temp = input('Nhap day :')
a = list(temp)
b = tuple(a)
count = 0
print(b)
for i in range(0,9) :
    for x in b :
            if(x == " ") : break
            else :
                 if(x == str(i)) :
                       count = count + 1
    print(count)
        
