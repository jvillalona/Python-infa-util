# -------------------------------------------------------------------------------------------------------------------------
# Script name  : infa_create_control_file.py
# Creation Date: 06/14/2018
# Author       : Juan Villalona
# Description  : This script will create the control file that is required when doing an import of a workflow
#              : It tells pmrep how to handle conflicts.
#              : It will create a file name: object_import_ctl.xml
#              : Input parameters: object type ("W","S"), workflow or session name, target folder, target repository name
# -------------------------------------------------------------------------------------------------------------------------

import os.path
import os
import sys
import string


#This function takes the following input parameters, "W - workflow|S - session", Source folders, Source Repository, target folder, target repository
#The source folder is a list because it can contain multiple folders.

def create_import_control_file(obj_type, src_folder_list, src_repository, tgt_folder, tgt_repository):
    print("in function create_import_control")
    print(obj_type, src_folder_list, src_repository, tgt_folder, tgt_repository)
    path = 'c:\INFA\object_import_ctl.xml'
    object_import = open(path, 'w')
    object_import.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    object_import.write('<!--IMPORTPARAMS This inputs the options and inputs required for import operation -->\n')
    object_import.write('<!--CHECKIN_AFTER_IMPORT Check in objects on successful import operation -->\n')
    object_import.write('<!--CHECKIN_COMMENTS Check in comments -->\n')
    object_import.write('<!--APPLY_LABEL_NAME Apply the given label name on imported objects -->\n')
    object_import.write('<!--RETAIN_GENERATED_VALUE Retain existing sequence generator, normalizer and XML DSQ current values in the destination -->\n')
    object_import.write('<!--COPY_SAP_PROGRAM Copy SAP program information into the target repository -->\n')
    object_import.write('<!--APPLY_DEFAULT_CONNECTION Apply the default connection when a connection used by a session does not exist in the target repository -->\n')
    object_import.write('<!--IMPORTPARAMS This inputs the options and inputs required for import operation -->\n')
    object_import.write('<!--FOLDERMAP matches the folders in the imported file with the folders in the target repository -->\n')
    object_import.write('<IMPORTPARAMS CHECKIN_AFTER_IMPORT="NO" CHECKIN_COMMENTS="" RETAIN_GENERATED_VALUE="YES" COPY_SAP_PROGRAM="YES" APPLY_DEFAULT_CONNECTION="NO">\n')
    #find out how man source folders are in the xml file
    list_count = len(src_folder_list)
    for indx in range(list_count):
        print("src_folder_list:%s" %src_folder_list[indx])
        if "_SHARED" in src_folder_list[indx]:
            object_import.write('<FOLDERMAP\n')
            print("SOURCEFOLDERNAME=\"%s\" SOURCEREPOSITORYNAME=\"%s\" " % (src_folder_list[indx], src_repository[0]), file=object_import)
            print("TARGETFOLDERNAME=\"%s\" TARGETREPOSITORYNAME=\"%s\"/>" % (src_folder_list[indx], tgt_repository), file=object_import)
            object_import.write('\n')
        else:
            object_import.write('<FOLDERMAP\n')
            print("SOURCEFOLDERNAME=\"%s\" SOURCEREPOSITORYNAME=\"%s\" " % (src_folder_list[indx], src_repository[0]), file=object_import)
            print("TARGETFOLDERNAME=\"%s\" TARGETREPOSITORYNAME=\"%s\"/>" % (tgt_folder, tgt_repository), file=object_import)
            object_import.write('\n')
    object_import.write('<!--Import will only import the objects in the selected types in TYPEFILTER node -->\n')
    object_import.write('<!--TYPENAME type name to import. This should comforming to the element name in powermart.dtd, e.g. SOURCE, TARGET and etc.-->\n')
    object_import.write('        <TYPEFILTER TYPENAME="SOURCE"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="TARGET"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="MAPPLET"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="MAPPING"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="TRANSFORMATION"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="CONFIG"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="TASK"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="SESSION"/>\n')
    object_import.write('        <TYPEFILTER TYPENAME="SCHEDULER"/>\n')
    if obj_type.upper() == "W":
       object_import.write('        <TYPEFILTER TYPENAME="WORKFLOW"/>\n')
       object_import.write('        <TYPEFILTER TYPENAME="WORKLET"/>\n')
    object_import.write('\n')
    object_import.write('<!--RESOLVECONFLICT allows to specify resolution for conflicting objects during import. The combination of specified child nodes can be supplied -->\n')
    object_import.write('<RESOLVECONFLICT>\n')
    object_import.write('<!--TYPEOBJECT allows objects of certain type to apply replace/reuse upon conflict-->\n')
    object_import.write('<!--TYPEOBJECT OBJECTTYPENAME="ALL" RESOLUTION="REPLACE"/ -->\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="SOURCE DEFINITION" RESOLUTION="REUSE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="TARGET DEFINITION" RESOLUTION="REUSE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="SESSION" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="MAPPING" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Scheduler" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Lookup Procedure" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Stored Procedure" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Expression" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Filter" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Aggregator" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Rank" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Normalizer" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Router" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Sequence" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Sorter" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="update strategy" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Custom Transformation" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Transaction control" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="External Procedure" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Joiner" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="SessionConfig" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Mapplet" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Shortcut" RESOLUTION="REUSE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Command" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Decision" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Email" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Event raise" RESOLUTION="REPLACE"/>\n')
    object_import.write('<TYPEOBJECT OBJECTTYPENAME="Event wait" RESOLUTION="REPLACE"/>\n')
    if obj_type.upper() == "W":
        object_import.write('<TYPEOBJECT OBJECTTYPENAME="WORKFLOW" RESOLUTION="REPLACE"/>\n')
        object_import.write('<TYPEOBJECT OBJECTTYPENAME="Worklet" RESOLUTION="REPLACE"/>\n')
    object_import.write('\n')
    object_import.write('</RESOLVECONFLICT>\n')
    object_import.write('</IMPORTPARAMS>\n')
    object_import.write('\n')
    object_import.close()

def getWorkflow(wk_file):
    # search through the xml file and get the folders and repository
    # return a list containing the source folders and source repository
    wk_f = "c:\INFA\EXPORT\%s.xml" % wk_file
    print("XML File passed in for importing is: " + wk_f)

    folder_list = list()
    repository_list = list()
    with open("%s" % wk_f,"rt") as in_file:
        for line in in_file:  # Store each line in a string variable "line"
            #Extract the folder names from the xml file
            if "FOLDER NAME=" in line:
               folder = line.split('"')
               folder_list.append(folder[1])
            #Extract the source repository name from the xml file
            if "REPOSITORY NAME" in line:
                rep = line.split('"')
                repository_list.append(rep[1])
    return folder_list, repository_list




