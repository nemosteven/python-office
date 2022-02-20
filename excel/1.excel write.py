import xlwt
import xlrd
from xlutils import copy

wb = xlwt.Workbook()

sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

sh1.write(0, 0, '姓名')
sh1.write(0, 1, '性别')
sh1.write(0, 2, '语文')
sh1.write(0, 3, '数学')
sh1.write(0, 4, '英语')
sh1.write(1, 0, '夏明')
sh1.write(1, 1, '男')
sh1.write(1, 2, 90)
sh1.write(1, 3, 91)
sh1.write(1, 4, 92)
sh2.write(0, 0, 273)

wb.save('test.xls')
