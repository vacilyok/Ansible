#!/usr/bin/python
import os
from datetime import datetime

os.chdir("/Ansible/switch")

filename = str(datetime.date(datetime.now()))+"-"+ str(datetime.time(datetime.now()))+'.zip'
filedir = "/var/lib/tftpboot/switch"

# ************************************************************
# Run Ansible playbook
command = "ansible-playbook all_switch.yml"
os.system(command)


# ************************************************************
# Archive file
command = "zip -r /var/lib/tftpboot/archive/{} {} ".format(filename, filedir)
os.system(command)


# ************************************************************
# sort array when zip file
zip_files = []
listFiles = os.listdir(filedir)
for fl in listFiles:
    if "zip" in fl:
	zip_files.append(fl)


# ************************************************************
# remove old file
if (len(zip_files)>10):
    os.remove("/var/lib/tftpboot/archive/"+zip_files[0])
#    print("Remove file  "+zip_files[0])

