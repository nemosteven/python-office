import xlrd
from xlutils.copy import copy

rb = xlrd.open_workbook('test.xls')

# Copy and Add something
wb = copy(rb)
sh1 = wb.get_sheet(0)

sh1.write(2, 0, '王欢')
sh1.write(2, 1, '女')
sh1.write(2, 2, 92)
sh1.write(2, 3, 93)
sh1.write(2, 4, 93)


sh2 = wb.get_sheet(1)
sh2.write(1, 0, 278)

wb.save('test_modify.xls')
