import xlrd,xlwt
import pickle
book = xlrd.open_workbook("练习.xlsx")
sheet1 = book.sheet_by_index(0)
data =[]
a = sheet1.nrows
for i in range(4,a):
    if i >= 76:
        cls = {}
        cls['name'] = sheet1.cell_value(i,0).strip()#移除空格
        data.append(cls)
    elif (i-1)%3 == 0:
        cls = {}
        name = sheet1.cell_value(i,0).strip()
        cls['teacher'] = sheet1.cell_value(i+1,2).strip()
        cls['con'] = [i for i in sheet1.row_values(i)[2:] if i != '']
        cls['room'] = sheet1.cell_value(i+2,2).strip()
        cls['name'] = name
        data.append(cls)
with open('data.txt','wb') as f:
    pickle.dump(data,f)
#读
du = xlwt.Workbook()
length = len(data)
mysheet = du.add_sheet('优逸客')
for m in range(0,length):
    if m>=24:
        mysheet.write(m, 0, data[m]['name'])
    else:
        mysheet.write(m, 2, data[m]['teacher'])
        mysheet.write(m, 1, data[m]['con'])
        mysheet.write(m, 3, data[m]['room'])
        mysheet.write(m, 0, data[m]['name'])
du.save('data.xls')
