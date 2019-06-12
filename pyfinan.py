import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('May 2019')

user_input = ''
counter = 0;
income_total = 0
expense_total = 0

desc_list1 = []
income_list = []

desc_list2 = []
expense_list = []

while user_input != 'z':
    temp = input('收入的描述是什麼?\n')
    if temp == 'z':
        break
    desc_list1.append(temp)
    income_list.append(float(input('收入金額是多少?\n')))
    sheet1.write(counter, 0, desc_list1[counter])
    sheet1.write(counter, 1, income_list[counter])
    income_total = income_total + income_list[counter]
    counter = counter + 1

counter = 0;
user_input = ''

while user_input != 'z':
    temp = input('費用的描述是什麼?\n')
    if temp == 'z':
        break
    desc_list2.append(temp)
    expense_list.append(float(input('費用金額是多少?\n')))
    sheet1.write(counter, 2, desc_list2[counter])
    sheet1.write(counter, 3, expense_list[counter])
    expense_total = expense_total + expense_list[counter]
    counter = counter + 1

sheet1.write(len(expense_list) + 2, 0, "這個月的收入是: "+ str(round(income_total-expense_total,2)))

wb.save('xlwt 收入.xls')