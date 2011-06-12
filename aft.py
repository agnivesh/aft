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
	print "Extracting accounts.db"
	adb.pull('/data/system/accounts.db',db)
	print "Extracting mmssms.db"
	adb.pull('/data/data/com.android.providers.telephony/databases/mmssms.db',db)
	print "Extracting contacts2.db"
	adb.pull('/data/data/com.android.providers.contacts/databases/contacts2.db',db)
	print "Extracting webviewCache.db"
	adb.pull('/data/data/com.android.browser/databases/webviewCache.db',db)
	print "Extracting webview.db"
	adb.pull('/data/data/com.android.browser/databases/webview.db',db)
	print "Extracting browser"
	adb.pull('/data/data/com.android.browser/databases/browser.db',db)
	print "Extracting telephony.db"
	adb.pull('/data/data/com.android.providers.telephony/databases/telephony.db',db)
	
	print "Extracting photos"
	result = adb.shell("ls /mnt/sdcard/DCIM/Camera -l")
	result = result.strip('\n')
	print result
	f = open ("%s/list.txt" % photo, 'w')
	f.write(result)
	f.close()
	f = open ("%s/list.txt" % photo, 'r')
	print 1
	line = f.readline()
	while 1:
		print 2	
		result = re.search(r'.\.jpg$', line)
		print result
		if result:
			print "3-1"
			adb.pull('/mnt/sdcard/DCIM/Camera/'+line, photo)
			print line
		if not line:                        # or an empty string at EOF
			print "3-2"
			break
		line = f.readline()
		line.strip(' \t\n\r')
		print line

if __name__ == "__main__":
    main()
##os.system('adb pull /data/system/accounts.db')
##/data/data/com.dropbox.android/databases/db.db