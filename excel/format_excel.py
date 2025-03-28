from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

wb = load_workbook('sales.xlsx')
ws = wb.active

# for cell in ws[2]:
#     cell.font = Font(bold=True)

# wb.save('fonted_excel.xlsx')
green_fill = PatternFill(start_color='00FF00',end_color='00FF00', fill_type='solid')

for row in ws.iter_rows(min_row=2, max_col=6, max_row=ws.max_row):
    if row[5].value > 500:
        for cell in row:
            cell.fill = green_fill

wb.save('fonted_excel.xlsx')

