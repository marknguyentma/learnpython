# Viết câu lệnh nhiều dòng
sum = 1 + 2 + 3 + \
    7 + 9 + 11  +\
    13 + 15 + 17

sum = (1 + 3 + 5 + 
      7 + 9 + 11 + 
      13 + 15 + 17)

# Chú thích
'''
Chú thích
'''

"""
Chú thích
"""

# Docstring 
def double(num):
    """Function to double the value"""
    return 2*num

print(double.__doc__)

#Variable (Biến)

hoa ="Hồng"
la =3
canh = 5.5

# Gán nhiều giá trị
hoa, la , canh = "Hồng", 3, 5.5


# Kiểu dữ liệu số in Python
'''
int
float
decimal
fraction
'''
a = 9
print(isinstance(a, complex))

# Output: 187
print(0b10111011)
 
 # Output: 257 (250 + 7)
print(0xFA + 0b111)
 
 # Output: 15
print(0o17)

# Chuyển đổi các kiểu số trong python
2 + 3.0
int(3.6)
float(7)
complex('2+8j')

#Module Decimal in python
# Exe:
(1.1 + 2.2) == 3.3
# out put: False
print( 1.1 + 2.2 )
# out put 3.300000003
import decimal

print(0.1)
print(decimal.Decimal(0.1))

from decimal import Decimal
#Out put: 3.3
print(Decimal('1.1') + Decimal('2.2'))

from decimal import Decimal as D

print(D('1.1') + D('2.2'))

# Phân số
import fractions

print(fractions.Fraction(4.5))
print(fractions.Fraction(2,5))
# Tạo phân số từ một float thì nên đưa vào một string
print(fractions.Fraction('0.1'))

#Toán học trong python
from fractions import Fraction as F
import math

print(math.pi)

# Chia lấy số nguyên
11 //3
# bình phương
5 ** 2

# biểu thức được in ra cuối cùng sẽ được gán cho biên _
# VD:
'''
tax = 12.5 / 100
price = 100.50
price*tax
price + _
round(_, 2)
'''

#Cách tạo string
'''
'spam eggs'
'doesn\'t'
"doesn't"
'"Yes," he said.'
"\"Yes,\" he said."
'"Isn\'t," she said.'
'''

# print('C:\some\name')
print(r'C:\some\name')
print("""\
 Usage: thingy [OPTIONS]
 -h Display this usage message
 -H hostname Hostname to connect to
 """)


# \newline Dấu gạch chéo ngược và dòng mới bị bỏ qua
# \\	Dấu gạch chéo ngược
# \'	Dấu nháy đơn
# \"	Dấu nháy kép
# \a	ASCII Bell
# \b	ASCII Backspace
# \f	ASCII Formfeed
# \n	ASCII Linefeed
# \r	ASCII Carriage Return
# \t	ASCII Horizontal Tab
# \v	ASCII Vertical Tab
# \ooo Ký tự có giá trị bát phân là ooo
# \xHH Ký tự có giá trị thập lục phân là HH

# Truy cập vào phần tử của chuỗi
word = 'Python'
print(word[0])
# Đếm từ phải sang trái
print(word[-1])

print(word[0:2])
print(word[2:5])

print(word[:2]+word[2:])

# Thay đổi xoá chuỗi
print('J'+word[1:])

qtm_string = 'quantrimang.com'
del qtm_string
# print(qtm_string)

# Nối chuỗi
print(3 * 'un' + 'ium')
print('Py' 'thon')
prefix = 'Py'
print(prefix + 'thon')

# Lặp và kiểm tra phần tử của chuỗi
count = 0
for letter in 'Quantrimang.com':
    if(letter == 'i'):
        count += 1
    print('Có', count, ' chữ i được tìm thấy')

# Kiểm tra có trong chuỗi hay chưa
print('quantrimang' in 'quantrimang.com')
print('python' in 'quantrimang.com')

# Làm việc với chuỗi
# chiều dài của chuỗi
s = 'supercalifragilisticexpialidocious'
print(len(s))

# hàm enumrate() trả về đối tượng liệt kê chứa các cặp giá trị index
qtm_string = 'Python'
qtm_enum = list(enumerate(qtm_string))
print('List: ', qtm_enum)

# Phương thức format() để định dạng chuỗi
# default
mac_dinh = "{}, {} và {}".format('Quản', 'Trị', 'Mạng')
print('\n--- Thứ tự mặc định ---')
print(mac_dinh)

# sử dụng đối số
thu_tu = "{1}, {0} và {2}".format('Quản', 'Trị', 'Mạng')
print('\n--- Thứ tự theo vị trí ---')
print(thu_tu)

tu_khoa = "{s}, {b} và {j}".format(j='Quản', b='Trị', s='Mạng')
print('\n--- Thứ tự theo từ khoá ---')
print(tu_khoa)

# Định dạng số nguyên
print("Khi chuyển {0} sang nhị phân sẽ là {0:b}".format(12))
# Định dạng số thập phân
print("Số thập phân {0} ở dạng mũ sẽ là {0:e}".format(1566.345))
# Làm tròn số thập phân
print("1 phần 3 là: {0:.3f}".format(1/3))
#căn chỉnh chuỗi
print("{:<10}|{:^10}|{:>10}".format('Quản', 'Trị', 'Mạng'))

# Định dạng kiểu cũ
x = 15.1236789
print('Giá trị của x là %3.2f' %x)
print('Giá trị của x là %3.4f' %x)

#Phương thức thường được sử dụng trong string
print("HeHeHe".lower())
print("HeHeHe".upper())
print("He He He".split())
print('..'.join(['He', 'He', 'He']))
print("He He He".find('He'))
print('He He Chấm He'.replace('Chấm', '...'))

# List (Danh sách)
squares = [1, 3,  9, 16, 25]
list1 = [1, "Hello", 3.4] 

# List lồng nhau
list4 = ["mouse", [8, 4, 6], ['a']]
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)
print(x[0])
print(x[0][1])

# Truy cập vào phần tử của list
qtm_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
 # Output: q
print(qtm_list[0])
 
 # Output: a
print(qtm_list[2])
 
 # Output: t
print(qtm_list[4])
 
 # List lồng nhau
ln_list = ["Happy", [1,3,5,9]]
 
 # Index lồng nhau
 
 # Output: a
print(ln_list[0][1])
 
 # Output: 9
print(ln_list[1][3])

print(qtm_list[-1])
print(qtm_list[-9])

# Cắt slice
print(qtm_list[1:5])
print(qtm_list[:8])
print(qtm_list[9:])
print(qtm_list[:])

# Thay đổi hoặc thêm phần từ vào list
abc = qtm_list + [1, 2, 3, 4, 5, 6, 7]
print(abc)

# Thay đổi giá trị trong list
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

# Chèn vào list
cubes.append(216)
cubes.append(7**3)
print(cubes)

# Thay đổi kích thước của list hay xoá nó hoàn toàn
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)

# Xoá
letters[2:5] = []
print(letters)
# Output [a, b, f, g]
print(len(letters))

# Xoá loại bỏ phần tử khỏi list
my_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
 
# xóa phần tử có index là 2
del my_list[2]
 
# Output: ['q', 'u', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm'] 
print(my_list)
 
# xóa phần tử có index từ 1 đến 7
del my_list[1:7]
 
# Output: ['q', 'a', 'n', 'g', '.', 'c', 'o', 'm']
print(my_list)
 
# xóa toàn bộ list my_list
del my_list
 
# Error: NameError: name 'my_list' is not defined
# print(my_list)
print("-----------------Xoá----------------------")
my_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
my_list.remove('.')
 
# Output: ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', 'c', 'o', 'm'] 
print(my_list)
 
# Output: n
print(my_list.pop(3))
 
# Output: ['q', 'u', 'a', 't', 'r', 'i', 'm', 'a', 'n', 'g', 'c', 'o', 'm']
print(my_list)
 
# Output: m
print(my_list.pop())
 
# Output: ['q', 'u', 'a', 't', 'r', 'i', 'm', 'a', 'n', 'g', 'c', 'o']
print(my_list)
 
my_list.clear()

# Output: [] (list rỗng)
print(my_list)

# Cách xoá các phần tử của một list bằng cách gán cho nó một list rỗng

my_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
my_list[11:15] = []
print(my_list)

# Phương thức trong list
# append(): Thêm phần tử vào cuối list.
# extend(): Thêm tất cả phần tử của list hiện tại vào list khác.
# insert(): Chèn một phần tử vào index cho trước.
# remove(): Xóa phần tử khỏi list.
# pop(): Xóa phần tử khỏi list và trả về phần tử tại index đã cho.
# clear(): Xóa tất cả phần tử của list.
# index(): Trả về index của phần tử phù hợp đầu tiên.
# count(): Trả về số lượng phần tử đã đếm được trong list như một đối số.
# sort(): Sắp xếp các phần tử trong list theo thứ tự tăng dần.
# reverse(): Đảo ngược thứ tự các phần tử trong list.
# copy(): Trả về bản sao của list.

QTM = [9,8,7,6,8,5,8]
 
# Output: 2
print(QTM.index(7))
 
# Output: 3
print(QTM.count(8))

QTM.sort()
 
# Output: [5, 6, 7, 8, 8, 8, 9]
print(QTM)
 
QTM.reverse()
 
# Output: [9, 8, 8, 8, 7, 6, 5]
print(QTM)

QTM = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
 
# Output: 3
print(QTM.index('n'))
 
# Output: 2
print(QTM.count('a'))

QTM.sort()
 
# Output: ['.', 'a', 'a', 'c', 'g', 'i', 'm', 'm', 'n', 'n', 'o', 'q', 'r', 't', 'u']
print(QTM)
 
QTM.reverse()
 
# Output: ['u', 't', 'r', 'q', 'o', 'n', 'n', 'm', 'm', 'i', 'g', 'c', 'a', 'a', '.']
print(QTM)

# Cách tạo một list (List comprehension)
# List comprehension là 1 biểu thức đi kèm với lệnh
# for được đặt trong cặp dấu ngoặc vuông []
for x in range(9):
    print(x)
cub3 = [3 ** x for x in range(9)]
print(cub3)

cub3 = []
for x in range(9):
    cub3.append(3 ** x)
print(cub3)

# if
cub3 = [3 ** x for x in range(9) if x > 4]
 
# Output: [243, 729, 2187, 6561]
print(cub3)
 
so_le = [x for x in range (18) if x % 2 == 1]
 
# Output: [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(so_le)
 
noi_list = [x+y for x in ['Ngôn ngữ ','Lập trình '] for y in ['Python','C++']]
 
# Output: ['Ngôn ngữ Python', 'Ngôn ngữ C++', 'Lập trình Python', 'Lập trình C++']
print(noi_list)

# Kiểm tra phần tử có trong list không
QTM = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
 
# Output: True
print('q' in QTM)
 
# Output: True 
print('.' in QTM)
 
# Output: False
print('z' in QTM)

# Vòng lặp trong list
for ngon_ngu in ['Python', 'Java', 'C']:
    print("Tôi thích lập trình", ngon_ngu)

# Các hàm Python tích hợp vs list
# all(): Trả về giá trị True nếu tất cả các phần tử của list đều là true hoặc list rỗng.
# any(): Trả về True khi bất kỳ phần tử nào trong list là true. Nếu list rỗng hàm trả về giá trị False.
# enumerate(): Trả về đối tượng enumerate, chứa index và giá trị của tất cả các phần tử của list dưới dạng tuple.
# len(): Trả về độ dài (số lượng phần tử) của list.
# list(): Chuyển đổi một đối tượng có thể lặp (tuple, string, set, dictionary) thành list.
# max(): Trả về phần tử lớn nhất trong list.
# min(): Trả về phần tử nhỏ nhất trong list.
# sorted(): Trả về list mới đã được sắp xếp.
# sum(): Trả về tổng của tất cả các phần tử trong list.

# Tuple
# Tuple thường được sử dụng cho các dữ liệu không cho phép sửa đổi
# VD:
t = (10, "quan tri mang", 2j)

# Có thể cắt ra nhưng không thể thay đổi giá trị
print("t[0:2]= ", t[0:2])

# Tuple thường được sử dụng cho các kiểu dữ liệu không đồng nhất (khác nhau) 
# và list thường sử dụng cho các kiểu dữ liệu (đồng nhất) giống nhau.
# Vì tuple không thể thay đổi, việc lặp qua các phần tử của tuple 
# nhanh hơn so với list. Vì vậy, trong trường hợp này tuple chiếm ưu thế về hiệu suất hơn list một chút.
# Tuple chứa những phần tử không thay đổi, có thể được sử dụng như
# key cho dictionary. Với list, điều này không thể làm được.
# Nếu có dữ liệu không thay đổi việc triển khai nó như một tuple
# sẽ đảm bảo rằng dữ liệu đó được bảo vệ chống ghi (write-protected).

# Tuple rỗng
# Output: ()
my_tuple = ()
print(my_tuple)
 
# tuple số nguyên
# Output: (2, 4, 16, 256)
my_tuple = (2, 4, 16, 256)
print(my_tuple)
 
# tuple có nhiều kiểu dữ liệu
# Output: (10, "Quantrimang.com", 3.5)
my_tuple = (10, "Quantrimang.com", 3.5)
print(my_tuple)
 
# tuple lồng nhau
# Output: ("QTM", [2, 4, 6], (3, 5, 7))
my_tuple = ("QTM", [2, 4, 6], (3, 5, 7))
print(my_tuple)
 
# tuple có thể được tạo mà không cần dấu ()
# còn gọi là đóng gói tuple
# Output: (10, "Quantrimang.com", 3.5)
 
my_tuple = 10, "Quantrimang.com", 3.5
print(my_tuple)
 
# mở gói (unpacking) tuple cũng có thể làm được
# Output:
# 10
# Quantrimang.com
# 3.5
a, b, c = my_tuple
print(a)
print(b)
print(c) 

# Để tạo một tuple thì phần tử trong dấu () là chưa đủ
# phải cần thêm dấu phẩy

# tạo tuple chỉ với ()
# Output: <class 'str'>
my_tuple = ("Quantrimang.com")
print(type(my_tuple))
 
# khi thêm dấu phẩy vào cuối
# Output: <class 'tuple'>
my_tuple = ("Quantrimang.com",) 
print(type(my_tuple))
 
# dấu () là tùy chọn, bạn có thể bỏ nếu thích
# Output: <class 'tuple'>
my_tuple = "Quantrimang.com",
print(type(my_tuple))

# Truy cập vào các phần tử tuple
# tuple lồng nhau
n_tuple = ("Quantrimang.com", [2, 6, 8], (1, 2, 3))
 
# index lồng nhau
# Output: 'r'
print(n_tuple[0][5])
 
# index lồng nhau
# Output: 8
print(n_tuple[1][2])

# Thay đổi 1 tuple chỉ thay đổi được biến list trong tuple đó
my_tuple = (1, 3, 5, [7, 9])

my_tuple[3][0] = 8
print(my_tuple)

# Nối tuple
# Nối 2 tuple
# Output: (2, 4, 6, 3, 5, 7)
print((2, 4, 6) + (3, 5, 7))
 
# Lặp lại tuple
# Output: ('Quantrimang.com', 'Quantrimang.com', 'Quantrimang.com')
print(("Quantrimang.com",) * 3)

# Xoá tuple
QTM = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
 
# Không thể xóa phần tử của tuple
# Nếu bạn bỏ dấu # ở dòng 8,
# sẽ tạo ra lỗi:
# TypeError: 'tuple' object doesn't support item deletion

#del QTM[3]

# Có thể xóa toàn bộ tuple
# Kết quả chạy code sẽ hiện ra lỗi:
# NameError: name 'my_tuple' is not defined
del QTM
# QTM

# Các phương thức và hàm dùng với tuple
QTM = ('q','u','a','n','t','r','i','m','a','n','g','.','c','o','m')

print(type(QTM))
# Count
# Output: 2
print(QTM.count('m'))

# Index trả về index đầu tiên của nó trong mảng
# Output: 3
print(QTM.index('n'))

# all(): Trả về giá trị True nếu tất cả các phần tử của tuple là true hoặc tuple rỗng.
# any(): Trả về True nếu bất kỳ phần tử nào của tuple là true, nếu tuple rỗng trả về False.
# enumerated(): Trả về đối tượng enumerate (liệt kê), chứa cặp index và giá trị của tất cả phần tử của tuple.
# len(): Trả về độ dài (số phần tử) của tuple.
# max(): Trả về phần tử lớn nhất của tuple.
# min(): Trả về phần tử nhỏ nhất của tuple.
# sorted(): Lấy phần tử trong tuple và trả về list mới được sắp xếp (tuple không sắp xếp được).
# sum(): Trả về tổng tất cả các phần tử trong tuple.
# tuple(): Chuyển đổi những đối tượng có thể lặp (list, string, set, dictionary) thành tuple.

# Kiểm tra các phần tử trong tuple
QTM = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
 
# Kiểm tra phần tử
# Output: True
print('a' in QTM)

# Output: False
print('b' in QTM)

# Not in operation
# Output: False
print('g' not in QTM)

# Lặp qua các phần tử của tuple trong Python
for ngon_ngu in ('Python', 'C#'):
    print('I like ', ngon_ngu)

# Set
# Set là tập hợp các phần tử duy nhất không có thứ tự
# Các phần tử cách nhau bởi dấu phẩy nằm trong dấu ngoặc nhọn {}
# Trong set không thể chứa các phần tử thay đổi được như list, set hay dictionary
# VD:
a = {5, 2, 3, 1, 4}
print(a)
my_set = {1.0, "Xin chào", (1, 2, 3)}
print(my_set)

# Tạo 1 set rỗng
# initialize a with {}
qtm = {}

# Kiểm tra kiểu dữ liệu của qtm
# Output: <class 'dict'>
print(type(qtm))

# Khởi tạo qtm với set()
qtm = set()

# Kiểm tra kiểu dữ liệu của qtm
# Output: <class 'set'>
print(type(qtm))

# Để thêm một phần tử vào trong set bạn sử dụng add()
# Thêm nhiều dùng update() trong update() có thể nhận tuple, list, string, set làm đối số
# Khi thêm vào các bản sao sẽ bị loại bỏ

my_set = {1, 3}

my_set.add(2)
print(my_set)

my_set.update([2, 3, 4])
print(my_set)

my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Xoá một phần tử khỏi set
# Chuyền vào một giá trị cụ thể
# Discard Note: Xoá một phần tử không tồn tại trong set thì discard không làm gì cả
my_set.discard(4)
print(my_set)

#Remove Note: Xoá một phần tử không tồn tại trong set sẽ báo lỗi
my_set.remove(6)
print(my_set)

# Xoá ngẫu nhiên
my_set.pop()
print(my_set)

# Xoá hoàn toàn
my_set.clear()
print(my_set)

# Các toán tử trong set
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Hợp A và B
# Dùng dấu |
print(A | B)

# Dùng hàm union()
print(A.union(B))
print(B.union(A))

# Giao A và B
# Dùng dấu &
print(A & B)

# Dùng hàm intersection()
print(A.intersection(B))
print(B.intersection(A))

# Hiệu của A và B
# A - B là tập hợp các phần tử chỉ có trong A
# B - A là tập hợp các phần tử chỉ có trong B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Dùng giấu -
print(A - B)

# Dùng hàm difference
print(A.difference(B))

# Bù của A và B
print(A.symmetric_difference(B))

# Các phương thức sử dụng trên set
# add()	Thêm một phần tử vào set.
# clear()	Xóa tất cả phần tử của set.
# copy()	Trả về bản sao chép của set.
# difference()	Trả về set mới chứa những phần tử khác nhau của 2 hay nhiều set.
# difference_update()	Xóa tất cả các phần tử của set khác từ set này.
# discard()	Xóa phần tử nếu nó có mặt trong set.
# intersection()	Trả về set mới chứa phần tử chung của 2 set.
# intersection_update()	Cập nhật set với phần tử chung của chính nó và set khác.
# isdisjoint()	Trả về True nếu 2 set không có phần tử chung.
# issubset()	Trả về True nếu set khác chứa set này.
# issuperset()	Trả về True nếu set này chưa set khác.
# pop()	Xóa và trả về phần tử ngẫu nhiên, báo lỗi KeyError nếu set rỗng.
# remove()	Xóa phần tử từ set. Nếu phần tử đó không có trong set sẽ báo lỗi KeyError.
# symmetric_difference()	Trả về set mới chứa những phần tử không phải là phần tử chung của 2 set.
# symmetric_difference_update()	Cập nhật set với những phần tử khác nhau của chính nó và set khác.
# union()	Trả về set mới là hợp của 2 set.
# update()	Cập nhật set với hợp của chính nó và set khác.

# Kiểm tra phần tử trong set
# Khởi tạo my_set
my_set = set("Quantrimang.com")

# Kiểm tra xem Q có trong my_set không
# Output: True
print('Q' in my_set)

# Kiểm tra xem q có trong my_set không
# Output: False
print('q' in my_set)

# Lặp qua các phần tử của set
for letter in set("Python"):
    print(letter)

# Frozenset
"""
Các set có thể thay đổi được nhưng không thể băm (hash) được, do đó 
không thể sử dụng set để làm key cho dictionary. Nhưng frozenset có 
thể băm được nên có thể dùng như các key cho dictionary.
Frozenset có thể tạo bằng hàm frozenset(). Kiểu dữ liệu này hỗ trợ 
các phương thức như copy(), difference(), intersection(), isdisjoint(),
issubset(), issuperset(), symmetric_difference() và union(). Vì không 
thể thay đổi nên phương thức add() hay remove() không sử dụng được trên frozenset.
"""

# Dictionary

# Được định nghĩa trong giấu {} với mỗi phần tử là một cặp theo dạng key: value
dict1 = {} #dictionary rỗng
print(dict1)
#dict2 là dictionary với các khóa nguyên
dict2 = {1: 'Quantrimang.com',2: 'Công nghệ'}
print(dict2)
#Tạo dictionary với khóa hỗn hợp
dict3 = {'tên': 'QTM', 1: [1, 3, 5]}
print(dict3)
#Tạo dictionary bằng dict()
dict4 = dict({1:'apple', 2:'ball'})
print(dict4)
#Tạo dictionary từ chuỗi với mỗi mục là một cặp
dict5 = dict([(1,'QTM'), (2,'CN')])
print(dict5)

# Truy cập phần tử của dictionary

#khai báo và gán giá trị dict2
dict2 = {1: 'Quantrimang.com','quantrimang': 'Công nghệ'} 
print(type(dict2)) #in kiểu dữ liệu của dict2
#trích xuất dữ liệu bằng khóa rồi in
print("dict2[1] = ", dict2[1]) 
print("dict2[quantrimang] = ",dict2['quantrimang'])

# Thay đổi, thêm phần tử cho dictionary
dict2['quantrimang'] = 'Tech'
dict2[2] = 'Add'

print(dict2)

# Xoá phần tử dictionary
binh_phuong = {1:1, 2:4, 3:9, 4:16, 5:25}

# Xoá phần tử key = 4
binh_phuong.pop(4)
print(binh_phuong)

# Xoá phần tử key = 3
del binh_phuong[3]
print(binh_phuong)

# Xoá ngẫu nhiên
binh_phuong.popitem()
print(binh_phuong)

# Xoá hết phần tử
binh_phuong.clear()
print(binh_phuong)

# Xoá dict
# del binh_phuong
# print(binh_phuong)

# Các phương thức và hàm cho dictionary
# clear()	Xóa tất cả phần tử của dictionary.
# copy()	Trả về một bản sao shollow copy của dictionary.
# fromkeys(seq[,v])	Trả về dictionary mới với key từ seq và value bằng v (default là None).
# get(key[,d])	Trả về giá trị của key, nếu key không tồn tại, trả về d. (default là None).
# items()	Trả lại kiểu xem mới của các phần tử trong dictionary (key, value).
# keys()	Trả về kiểu xem mới của các key trong dictionary.
# pop(key[,d])	Xóa phần tử bằng key và trả về giá trị hoặc d nếu key không tìm thấy. Nếu d không được cấp, key không tồn tại thì sẽ tạo lỗi KeyError.
# popitem()	Xóa và trả về phần tử bất kỳ ở dạng (key, value). Tạo lỗi KeyError nếu dictionary rỗng.
# setdefault(key,[,d])	Nếy key tồn tại trả về value của nó, nếu không thêm key với value là d và trả về d (default là None).
# update([other])	Cập nhật dictionary với cặp key/value từ other, ghi đè lên các key đã có.
# values()	Trả về kiểu view mới của value trong dictionary.

# Dictionary comprehension
# Là cách đơn giản, rút gọn để gọn dictionary từ một vòng lặp trong Python
lap_phuong = {x: x*x*x for x in range(6)}
print(lap_phuong)

lap_phuong = {}
for x in range(6):
    lap_phuong[x] = x*x*x
print(lap_phuong)

# Có thể chèn if vào
lap_phuong_chan = { x: x*x*x for x in range(10) if  x%2 == 0}
print(lap_phuong_chan)

# Kiểm tra và lặp qua phần tử trong dictionary
lap_phuong = {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
#output: True
print (2 in lap_phuong)
#output: False
print (9 in lap_phuong)
#output: False
print (5 not in lap_phuong)

# Duyệt qua các key
for i in lap_phuong:
    print(lap_phuong[i])

# Chuyển đổi các kiểu dữ liệu
# VD:
print(float(11))
print(int(18.6))
print(set([2, 4, 6]))
print(tuple({3, 5, 7}))
print(list('quantrimang'))
print(dict([[2, 4], [1, 3]]))

# First Step
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

# sử dụng đối số end cho hàm print() để tránh thêm dòng mới trong kết quả đầu ra
# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a + b


# Mảng (Array)
# List và module array trong python
a = [1, 3.5, "Hello"]

# Nếu tạo mảng sử dụng module array thì các phần tử của mảng phải có cùng kiểu số
# import array as arr
# a = arr.array('d', [1, 3.5, "Hello"])

# How to create a array?
import array as arr

a = arr.array('d', [1.1, 3.5, 4.5])
print(a)

# Code trên tạo mảng kiểu float
# Chữ 'd' là mã kiểu quyết định kiểu của mảng trong quá trình tạo.

# Mã kiểu   ||   	C Type    ||	Python Type	   || Kích thước tối thiểu tính theo byte
# 'b'	        signed char	           int	                    1
# 'B'	        unsigned char	       int	                    1
# 'u'	        Py_UNICODE	      Unicode character	            2
# 'h'	        signed short	        int	                    2
# 'H'	        unsigned short	        int	                    2
# 'i'	        signed int	            int	                    2
# 'I'	        unsigned int	        int	                    2
# 'l'	        signed long	            int 	                4
# 'L'	        unsigned long	        int	                    4
# 'f'	        float	                float	                4
# 'd'	        double	                float	                8

# Truy cập vào các phần tử của mảng
import array as arr

a = arr.array('i', [2, 4, 6, 8])
print("Phần tử đầu tiên", a[0])
print("List number", a[1:3])

# Thay đổi và thêm phần tử trong mảng
a[0] = 1
print(a)

a[1:3] = arr.array('i', [5, 6])
print(a)

a.append(9)
print(a)

a.extend([5, 6, 7])
print(a)

mang_le = arr.array('i', [3, 5, 7])
mang_chan = arr.array('i', [2, 4, 6])

noi = mang_chan + mang_le
print(noi)


# List Comprehension
# Cách viết code ngắn gọn để tạo một danh sách phức tạp
letters = ['a', 'b', 'c', 'd']
print(letters)
# C1:
uppers = []
for letter in letters:
    a = letter.upper()
    uppers.append(a)
print(uppers)

# C2:
uppers_letter = [x.upper() for x in letters]
print(uppers_letter)

# Phần thứ 3 của LC
# Thêm điều kiện
ages = [1, 34, 5, 7, 3, 57, 356]
print(ages)

old_ages = [x for x in ages if x > 10]
print(old_ages)

# Tránh sử dụng LC khi code có nhiều hơn một hàm đơn giản
# Vì như thế code sẽ dài và khó hiểu
# VD: 
old_ages = [x for x in ages if x > 10 and x < 100 and x is not None]

# VD2:
# letters = ['a', 'b', 'c', 'd', 2]
# print(letters)

# upper_letters = [x.upper() for x in letters]
# print(upper_letters)

# Tạo ra ngoại lệ để tránh các trường hợp lỗi thay vì dùng LC
letters = ['a', 'b', 'c', 1]
print(letters)

uppers_letter = []

for letter in letters:
    try: 
        result = letter.upper()
        uppers_letter.append(result)
    except AttributeError:
        pass

print(uppers_letter)