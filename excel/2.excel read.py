import xlrd

wb = xlrd.open_workbook('test.xls')
sh1 = wb.sheet_by_index(0)

# Information of Sheets
print('Number of Sheets:', wb.nsheets)
print('Name of Sheets:', wb.sheet_names())
print('Sheet by Index:', wb.sheet_by_index(0))
print('Sheet by Name:', wb.sheet_by_name('汇总'))
print(u'sheet %s Number of Rows and Cols: %d %d' % (sh1.name, sh1.nrows, sh1.ncols))

# Content of Cell
print('value of Cell in Row 1 Col 1 :', sh1.cell_value(1, 1))
print('value of Row 1 :', sh1.row(1))
print('value of Col 1 :', sh1.col(1))
print('Type of Cell in Row 1, Col 1 :', sh1.cell(1, 1).ctype)
print('(Here, 0-empty 1-string 2-number 3-date 4-boolean 5-error)')

# Traverse the Content
for sh in wb.sheets():
    for r in range(sh.nrows):
        print(sh.row(r))
