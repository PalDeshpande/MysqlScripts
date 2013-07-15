import paramiko
import os

#-----------------------------------------------------------------------
# Script name: SFTP Upload Script
# Author: Pallavi Keskar
# Date: July 8th, 2013
# 
# Description: This script can be used to download a file from a remote 
# SFTP server.  It expects these parameters:
#
#    host_address: The remote server to which the file will be uploaded
#    username: The username with permission to connect to the server
#    password: The password for the username
#    local_filename: The full path to the local system to save the downloaded file
#    remote_path: The path on the remote server where the file is stored
#-----------------------------------------------------------------------

host = ''
username = ''
password = ''
local_file_path = '' 
remote_file_path= ''

transport = paramiko.Transport((host, 22))

        # authenticate with supplied credentials:
transport.connect(username = username, password = password)

        # start SFTP Client from SSH transport:
sftp = paramiko.SFTPClient.from_transport(transport)

# download the file:
sftp.get(remote_file_path, local_file_path)

        #Close connections:
sftp.close()
transport.close()