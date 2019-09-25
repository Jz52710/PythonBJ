import xlrd,xlwt
import pickle
sheel1 = xlrd.open_workbook('练习.xlsx')
xie = sheel1.sheet_by_index(0)
data =[]
a = xie.nrows
for i in range(4,a):
    if i >=76:
        cls = {}
        cls['name'] = xie.cell_value(i,0)
        data.append(cls)
        # print(cls)
    elif (i-1)%3 == 0:
        cls = {}
        cls['name'] = xie.cell_value(i,0).strip()
        cls['classCon'] = [i for i in xie.row_values(i)[2:] if i !='']
        cls['room'] = [i for i in xie.row_values(i+2,2)[2:] if i !='']
        cls['teacher'] = [i for i in xie.row_values(i+1,2) if i != '']
        data.append(cls)
# print(data)
with open('dataa.txt','wb') as f:
    pickle.dump(data,f)
#读
du = xlwt.Workbook()
length = len(data)
mysheel = du.add_sheet("qyt")
for m in range(0,length):
    if m >=24:
        mysheel.write(m,0,data[m]['name'])
    else:
        mysheel.write(m,0,data[m]['name'])
        mysheel.write(m,1,data[m]['classCon'])
        mysheel.write(m,2,data[m]['teacher'])
        mysheel.write(m,3,data[m]['room'])
du.save('qyt.xls')