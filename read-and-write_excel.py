from openpyxl import load_workbook
wb = load_workbook(r'.\tk-colours.xlsx')  # 存成工作簿

sheet = wb.active  # 獲取目前執行的工作表
print(sheet.rows)  # generator object

list_2D = []
for n,item in enumerate(sheet.rows):
    if n == 0 :
        continue
    list_2D.append([item[0].value, item[1].value, item[2].value, item[3].value])

print(len(list_2D))


