Android Forensic Toolkit
================================

Android Forensic Toolkit allows you to extract SMS records, call history, photos, browsing history, and password from an Android phone. It currently uses adb to pull the databases and photos from the phone and the rest of the processes are performed by python.

Prerequisites
-
* Python 2.7 
* [pyexiv2](http://tilloy.net/dev/pyexiv2/)

Announcements
-
Nothing for now, but keep checking this space.

Forensic Artefacts
-
<table>
<tr>
<th>Artefact</th><th>Status</th><th>Remarks</th>
</tr>
<tr>
<td>Accounts</td><td>Implemented</td><td>Passwords are available as plaintext only till Android version 2.3, current versions have hashed passwords.</td>
</tr>
<tr>
<td>Browsing History</td><td>Implemented</td><td> History only from the default browser, will add support for other browsers in later versions.</td>
</tr>
<tr>
<td>Browser bookmarks</td><td>Implemented</td><td>Bookmarks only from the default browser, will add support for other browsers in later versions.</td>
</tr>
<tr>
<td>Search history</td><td>Implemented</td><td>Search history for searches done through Google.</td>
</tr>
<tr>
<td>Browser Saved Passwords</td><td>In Progress</td><td>Only supports the default browser for now</td>
</tr>
<tr>
<td>Call Logs</td><td>In Progress</td><td></td>
</tr>
<tr>
<td>SMS History</td><td>In Progress</td><td></td>
</tr>
<tr>
<td>Contacts</td><td>In Progress</td><td></td>
<tr>
<tr>
<td>Social Networks</td><td>Planned</td><td>Planned support for the default apps from Facebook, Twitter, Google+ and Foursquare</td>
</tr>
<tr>
<td>Email</td><td>Planned</td><td> Initial support only for the default email client.</td>
</tr>
</table>
The table will be updated with further details as and when I add a new functionality.

The databases extracted from the device will be present in the databases folder and can be viewed using [SQLite Database Browser](http://sqlitebrowser.sourceforge.net/) or [SQLiteSpy](http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index) (I personally prefer the SQLiteSpy as SQLite Database Browser hasn't been updated in a long time).

A detailed explanation on what each database contains will soon be available in the wiki.

Supported Devices
-
Tested only on Android virtual machines, has support upto Android version 2.3.6. Please message me with the devices you have been able to get this working on.

Bugs & Oddities
-
* Python 2.7 comes with sqlite3 version 2.6.0 while Andriod 2.3.7 uses sqlite3 version 3.7.2, which causes it to return a "DatabaseError?: file is encrypted or is not a database" error. A workaround is to compile Python with the lastest version of SQLite Library. If anyone has suggestion, please feel free to log an issue with the solution.
* Start the adb server separately (use adb start-server) before you use the script. Added code to check and start it automatically before rest of the code is executed but it doesn't seem to work.

Acknowledgements
-
The ADB implementation is from Ryan Brady's [python-adb](https://github.com/rbrady/python-adb/) code.
