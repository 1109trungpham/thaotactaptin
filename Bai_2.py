#Nhập tên tập tin từ bàn phím
#Đọc nội dung tập tin và in ra màn hình

import os

tentaptin = input('nhập tên file: ')
doc = open(tentaptin,'r')
print('đọc file',tentaptin,':',doc.read())