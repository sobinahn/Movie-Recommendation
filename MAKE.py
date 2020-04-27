from openpyxl import load_workbook

print('Opening results from the workbook...')

wb = load_workbook(filename = 'movie_optimization.xlsm', read_only=True)
ws = wb['result']
for row in ws.rows:
    for cell in row:
        print(cell.value)