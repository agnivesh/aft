import os
import re
from lib.adb import AndroidDebugBridge
import string
from lib.read_db import *

adb = AndroidDebugBridge()

def main():

	dir = raw_input("Enter the location at which the workspace is to be created: ")
	if not os.path.exists(dir):
		os.makedirs(dir)
	os.makedirs("%s/database" % dir)
	os.makedirs("%s/photos" % dir)
	os.makedirs("%s/reports" % dir)
	
	db = dir + "/database"
	photo = dir + "/photos"
	report = dir + "/reports"
	aphoto = "/mnt/sdcard/DCIM/Camera/"
	
	result = adb.get_state()
	result = result.strip('\n')
	if result == "unknown":
		print "Not able to access device. Please check whether the device is connected properly and USB debugging mode is enabled"
	
	print "Extracting databases:"
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

	print "\nExtracting photos:"
	result = adb.shell("ls /mnt/sdcard/DCIM/Camera")
	f = open ("%s/list.txt" % photo, 'w')
	f.write(result)
	f.close()
	
	regex = r'\S[^\r\n\t]*\.jpg'
	
	f = open("%s/list.txt" % photo,'r')
	content = f.read()
	fList = content.strip().split()

	regex = r'\S[^\r\n\t]*\.jpg'

	for x in range(0,len(fList)):
		if re.search(regex,fList[x]):
			adb.pull('/mnt/sdcard/DCIM/Camera/%s' % fList[x], photo)

	read_account(db, report)
	read_history(db, report)
	read_mmssms (db,report)
	
if __name__ == "__main__":
    main()