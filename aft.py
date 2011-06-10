import os
import shlex, subprocess
from subprocess import call

def call_adb (command)
	command_result = ''
	command_text = 'adb %s' % command
	results = os.popen(command_text, "r")
	while 1:
	    line = results.readline()
		if not line: break
		command_result += line
	command_result = command_result.strip(' \t\n\r')
	return command_result


def main():
	if command_result == "unknown":
		print "Not able to access device. Please check whether the device is connected properly and USB debugging mode is enabled"

if __name__ == "__main__":
    main()
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