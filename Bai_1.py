#Nhập một chuỗi kí tự từ bàn phím
#Nhập tên tập tin từ bàn phím
#Lưu chuỗi ký tự ở trên vào tập tin

import os

print("thư mục làm việc hiện tại:", os.getcwd())
print('thư mục gồm: ',os.listdir(os.getcwd()))

nhap = input('input something: ')
ten = input('input name of file: ')

f = open(ten,'r')
print('file ban đầu: ',f.read())

f = open(ten,'w')
f.write(nhap)

f = open(ten,'r')
print('file sau khi ghi dữ liệu: ',f.read())
