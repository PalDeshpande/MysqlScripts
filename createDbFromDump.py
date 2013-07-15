import os
import MySQLdb
from platform import system
import platform
import dircache
import subprocess




user='root'
passwd='root123'
host='localhost'


if(platform.system() == "Windows"):
    exe_path = r'""C:\Program Files\MySQL\MySQL Server 5.6\bin\mysql.exe""'
elif(platform.system() == "Linux" ):
        exe_path = 'mysql'
else:
    print "Unknown OS"
    
dump_path ='C:\\Users\\pallavi.keskar\\Desktop\\bk2\\world.sql' 
"""pathname = '.'
list = dircache.listdir(pathname)
i = 0
check = len(list[0])
temp = []
count = len(list)
print count
while count != 0:
  if len(list[i]) != check:
     temp.append(list[i-1])
     check = len(list[i])
  else:
    i = i + 1
    count = count - 1

print temp
"""
list1  = os.listdir("C:\\Users\\pallavi.keskar\\Desktop\\bk2\\")
    
i = 0
check1 = len(list1[0])
temp1 = []
count1 = len(list1)
print count1
while count1 != 0:
  print list1[i]
  if len(list1[i]) != check1:
     temp1.append(list1[i-1])
     check1 = len(list1[i])
  else:
    i = i + 1
    count1 = count1 - 1

print temp1


#preparing progressbar


#widgets = ['Test: ', Percentage(), ]

#testing progressbar functionality

for i in range(0,count1,1):
    print list1[i]
"""
count1 = len(list1)
i = 0
while count1 !=0:
    cmd = exe_path+" -u "+user+" -h "+host+" -p "+passwd+ " "+" < "C:\Users\pallavi.keskar\Documents\Aptana Studio 3 Workspace\CopyDB\output"+ temp1[i]"
    print cmd
    os.system(cmd)
    i = i + 1
    count1 = count1 - 1
    
   
cmd = exe_path+" -u "+user+" -h "+host+" --password="+passwd+ " < " + dump_path
print cmd
os.system(cmd)


"""
cmd2 =exe_path+" -u "+user+" -h "+host+" -p"+passwd+ " "+" < C:\\Users\\pallavi.keskar\\Desktop\\remote\\usphlra01_de.sql"
print cmd2
os.system(cmd2)
