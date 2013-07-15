import MySQLdb
import os
from platform import system
import platform


user='root'
passwd='ctsods'
host='10.140.145.52'

conn = MySQLdb.connect (host, user, passwd)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

results = cursor.fetchall()
cursor.close()
conn.close()

if(platform.system() == "Windows"):
    exe_path = r'""C:\Program Files\MySQL\MySQL Server 5.6\bin\mysqldump.exe""'
    exe_path_mysql = r'""C:\Program Files\MySQL\MySQL Server 5.6\bin\mysql.exe""'
elif(platform.system() == "Linux" ):
        exe_path = 'mysqldump'
        exe_path_mysql = 'mysql'
else:
            print "Unknown OS"

for result in results:
    backupfile=result[0]+".sql"
    cmd="echo 'Back up "+result[0]+" database to yourLocation/"+backupfile+"'"
    os.system(cmd)
    cmd=exe_path +" -u "+user+" -h "+host+" -p"+passwd+" --opt --routines --flush-privileges --set-gtid-purged=OFF --single-transaction --database "+result[0]+"  > C:\\Users\\pallavi.keskar\\Desktop\\remote\\test_"+backupfile
    os.system(cmd)