#1
N = int(input("Nhập số phần tử : "))
lst = []
for i in range(N):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(num)

#2
X = int(input("Nhập số X: "))
count_X = lst.count(X)
print(f"Số {X} xuất hiện {count_X} lần")

#3
replacement = [8, 5, 4, 0, 1, 3]
num_replace = 7 - 1
if len(lst) < 7:
    lst[1:] = replacement[:len(lst) - 1]
    lst.extend(replacement[len(lst) - 1:])
else:
    lst[1:7] = replacement
print(lst)
#4
print(f"Số lớn nhất trong list: {max(lst)}")
print(f"Số nhỏ nhất trong list: {min(lst)}")

#5
Y = int(input("Nhập số Y: "))
lst.insert(0, Y)

#6
if lst == sorted(lst):
    print("TĂNG")
elif lst == sorted(lst, reverse=True):
    print("GIẢM")
else:
    print("NO")
