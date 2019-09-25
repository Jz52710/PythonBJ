def copyy(*args,name):
    fobj = open(*args,'w')
    fobj.writelines('abc\njz\nqyt')
    fobj.close()
    fobj = open(*args,'r')
    a = fobj.readlines()
    fobj.close()
    print(a)
    fobj = open(name,'w')
    fobj.writelines(a)
    fobj.close()

