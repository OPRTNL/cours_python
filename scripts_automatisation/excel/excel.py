import openpyxl

wb = openpyxl.load_workbook('octobre.xlsx')
print(wb.sheetnames)

sheet = wb['Feuil1']
print(sheet['A1'].value)