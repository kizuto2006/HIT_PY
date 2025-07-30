#1
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

#2
s1rv = s1[::-1]
print("Chuỗi s1 đảo ngược:", s1rv)

#3
a = int(input("Nhập số a : "))
b = int(input("Nhập số b : "))
if 1 <= a < b <= len(s2):
    s2_1 = s2[a-1:b]
    s2rv = s2_1[::-1]
    print("Chuỗi con từ s2 sau khi đảo ngược:", s2rv)

#4
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
print("Chuỗi s3 :", s3)

#5
s4 = ''
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s4 += s1[i] + s2[i]
s4 += s1[min_len:] + s2[min_len:]

print("Chuỗi s4 :", s4)
