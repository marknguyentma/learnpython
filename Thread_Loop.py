# Lệnh if

# if
a = 1
if a > 0 :
    print('OK')

# if else
a = -1
if a > 0 :
    print('OK')
else: 
    print('A há')
# if elif else
a = -1
if a > 0 :
    print('OK')
elif a < 0:
    print('Ì hí') 

else: 
    print('A há')
# if if
a = 0
if a > 0:
    if a == 0:
        print('Không')
    else:
        print('OK')
else: 
    print('A há')

# Vòng lặp for

# Tính tổng tất cả các số trong danh sách A
# Danh sách A
A = [1, 3, 5, 9, 11, 2, 6, 8, 10]
# Biến để lưu trữ tổng các số là tong, gán giá trị ban đầu bằng 0 
tong = 0
# Vòng lặp for, a là biến lặp
for a in A: 
     tong = tong+a
# Đầu ra: Tổng các số là 55
print("Tổng các số là", tong)

# Hàm range()
# Hàm range(số bắt đầu, số kết thúc, khoảng cách giữa hai số)
#Lệnh 1
print(range(9)) 
#Lệnh 2
print(list(range(9)))
#Lệnh 3 
print(list(range(2, 5)))
#Lệnh 4 
print(list(range(0, 15, 5))) 

# Hàm range() có thể sử dụng kết hợp với len() để lặp qua một dãy sử dụng index
chuoi = ['bố','mẹ','em']

for tu in range(len(chuoi)):
    print("Anh yêu", chuoi[tu])

# Kết hợp for với else:
B = [0, 2, 4, 5]

for b in B:
    print(b)
else:
    print("Đã hết số.")

#VD: 
for num in range(0, 10):
    print(num)
    for i in range(2, num):
        print(i)
        if num%2 == 0:
            j = num/i
            print('%d bằng %d * %d' % (num, i, j))
            break
    else:
        print(num, ' là số nguyên tố')

# Vòng lặp while

count = 0
n = 0
while(count < 8):
    print('Số thứ ', n, ' là: ', count)
    n = n + 1
    count = count + 1
print('Done')

# VD2:
# n = int(input("Nhập n: "))
# tong = 0
# i = 1

# while i <= n:
#     tong = tong + i
#     i = i + 1
# print('Tổng là ', tong)

# Kết hợp while vs else
# VD1
dem = 0
while dem < 3:
    print("Đang ở trong vòng lặp while")
    dem = dem + 1
else:
    print("Đang ở trong else")

# VD2
n = 0
while n < 2:
    print(n,"nhỏ hơn 2")
    n = n + 1
else:
   print (n,"không nhỏ hơn 2")


# Break và continue
# break
# Kết thúc vòng lặp chứa nó

for val in "string":
    if val == 'i':
        break
    print(val)


# continue
# Quay lại vòng lặp cứ không kết thúc như break 
# Bỏ qua code phía dưới chạy lại vòng lặp

for val in "string":
    if val == 'i':
        continue
    print(val)
print('kết thúc')


bien = 10
while bien > 0:
    bien = bien - 1
    if bien == 5:
        continue
    print('Giá trị hiện tại là: ', bien)
print('OK')
    
# pass
# để giữ một hàm hay tạo một khối lệnh rỗng trong hàm đó để giữ hàm lại
sequence = {'p','a','s','s'}
for val in sequence:
    pass

def function(args): pass

# Kỹ thuật vòng lặp
# Vòng lặp vô hạn
# while True:
#     num = int(input("Nhập một số: "))
#     print("Gấp ba của",num,"là",3 * num)

# Vòng lặp với điều kiện đầu
#Thử những số khác nhau bằng cách gán số đó cho n 
n = 15

# Dùng lệnh sau nếu muốn người dùng nhập số
#n = int(input("Nhập số n: "))

# Khởi tạo tổng tong và biến đếm i
tong = 0
i = 1

while i <= n:
    tong = tong + i
    i = i+1 # cập nhật số đếm
# Code by Quantrimang.com
# in tổng
print("Tổng các số từ 1 đến ",n, " là", tong)

# Vòng lặp với điều kiện giữa
# Nhận đầu vào từ người dùng cho đến khi họ nhập một nguyên âm 
# nguyenAm = "aeiouAEIOU" 
# # vòng lặp vô hạn 
# while True: 
#     m = input("Nhập một nguyên âm: ")
#     # Điều kiện ở giữa khối lệnh 
#     if m in nguyenAm: 
#         break 
#     print("Đây không phải là nguyên âm. Hãy thử lại!") 
# print("Chuẩn rồi, cảm ơn bạn!")

# Vòng lặp với điều kiện cuối
# Tung xúc xắc cho đến khi người dùng chọn thoát
import random 
while True: 
    input("Nhấn Enter để tung xúc xắc") 
    # nhận số mặt xúc xắc bất kỳ từ 1 đến 6 
    num = random.randint(1,6) 
    print("Bạn tung được mặt",num) 
    option = input("Bạn có muốn tung lại không?(y/n) ") 
    # điều kiện 
    if option == 'n': 
        break