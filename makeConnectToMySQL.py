import os
import MySQLdb
import sys
from symbol import if_stmt
import csv

#-----------------------------------------------------------------------
# Script name: OS details Script
# Author: Pallavi Keskar
# Date: June 25th, 2013
# 
# Description: This script can be used to query remote servers to collect os realted information
#
#    host_address: The remote server where the databse resides
#    username: The username with permission to connect to the server
#    password: The password for the username
#    local_filename: The full path to the local file to upload
#    remote_path: The path on the remote server where the file should be put
#-----------------------------------------------------------------------

user = '***'
passwd = '***'
host = '***'

abs_path = 'C:\\Users\\pallavi.keskar\\Desktop\\backupNew\\uswdlra01.csv'
new_file = open(abs_path, 'wb')
fp = csv.writer(new_file)

COMMA = "','"

NEW_LINE = "\n"



try: 
    conn = MySQLdb.connect (host, 
                            user, 
                            passwd 
                            )    
    print "successful"
    cursor = conn.cursor()
except MySQLdb.Error, e: 
 print "Error %d: %s" % (e.args[0], e.args[1]) 
 sys.exit (1) 
 
 
if(cursor):
    print"got a cursor"
    
command = "SELECT image_type,os, ed, sp, target_hardware,hwarch INTO OUTFILE"
#cursor.execute(" SELECT image_type,os, ed, sp, target_hardware,hwarch INTO OUTFILE " +abs_path+ " FIELDS TERMINATED BY "+COMMA+" LINES TERMINATED BY "+NEW_LINE+" FROM de.deployment_osimage ORDER BY os,ed,sp ") 
cursor.execute("SELECT image_type,os,ed,sp,target_hardware, hwarch FROM de.deployment_osimage ORDER BY os,ed,sp")

results = cursor.fetchall()
"""
for result in results:
    print"printing results"
    print result

"""

"""
    #print  result
    
    fp.writerow(result)
   
"""
for result in results:
    
    fp.writerow(result)

        

cursor.close()
conn.close()