import openpyxl

wb = openpyxl.load_workbook('octobre.xlsx')
print(wb.sheetnames)