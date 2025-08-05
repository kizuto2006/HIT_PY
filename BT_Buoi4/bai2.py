A = {'001','002','003','004','007'}
B = {'003','006','002','007','009','034','462'}
AuB= A.intersection(B)
AandB = A.union(B)
AdifB = A.difference(B)
print('Những sinh viên đăng kí học cả hai lớp là : ',AuB)
print('Những sinh viên đăng kí học là : ',AandB)
print('Những sinh viên đăng kí bàn 1 mà không đăng kí bàn 2 là : ',AdifB)
