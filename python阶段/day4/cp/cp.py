from sys import argv
fobj = open(argv[1],'w')
fobj.writelines('abc\njz\nqyt')
fobj.close()
fobj = open(argv[1],'r')
a = fobj.readlines()
fobj.close()
if len(argv) == 2:
    fobj = open(argv[1][:-4]+'-副本'+argv[1][-4:], 'w')
    fobj.writelines(a)
    fobj.close()
elif len(argv) == 3:
    fobj = open(argv[2],'w')
    fobj.writelines(a)
    fobj.close()