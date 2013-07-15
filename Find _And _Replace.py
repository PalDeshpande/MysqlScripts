from  tempfile import mkstemp
from shutil import  move
from os import remove, close

def Find_And_Replace():
    #create a temp file
    print"inside function"
    abs_path = 'C:\\Users\\dmuser\\Desktop\\BackupDump\\temp0.sql'
    inputFileName = 'C:\\Users\\dmuser\\Desktop\\BackupDump\\usphlra01_de.sql' 
    new_file = open(abs_path, "w")
    
    old_file = open(inputFileName, "r")
    
    
    
    string = "`de`"
    for line in old_file:
        if (string in line):
            print"replacing database name and writing"
            new_file.write(line.replace('`de`', '`usphlra01_de`'))
        else:
            print "writing as it is in file"
            new_file.write(line)
            
    new_file.close()
    #close(fh)
    old_file.close()
    remove(inputFileName)
    move(abs_path, inputFileName)
        
    
Find_And_Replace()