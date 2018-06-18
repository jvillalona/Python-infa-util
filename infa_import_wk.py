#----------------------------------------------------------------------------------------------------------------------------------------
#Script name  : infa_import_wk.py
#Creation Date: 06/14/2018
#Author       : Juan Villalona
#Description  : This script takes in three input parameters as listed below under usage
#             : The valid environments are DEV, QA PROD, follow by DESTINATION FOLDER and OBJECT TYPE of workflow or
#             : session. It uses a file name workflows.txt, which contains the workflows to import.
#             : It also expects the xml files to be stored in the EXPORT directory
#             : The script will read the workflows.txt file and go into a for loop to load all of the workflows or
#             : session that are in this file. For every xml file that it finds in the EXPORT directory it
#             : do a pmrep objectimport to import into the Informatica Repository
#             : It requires an xml file:import_infa_obj_ctl.xml that contains the rules for importing the objects.
#             : This file is created by calling function: infa_create_control_file.getWorkflow and passing the workflow name
#             : It imports infa_create_control_file.py in order to call two of it functions
#             : Usage infa_import_wk.sh <DEV|QA|PROD> <DEST FOLDER> <OBJECT TYPE W|S>
#----------------------------------------------------------------------------------------------------------------------------------------

import os.path
import os
import sys
import string
# import the python script that creates the control file
import infa_create_control_file

def create_import_file():
	path = 'c:\INFA\EXPORT\object_import.txt'
	object_import = open(path,'w')
	object_import.write('This is a test to create a file first line\n')
	object_import.write('Second line\n')
	object_import.close()


#Check to see if the correct number of parameters are passed in
if len(sys.argv) != 4:
   print('Usage: infa_import_wks.py <DEV|QA|PROD> <DEST FOLDER> <OBJECT TYPE W|S>')
   quit()
   
ENV=sys.argv[1].upper()
TGT_FOLDER=sys.argv[2]
OBJ_TYPE=sys.argv[3]
XML_FILE="object_import_ctl.xml"

print("running infa_import_wks.py, ENV: %s, TARGET FOLDER: %s, OBJECT TYPE: %s" % (ENV, TGT_FOLDER, OBJ_TYPE) )

# Set environment variable
if ENV == 'DEV':
    INFA_SERVICE = 'DEV_OCX_RS'
    INFA_DOMAIN = "DOM_INFA_DEV"
    #use this password for Windows only
    #INFA_ADMIN_PASSWD = 'm2e2kX8mZ0al9TfK2okQURuXqYRHXgjLbjYH+lEPbI0='
    os.environ["INFA_ADMIN_PASSWD"] = "m2e2kX8mZ0al9TfK2okQURuXqYRHXgjLbjYH+lEPbI0="
    # For Unix only INFA_ADMIN_PASSWD = 'IOXCIEw8KauWHP4ORMb9B+GIshC5xVBisYP3Bkth9x0='
elif ENV == 'QA':
    INFA_SERVICE = 'QA_OCX_RS'
    INFA_DOMAIN = 'DOM_INFA_QA'
    INFA_ADMIN_PASSWD = 'j/h7cxVgRPWH03aORbhGjS0Z1b/Tn9Uwnm+/VoDDhCA='
elif ENV == 'PROD':
    INFA_SERVICE = 'PROD_OCX_RS'
    INFA_DOMAIN = 'DOM_INFA_PROD'
    INFA_ADMIN_PASSWD = '7vRgpqJrC6x57VFz6ANzpwEKlU8eNHPGmliMoc38EhA='
else:
    print('Usage: infa_import_wks.py <DEV|QA|PROD> <XML control file>')
    quit()

print("Environment variable INFA_ADMIN_PASSWD IS: " + os.environ["INFA_ADMIN_PASSWD"])

INFA_USER='administrator'
INFA_EXP_DIR='c:\INFA\EXPORT\\'
INFA_HOME = 'C:\Informatica\\10.1.0\clients\PowerCenterClient\client\\bin\\'

if os.path.isfile('c:\INFA\workflows.txt'):
    # Create a file handle for workflows.txt
     with open('c:\INFA\workflows.txt','r') as f_wks:
        WK = f_wks.readline()
        cnt = 1
        while WK:
            f_objimport = 'c:\INFA\EXPORT\object_import.txt'
            f_objimport = open(f_objimport, 'w')
            WORKFLOW = WK.strip()
            #print("Importing Informatica objects for: %s" % WORKFLOW)
            print ("*************************************************************************************************\n")
            wk_list = infa_create_control_file.getWorkflow(WORKFLOW)
            infa_create_control_file.create_import_control_file(OBJ_TYPE, wk_list[0], wk_list[1], TGT_FOLDER, INFA_SERVICE)
            print("objectimport -c C:\INFA\\%s -i C:\INFA\EXPORT\\%s.xml" % (XML_FILE, WORKFLOW), file=f_objimport)
            f_objimport.close()
            os.system("C:\Informatica\\10.1.0\clients\PowerCenterClient\client\\bin\pmrep.exe connect -r " + INFA_SERVICE + " -d " + INFA_DOMAIN + " -n " + INFA_USER + " -x infadom_OCX10")
            st_cmd = "C:\Informatica\\10.1.0\clients\PowerCenterClient\client\\bin\pmrep.exe run -f " + INFA_EXP_DIR + "object_import.txt" + " -o object_import.log -s "
            os.system(st_cmd)
            # read line
            WK = f_wks.readline()
else:
    print('c:\INFA\workflow.txt file does not exists, cannot continue')
    quit()




