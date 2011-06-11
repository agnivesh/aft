import os
import re
from lib.adb import AndroidDebugBridge
import string

adb = AndroidDebugBridge()

def main():
	dir = raw_input("Enter the location at which the workspace is to be created: ")
	if not os.path.exists(dir):
		os.makedirs(dir)
	os.makedirs("%s/database" % dir)
	os.makedirs("%s/photos" % dir)
	db = dir + "/database"
	photo = dir + "/photos"
	
	result = adb.get_state()
	result = result.strip('\n')
	if result == "unknown":
		print "Not able to access device. Please check whether the device is connected properly and USB debugging mode is enabled"
	
	print "Extracting database"
	adb.pull('/data/system/accounts.db',db)
	adb.pull('/data/data/com.android.providers.telephony/databases/mmssms.db',db)
	adb.pull('/data/data/com.android.providers.contacts/databases/contacts2.db',db)
	adb.pull('/data/data/com.android.browser/databases/webviewCache.db',db)
	adb.pull('/data/data/com.android.browser/databases/webview.db',db)
	adb.pull('/data/data/com.android.browser/databases/browser.db',db)
	adb.pull('/data/data/com.android.providers.telephony/databases/telephony.db',db)
	
	print "Extracting photos"
	result = adb.shell("ls /sdcard/DCIM/Camera -l")
	f = open ("%s/list.txt" % photo, 'w')
	f.write(result)
	f.close()
	f = open ("%s/list.txt" % photo, 'r')
	line = f.readline()
	while line:
		if re.match(r"^*.jpg$", line):
			adb.pull("/sdcard/DCIM/Camera/%s" % line, photo)
		f.readline()
		
if __name__ == "__main__":
    main()
##os.system('adb pull /data/system/accounts.db')
##/data/data/com.dropbox.android/databases/db.db