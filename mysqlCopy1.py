#!/usr/bin/python


#modified on 06/18/2013

import MySQLdb
import os
from platform import system
import platform
from  tempfile import mkstemp
from shutil import  move
from os import remove, close

#array of user names passwords and host names for all the 5 datacenters
user=['***']
passwd=['***']
host=['***']

"""

conn = MySQLdb.connect (host, user, passwd)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

results = cursor.fetchall()
cursor.close()
conn.close()
"""
#determine the operating system befire executing the command ......

if(platform.system() == "Windows"):
    exe_path = r'""C:\Program Files\MySQL\MySQL Server 5.6\bin\mysqldump.exe""'
    exe_path_mysql = r'""C:\Program Files\MySQL\MySQL Server 5.6\bin\mysql.exe""'
elif(platform.system() == "Linux" ):
        exe_path = 'mysqldump'
        exe_path_mysql = 'mysql'
else:
            print "Unknown OS"
        


#preparing array of machine names

machines = ['uscrlra01', 'usphlra01', 'usscora01','camsgra01']
dump_sqls = []
DB_names = []

for i in range(4):
    print machines[i]
    string  = machines[i]+"_de"
    DB_names.append(`string`)
    print DB_names[i]
    i = i+1

#exe_path = r'""C:\Program Files\MySQL\MySQL Server 5.6\bin\mysqldump.exe""'


#array to hold cmd for each machine
cmdForEachHost = []


#preparing an array with commands for each machine to take the backup dump

    
for i in range(4):
    print "i am in here"
    backupfile=machines[i]+"_de.sql"
    dump_sqls.append(backupfile)
    print dump_sqls[i]
    #B_names.append("`"+machines[i]+"_de`")
    cmd= exe_path +" -u "+user[i]+" -h "+host[i]+" -p"+passwd[i]+" --opt --routines --flush-privileges --single-transaction --database de"\
   " --set-gtid-purged=OFF  > C:\\Users\\pallavi.keskar\\Desktop\\remote\\"+backupfile
    
    cmdForEachHost.append(cmd)
   #print cmdForEachHost[i]
    

##function to take mysqldump from the machines
def mysqldump_sql(*cmdForEachHostd):
    
    for i in range(4):
        cmdForEachHost[i]
        print "Taking mysqldump from machine" + machines[i]
        os.system(cmdForEachHost[i])
        print "dump from "+machines[i]+" is complete"
        

#method to restore databases from mysqldump
def restoreDB_from_mysqldump(*backupfile):
    for i in range(4):
        dump_path ='C:\\Users\\pallavi.keskar\\Desktop\\remote\\'+dump_sqls[i]
        print "restoring databe de from machine "+machines[i] +" using cackup file "+dump_sqls[i]
        
        DB_sql= dump_sqls[i]
        print"restoration in progress....."
        cmd = exe_path_mysql + " -u "+user+" -h "+host+" --password="+passwd+ " < C:\\Users\\pallavi.keskar\\Desktop\\remote\\" + DB_sql
        print (cmd)
        os.system(cmd)
    

# methos modifies the dump files to create the databse with name with respective machine

def Find_And_Replace(*backupfile):
    #create a temp file
    
    for i in range(4):
       
        print"inside function"
        abs_path = 'C:\\Users\\pallavi.keskar\\Documents\Aptana Studio 3 Workspace\\CopyDB\\' + dump_sqls[i]
        inputFileName = 'C:\\Users\\pallavi.keskar\\Desktop\\remote\\' + dump_sqls[i]

        new_file = open(abs_path, "w")
    
        old_file = open(inputFileName, "r")
    
    #check for the databse name in the dump file and replace it with new name that appends db name with machine name
        string = "`de`"
        for line in old_file:
            if (string in line):
                print"replacing database name and writing"
                new_file.write(line.replace('`de`', DB_names[i]))
            else:
                    print "writing as it is in file"
                    new_file.write(line)
            
        new_file.close()
    #close(fh)
        old_file.close()
        remove(inputFileName)
        move(abs_path, inputFileName)
    

#execute the methods to take dump, restore DB from dump 
#mysqldump_sql(cmdForEachHost) 
#Find_And_Replace() 
print " preparing dump files for restoring databases"
restoreDB_from_mysqldump(dump_sqls)
    
        
"""    
def dump_db(exec_path):
    for result in results:
        backupfile=machineName+result[0]+".sql"
    cmd= exe_path +" -u "+user+" -h "+host+" -p"+passwd+" --opt --routines --flush-privileges --single-transaction --database "\
    +result[0]+" > C:\\Users\\pallavi.keskar\\Desktop\\bk2\\"+backupfile
    print cmd
    os.system(cmd)
    # >mysql --user root -p < sakila.sql executed in same directory as sql file.
    #to take care of space e.g. 
"""