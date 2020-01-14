# Mở file
f = open('test.txt')

# Xem chế độ mode khi mở file
# https://quantrimang.com/lam-viec-voi-file-trong-python-160073


f = open("test.txt") # mở file mode 'r' hoăc 'rt' để đọc
# f = open("test.txt",'w') # mở file mode ‘w’ để ghi
# f = open("img.bmp",'r+b') # mở file mode ‘r+b’ để đọc và ghi dạng nhị phân

f = open("test.txt",mode = 'r',encoding = 'utf-8')

# Đóng File
f.close()

# Tuy nhiên cách này chưa thực sự đảm bảo. Vẫn có trường hợp một số ngoại lệ xảy ra 
# khi chúng ta thực hiện các thao tác với file khiến chương trình tự động thoát ra mà không đóng tệp.
# Để đảm bảo hơn, bạn nên sử dụng khối lệnh try...finally (finally sẽ luôn luôn được thực thi bất 
# chấp có hay không ngoại lệ) ở đây.

try: 
    f = open('test.txt', encoding='utf8')
finally:
    f.close()

# Bằng cách này, ta có thể yên tâm file được đóng đúng ngay cả khi phát sinh ngoại lệ khiến chương trình dừng đột ngột.

# Một cách khác để đóng file là sử dụng câu lệnh with. Lệnh with cho chúng ta bảo đảm rằng file luôn luôn được đóng mà không cần biết những logic xử lý bên trong.

# Ghi file
with open("test.txt", 'w',encoding = 'utf-8') as f:
    f.write("Quantrimang\n")
    f.write("Kiến thức - Kinh nghiệm - Hỏi đáp\n\n")
    f.write("Quantrimang.com\n")
    # thực hiện các thao tác với tệp
# So sánh hai cách viết này thì chúng ta đã thấy rất rõ ràng rằng, sử dụng with cho chúng ta cách viết code ngắn gọn hơn hẳn.

# Đọc file trong python
f = open("test.txt",'r',encoding = 'utf-8')
a = f.read(12) # đọc 12 kí tự đầu tiên
print('Nội dung 11 kí tự đầu là:\n', (a))
b = f.read(35) # đọc 35 kí tự tiếp theo
print('Nội dung 35 kí tự tiếp theo là:\n', (b))
c = f.read() # đọc phần còn lại
print('Nội dung phần còn lại là:\n', (c))

# Dùng tell() và seek()
f = open("test.txt",'r',encoding = 'utf-8')
a = f.read(12) # đọc 12 kí tự đầu tiên
print('Nội dung là: \n', (a))

b = f.tell() # Kiểm tra vị trí hiện tại
print ('Vị trí hiện tại: ', (b))

f.seek(0) # Đặt lại vị trí con trỏ tại vị trí đầu file
c = f.read()
print('Nội dung mới là: \n', (c))

# Dùng readline()
# Phương thức này dùng để đọc từng dòng trong file:
f = open("test.txt",'r',encoding = 'utf-8')
a = f.readline()
print ('Nội dung dòng đầu: ', (a))
b = f.readline()
print ('Nội dung dòng 2: ', (b))
c = f.readline()
print ('Nội dung dòng 3: ', (c))
d = f.readline()
print ('Nội dung dòng 4: ', (d))

# Dùng readlines()
# Trả về toàn bộ các dòng còn lại trong file và trả về giá trị rỗng khi kết thúc file
f = open("test.txt",'r',encoding = 'utf-8')
a = f.readline()
print ('Nội dung dòng đầu: ', (a))
b = f.readlines()
print ('Nội dung các dòng còn lại: \n', (b))
c = f.readlines()
print ('Nội dung các dòng còn lại: \n', (c))

# Một số phương thức làm việc với File 
# PHƯƠNG THỨC	||  MÔ TẢ
# close()	        Đóng một file đang mở. Nó không thực thi được nếu tập tin đã bị đóng.
# fileno()	        Trả về một số nguyên mô tả file (file descriptor).
# flush()	        Xóa sạch bộ nhớ đệm của luồng file.
# isatty()	        Trả về TRUE nếu file được kết nối với một thiết bị đầu cuối.
# read(n)	        Đọc n kí tự trong file.
# readable()	    Trả về TRUE nếu file có thể đọc được.
# readline(n=-1)	Đọc và trả về một dòng từ file. Đọc nhiều nhất n byte/ký tự nếu được chỉ định.
# readlines(n=-1)	Đọc và trả về một danh sách các dòng từ file. Đọc nhiều nhất n byte/ký tự nếu được chỉ định. 
# seek(offset,from=SEEK_SET)	Thay đổi vị trí hiện tại bên trong file.
# seekable()	    Trả về TRUE nếu luồng hỗ trợ truy cập ngẫu nhiên.
# tell()	        Trả về vị trí hiện tại bên trong file.
# truncate(size=None)	Cắt gọn kích cỡ file thành kích cỡ tham số size.
# writable()	    Trả về TRUE nếu file có thể ghi được.
# write(s)	        Ghi s kí tự vào trong file và trả về. 
# writelines(lines)	Ghi một danh sách các dòng và file.


# Folder (Thư mục trong Python)
# Module os có được xây dựng để cung cấp các phương thức giúp bạn tạo, xoá 
# và thay đổi các thư mục

# Hiện thị thư mục hiện tại
import os

print(os.getcwd())
print(os.getcwdb())

# Thay đổi thư mục hiện tại
# os.chdir('D:\Learn\LearnPython\HiHi')
# print(os.getcwd())

# Danh sách thư mục và file
print(os.listdir())


# Tạo một thư mục mới
# os.mkdir('HiHi')

# Đổi tên thư mục hoặc tên file
# os.rename('HiHi', 'New HiHi')

# Xoá bỏ thư mục hoặc file
# os.remove('New HiHi')
# os.rmdir('New Hihi')

# phương thức rmdir() chỉ có thể xóa các thư mục rỗng
# loại bỏ một thư mục không rỗng, chúng ta có thể sử 
# dụng phương thức rmtree() bên trong module shutil.

# import shutil
# shutil.rmtree('New HiHi')


# Lỗi (Error)
# Ngoại lệ (Exception)
# Ngoại lệ được Python tạo ra
# Xem các ngoại lệ
locals()['__builtins__']

# Xem các ngoại lệ được xây dựng sẵn trong Python
# https://quantrimang.com/error-va-exception-trong-python-160166

# Xử lý ngoại lệ
# Ngoại lệ (Exception)
# Lỗi xảy ra trong quá trình thực thi một chương trình
# sử dụng try ... except

# VD1:
import sys

randomList = ['a', 0, 2]

for nhap in randomList:
    try:
        print("Phần tử: ", nhap)
        r = 1/int(nhap)
        break
    except:
        print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra.")
        print("Nhập phần tử tiếp theo")
        print()
print("Kết quả với phần tử ", nhap, " là: ", r)

# Xử lý cụ thể một ngoại lệ
"""
Ở ví dụ trên, không có một ngoại lệ cụ thể nào được đề cập đến trong mệnh đề except nên khi 
chương trình gặp ngoại lệ (dù là bất kì exception nào) thì chúng đều được xử lý theo một cách.
Ngoài cách đó ra, ta có thể chỉ định các ngoại lệ cụ thể cho khối lệnh except.
Cú pháp như sau:
try:
 # khối code lệnh try
except exceptionName:
 # khối code lệnh except

Tham số:
exceptionName là tên của các exception bạn nghĩ có khả năng xảy ra.
Một mệnh đề try có thể có nhiều mệnh đề except để xử lý chúng khác nhau.
Nếu khối lệnh trong try có 1 lỗi gì đó xảy ra thì chương trình sẽ tìm đến 
các except phía dưới, except nào thỏa mãn thì nó sẽ thực thi code trong khối except đó.

try :
 # khối code lệnh try

except ValueError:
 # code xử lý ValueError

except RuntimeError:
 # code xử lý RuntimeError
Bạn cũng có thể bắt nhiều exception trên một lần khai báo except bằng việc đặt các ngoại 
lệ cách nhau bởi một dấu phẩy ‘,’

try :
 # khối code lệnh try

except (TypeError, ZeroDivisionError):
 # code xử lý nhiều ngoại lệ
 # TypeError, ZeroDivisionError
"""

# Xây dựng một Exception
# Sử dụng raise là một cách sử dụng ngoại lệ trong python
try:
    x = input('Nhập một số trong khoảng 1-10: ')
    if x<1 or x>10:
        raise Exception
    print('Bạn vừa nhập một số hợp lệ :D')
except:
    print('Số bạn vừa nhập nằm ngoài khoảng cho phép mất rồi!')
