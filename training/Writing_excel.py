'''
To write in to the excel we use openpyxl
'''

from openpyxl import Workbook
# create new workbook
excel_workbook = Workbook()

# initialize the worksheet

worksheet = excel_workbook.active

# set the title for the worksheet(optional)

worksheet.title = 'piku'

# enter the data

worksheet['A1']= 'Name'
worksheet['B1']= 'Address'
worksheet['C1']= 'Email'

data_list = [['vibha','germany','v@gmail.com'],['A','C','A@gmail.com'],['B','C','B@gmail.com']]

for row in data_list:
    worksheet.append(row)

# save the excel_file
excel_workbook.save('piku.xlsx')

# save the file in different location
excel_workbook.save(r'C:\Users\Veetrag\PycharmProjects\selenium training\files\piku.xlsx')