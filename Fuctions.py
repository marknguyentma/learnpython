# Hàm
def hello(name):
    """
    Hàm được dùng để chào
    """
    print('Hello,', name)

hello('hoang')

# Docstring in Python
# Được dùng để giải thích chức năng cho hàm

print(hello.__doc__)

# Lệnh return 
def gia_tri_tuyet_doi(so):
    """Hàm này trả về giá trị tuyệt đối
    của một số nhập vào"""
    if so >= 0: 
        return so 
    else: 
        return -so
# Đầu ra: 5
print(gia_tri_tuyet_doi(5))
# Đầu ra: 8
print(gia_tri_tuyet_doi(-8))
# Đầu ra: Giá trị tuyệt đối của số nhập vào
# num=int(input("Nhập số cần lấy giá trị tuyệt đối: "))
# print (gia_tri_tuyet_doi(num))

# Phạm vi của biến
def ham_in():
    x = 15
    print('Giá trị bên trong hàm: ', x)

x = 30
ham_in()
print("Giá trị bên ngoài hàm: ", x)

#  Hàm	     ||       Mô tả 
# abs()	            Trả về giá trị tuyệt đối của một số
# all()	            Trả về True khi tất cả các phần tử trong iterable là đúng
# any()	            Kiểm tra bất kỳ phần tử nào của iterable là True
# ascii()	        Tả về string chứa đại diện (representation) có thể in
# bin()	            Chuyển đổi số nguyên sang chuỗi nhị phân
# bool()	        Chuyển một giá trị sang Boolean
# bytearray()	    Trả về mảng kích thước byte được cấp
# bytes()	        Trả về đối tượng byte không đổi
# callable()	    Kiểm tra xem đối tượng có thể gọi hay không
# chr()         	Trả về một ký tự (một chuỗi) từ Integer
# classmethod()	    Trả về một class method cho hàm
# compile()	        Trả về đối tượng code Python
# complex()	        Tạo một số phức
# delattr()	        Xóa thuộc tính khỏi đối tượng
# dict()	        Tạo Dictionary
# dir()	            Trả lại thuộc tính của đối tượng
# divmod()	        Trả về một Tuple của Quotient và Remainder
# enumerate()	    Trả về đối tượng kê khai
# eval()	        Chạy code Python trong chương trình
# exec()	        Thực thi chương trình được tạo động
# filter()	        Xây dựng iterator từ các phần tử True
# float()	        Trả về số thập phân từ số, chuỗi
# format()	        Trả về representation được định dạng của giá trị
# frozenset()	    Trả về đối tượng frozenset không thay đổi
# getattr()	        Trả về giá trị thuộc tính được đặt tên của đối tượng
# globals()	        Trả về dictionary của bảng sumbol toàn cục hiện tại
# hasattr()	        Trả về đối tượng dù có thuộc tính được đặt tên hay không
# hash()	        Trả về giá trị hash của đối tượng
# help()	        Gọi Help System được tích hợp sẵn
# hex()	            Chuyển Integer thành Hexadecimal
# id()	            Trả về định danh của đối tượng
# input()	        Đọc và trả về chuỗi trong một dòng
# int()	            Trả về số nguyên từ số hoặc chuỗi
# isinstance()	    Kiểm tra xem đối tượng có là Instance của Class không
# issubclass()  	Kiểm tra xem đối tượng có là Subclass của Class không
# iter()	        Trả về iterator cho đối tượng
# len()	            Trả về độ dài của đối tượng
# list()	        Tạo list trong Python
# locals()	        Trả về dictionary của bảng sumbol cục bộ hiện tại
# map()	            Áp dụng hàm và trả về một list
# max()	            Trả về phần tử lớn nhất
# memoryview()  	Trả về chế độ xem bộ nhớ của đối số
# min()	            Trả về phần tử nhỏ nhất
# next()	        Trích xuất phần tử tiếp theo từ Iterator
# object()	        Tạo một đối tượng không có tính năng (Featureless Object)
# oct()	            Chuyển số nguyên sang bát phân
# open()	        Trả về đối tượng File
# ord()	            Trả về mã Unicode code cho ký tự Unicode
# pow()	            Trả về x mũ y
# print()	        In đối tượng được cung cấp
# property()	    Trả về thuộc tính property
# range()	        Trả về chuỗi số nguyên từ số bắt đầu đến số kết thúc
# repr()	        Trả về representation có thể in của đối tượng
# reversed()	    Trả về iterator đảo ngược của một dãy
# round()	        Làm tròn số thập phân
# set()	            Tạo một set các phần tử mới
# setattr()	        Đặt giá trị cho một thuộc tính của đối tượng
# slice()	        Cắt đối tượng được chỉ định bằng range()
# sorted()          Trả về list được sắp xếp
# staticmethod()	Tạo static method từ một hàm
# str()	            Trả về một representation không chính thức của một đối tượng
# sum()	            Thêm một mục vào Iterable
# super()	        Cho phép tham chiếu đến Parent Class bằng super
# tuple()	        Tạo một Tuple
# type()	        Trả về kiểu đối tượng
# vars()	        Trả về thuộc tính __dict__ của class
# zip()	            Trả về Iterator của Tuple
# __import__()	    Hàm nâng cao, được gọi bằng import


# Hàm do người dùng định nghĩa
def them_so(a,b):
 tong = a + b
 return tong

so1 = 5
so2 = 6
# so3 = int(input("Nhập một số: "))
# so4 = int(input("Nhập một số nữa: "))

print("Tổng hai số đầu là: ", them_so(so1, so2))

# print ("Tổng của hai số sau là: ", them_so(so3, so4))

# Tham số của hàm 
def Xin_chao(ten, loi_chao):
    """Hàm Xin_chao chào một người
    với thông điệp cho trước"""
    print("Xin chào", ten + ', '+loi_chao)

Xin_chao("Hoang", "Hi")

# Tham số mặc định
def Hello(ten, loi_chao="Hê Hê"):
    """Hàm Xin_chao chào một người
    với thông điệp cho trước"""
    print("Xin chào", ten + ', '+loi_chao)
Hello("Hoang")
Hello("Hoang", "Hi")

# Tham số keyword
Hello(ten="Linh", loi_chao="KK")
Hello(loi_chao="OKOK", ten="KOKO")
Hello("LOLO", loi_chao="OLOL")

# Tham số tuỳ biến trong hàm
def xinchao(*ten_chao):
    """Hàm này sẽ chào một danh sách người cho trước"""
    for ten in ten_chao:
        print("Xin chào", ten)

xinchao("Hải", "Hoa", "Công", "Sơn")

# Hàm lambda (Hàm vô danh)
nhandoi = lambda a: a*2
print(nhandoi)

# Sử dụng
# Kết hợp với filter
list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]

list_moi = list(filter(lambda a: (a%2 == 0) , list_goc))

# Kết quả: [10, 8, 6, 2, 4]
# By Quantrimang.com
print(list_moi)


#lambda với map()
list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]

list_moi = list(map(lambda a: a*2 , list_goc))

# Kết quả: [20, 18, 16, 14, 12, 2, 4, 6, 8, 10]
# By Quantrimang.com
print(list_moi)

# Các loại biến trong python
# Biến toàn cục (global)
x = "Biến toàn cục"

def vidu():
    print("X trong hàm vidu(): ",x)

vidu()
print("X ngoài: ", x)

# Biến cục bộ (local)
def vidu1():
    y = "Biến cục bộ"
    print(y)
vidu1()

# Biến cục bộ và biến toàn cục
# VD1:
x = 2

def vidu2():
    global x
    y = "Biến cục bộ"
    x = x * 2
    print(x)
    print(y)
#Viết bởi Quantrimang.com 
vidu2()

# VD2:
x = 5

def vidu3():
    x = 10
    print("Biến x cục bộ:", x)

vidu3()
print("Biến x toàn cục:", x)

# Biến nonlocal
def ham_ngoai():
    x = "Biến cục bộ"
 
    def ham_trong():
       nonlocal x
       x = "Biến nonlocal"
       print("Bên trong:", x)
 
    ham_trong()
    print("Bên ngoài:", x)

ham_ngoai()

# Từ khoá global
# Muốn chỉnh sửa biến global trong một hàm thì khai báo global tên biến trong hàm
a = 1 # Biến toàn cục

def them():
    global a 
    a = a + 9 
    print("Trong them():", a)

them()
print("Trong main:", a)

# Chia sẻ biến toàn cục thông qua module
import config

config.a = 10
config.b = "hello"

print(config.a)
print(config.b)

# Sử dụng biến toàn cục trong hàm lồng nhau
# x = 20
# def ham1():
#     def ham2():
#         global x
#         x = 25

# print("Trước khi gọi ham2: ", x)
# print("Đang gọi ham2")
# print("Sau khi gọi ham2: ", x)

# ham1()
# print("x trong main: ", x)

# Module trong python

import module

print(module.them(4,5))

# Sử dụng lệnh import
import math
print("Giá trị của pi là: ", math.pi)

# Nhập module và sửa tên khi nhập
import math as m
print("Giá trị của pi là: ", m.pi)

# Lệnh from ... import
from math import pi
print("Giá trị của pi là: ", pi)

# Nhập tất cả các tên
# from math import *
# print("Giá trị của pi là: ", pi)

# Đường dẫn tìm kiếm module 
# Khi nhập module, Python sẽ tìm một vài nơi. Trình thông dịch tìm các module có sẵn, 
# nếu không thấy nó sẽ vào danh sách các thư mục được định nghĩa trong sys.path. 
# Thứ tự tìm kiếm sẽ là:
# Thư mục hiện tại.
# PYTHONPATH (một biến môi trường với danh sách thư mục).
# Thư mục mặc định có vị trí phụ thuộc vào chọn lựa trong quá trình cài đặt.
import sys
sys.path


# Nạp lại module
# Trình thông dịch Python chỉ nhập một module trong một phiên. 
# Điều này làm cho mọi thứ trở nên hiệu quả hơn.
# Bạn viết code sau trong file mới, đặt tên là module_1:

# print("Code đã hoạt động") 
# Giờ ta thử nhập module module_1 để xem sự hiệu quả của việc nhập module nhiều lần.

# >>> import module_1
# Code đã hoạt động
# >>> import module_1
# >>> import module_1
# >>> import module_1
# >>> 

# Bạn có thể thấy rằng code trên chỉ thực hiện một lần, nghĩa là module_1 chỉ được nhập 1 lần trong 1 phiên làm việc đó. 
# Bây giờ nếu bạn sửa đổi code trong module_1 bạn phải nạp lại nó. Để làm điều này bạn phải khởi động lại trình thông dịch, 
# nhưng cách này có vẻ không ổn lắm.

# Python cung cấp cách thông minh hơn để làm điều này. 
# Bạn có thể sử dụng hàm reload() trong module imp để nạp lại module_1, như dưới đây:

# >>> import module_1
# Code đã hoạt động
# >>> import module_1
# >>> import module_1
# >>> import module_1
# >>> import imp
# >>> imp.reload(module_1)
# Code đã hoạt động


#Hàm dir()
# Hàm dir() trong Python được sử dụng để tìm ra các tên được định nghĩa trong 
# một module. Ví dụ, bạn định nghĩa hàm them() trong ví dụ ban đầu.
import module
print(dir(module))
print(module.__name__)

# Package
# Khi chương trình đang code ngày càng lớn với rất nhiều module, chúng ta sẽ đặt những module giống nhau vào một package, 
# và những nhóm module khác vào package khác. Điều này giúp dễ dàng quản lý chương trình hơn và nó cũng dễ hiểu hơn.

# Nếu như thư mục có thể chứa các thư mục con thì package cũng vậy, trong một package có thể có package con và các module khác.

# Một thư mục phải chứa file có tên __init__.py để Python hiểu thư mục này là một package. File này có thể để trống, 
# nhưng thông thường các lập trình viên thường đặt code khởi tạo cho package ở đây.