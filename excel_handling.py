from openpyxl import *

new_table = False
for row in sheet.iter_rows(max_col=5):
    if row[0].value == "№":
        for cell in row:
            if cell.value != None:
                print(cell.value, end=" ")
        new_table = True

    elif row[0].value == None:
        new_table = False

    elif new_table == True:
        for cell in row:
            if cell.value != None:
                print(cell.value, end=" ")

    print()