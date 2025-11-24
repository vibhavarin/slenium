# import xlrd
#
# path=
#
# ## open the excel
# workbook = xlrd.open_workbook(path)
# print(workbook)   ## book object
#
# ####open the worksheet
# worksheet = workbook.sheet_by_name('')
# print(worksheet)    ##sheet object
#
# rows = worksheet.get_rows()
# print(rows)        ## generator object
#
# # for ele in rows:
# print(ele)
#
# for ele in rows:
#     print(ele[0],ele[1],ele[2])
#
# for ele in rows:
#     print(ele[0].value,ele[1].value,ele[2].value)
#
#
#
#
#
#
#
#
# ###########################################################
#
#
# import xlrd
# path = r''
#
# def excel_read():
#     workbook = xlrd.open_workbook(path)  ##book object
#     worksheet = workbook.sheet_by_name('red_data')  ##sheet object
#     rows = worksheet.get_rows()   ### generator object
#
#     header = next(rows)
#     reg = {}
#     for ele in rows:
#         reg{ele}
