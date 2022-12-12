#Sinh ngẫu nhiên 1 danh sách gồm 1000 số nguyên trong khoảng (-1000 , 1000 )
#Nhập tên tập tin từ bàn phím
#Ghi danh sách trên vào tập tin theo quy tắc:
#--- 10 số trên một hàng
#--- các số phân cách nhau bởi dấu phẩy
#Đọc nội dung tập tin trên và in ra màn hình theo quy tắc:
#--- 10 số trên một hàng
#--- các số phân tách nhau bởi dấu Tab

import os
import random

danhsach=[]
while len(danhsach)<1000:
  a=random.randint(-10,10)
  danhsach.append(a)
danhsachstring = ''.join(map(str, danhsach))
print(type(danhsachstring))

print(danhsach)
print(danhsachstring)