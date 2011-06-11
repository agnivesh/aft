import os
from lib.adb import AndroidDebugBridge

adb = AndroidDebugBridge()

dir = raw_input("Enter the location at which the workspace is to be created: ")
print dir
if not os.path.exists(dir):
    os.makedirs(dir)
os.makedirs("%s/database" % dir)
os.makedirs("%s/photos" % dir)
db = dir + "/database"
print db
photo = dir + "/photos"
print photo


result = adb.get_state()
result = result.strip('\n')
if result == "unknown":
	print "Not able to access device. Please check whether the device is connected properly and USB debugging mode is enabled"

adb.pull('/data/system/accounts.db',db)

##os.system('adb pull /data/system/accounts.db')
##/data/data/com.dropbox.android/databases/db.db