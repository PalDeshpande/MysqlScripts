
import os.path
import sys
import MySQLdb
import paramiko

#-----------------------------------------------------------------------
# Script name: SFTP Upload Script
# Author: Pallavi Keskar
# Date: July 8th, 2013
# 
# Description: This script can be used to upload a file to a remote 
# SFTP server.  It expects these parameters:
#
#    host_address: The remote server to which the file will be uploaded
#    username: The username with permission to connect to the server
#    password: The password for the username
#    local_filename: The full path to the local file to upload
#    remote_path: The path on the remote server where the file should be put
#-----------------------------------------------------------------------

host = ''
username = ''
password = ''
local_file_path = '' 
remote_file_path= ''

    # Does the local file exist?  If not, error and exit
if os.path.exists(local_file_path) is False:

    print "** Error: File " + local_file_path + " does not exist\n\n\n"
    sys.exit()

else:
    try: 
            # open Paramiko's SSH transport:
        transport = paramiko.Transport((host, 22))

            # authenticate with supplied credentials:
        transport.connect(username = username, password = password)

            # start SFTP Client from SSH transport:
        sftp = paramiko.SFTPClient.from_transport(transport)

            # upload the file:
        sftp.put(remote_file_path, local_file_path)
         
        print "Fule has been pushed to Sftp server successfuly"
        
    except MySQLdb.Error, e: 
        print "Error %d: %s" % (e.args[0], e.args[1]) 
            #Close connections:
        sftp.close()
        transport.close()
        sys.exit (1)
        
            ## ToDo: Add better exeption handling:

       

        #Close connections:
    sftp.close()
    transport.close()