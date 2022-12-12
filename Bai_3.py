#Nhập tên tập tin từ bàn phím
#Nhập một chuỗi ký tự vào từ bàn phím
#Ghi chuỗi ký tự này vào cuối tập tin ở trên

import os

print("thư mục làm việc hiện tại:", os.getcwd())
print(os.listdir(os.getcwd()))

nhap = input('input something: ')
ten = input('input name of file: ')

f = open(ten,'r')
print('file ban đầu: ',f.read())

f = open(ten,'a')
f.write(nhap)

f = open(ten,'r')
print('file sau khi ghi dữ liệu: ',f.read())