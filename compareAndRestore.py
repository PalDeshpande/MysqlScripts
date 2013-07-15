import MySQLdb
import os
from platform import system
import platform
import fetchSQL

user = 'root'
passwd = 'root123'
host = 'localhost'

conn = MySQLdb.connect (host, user, passwd)

cursor = conn.cursor()

exe_path = r'""C:\Program Files (x86)\MySQL\MySQL Workbench CE 5.2.47\utilities""'


cmd =  "mysqldbcompare.exe --server1=local:root123localhost sakila:test0 --run-all-tests  --skip-object-compare  --skip-diff --difftype=sql > C:\\Users\\pallavi.keskar\\Desktop\\bk2\\backup.sql"

print cmd

os.chdir("C:\Program Files (x86)\MySQL\MySQL Workbench CE 5.2.47\utilities")
    
print "Comparing databases to get incremental backup........................"
os.system(cmd) 

print "Incremental backup process completed....."


