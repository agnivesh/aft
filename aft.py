from lib.adb import AndroidDebugBridge

adb = AndroidDebugBridge()
result = adb.get_state()
result = result.strip(' \t\n\r')
if result == "unknown":
	print "Not able to access device. Please check whether the device is connected properly and USB debugging mode is enabled"


"""
dir = raw_input("Enter the location at which the workspace is to be created: ")
if not os.path.exists(dir):
    os.makedirs(dir)

results = subprocess.call(["adb", "get-state"])
print results
while 1:
	line = results.readline()
	if not line: break
	command_result += line

print command_result

if command_result == "unknown":
	print "Not able to access device. Please check whether the device is connected properly and USB debugging mode is enabled"
	exit()

	##os.system('adb pull /data/system/accounts.db')
##/data/data/com.dropbox.android/databases/db.db
"""