import xlwt

# Here we try to use specific format of text

# Style of Font: Times New Roman, red and bold
styleBR = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

# Style of Number: Save 2 decimal points
styleNum = xlwt.easyxf(num_format_str='#,##0.00')

# Style of Date: YYYY-MM-DD
styleDate = xlwt.easyxf(num_format_str='YYYY-MM-DD')

wb = xlwt.Workbook()

sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

sh1.write(0, 0, '姓名', styleBR)
sh1.write(0, 1, '性别', styleBR)
sh1.write(0, 2, '语文', styleBR)
sh1.write(0, 3, '数学', styleBR)
sh1.write(0, 4, '英语', styleBR)
sh1.write(0, 5, '日期')
sh1.write(1, 0, '夏明')
sh1.write(1, 1, '男')
sh1.write(1, 2, 90, styleNum)
sh1.write(1, 3, 91, styleNum)
sh1.write(1, 4, 92, styleNum)
sh1.write(1, 5, '2021-9-8', styleDate)
sh2.write(0, 0, 273, styleNum)

# Center the Content in the cell
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
style = xlwt.XFStyle()
style.alignment = alignment

# Merge the Cell of  A3 and B3, Center the Content
sh1.write_merge(3, 3, 0, 1, 'merge', style)

# Calculate the Sum of C2 and C3 cell
sh1.write(1, 6, xlwt.Formula("C2+D2+E2"), style)


wb.save('test_format.xls')



