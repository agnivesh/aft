import sqlite3
from datetime import datetime
import csv, codecs, cStringIO

class UnicodeWriter:
    
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)



def read_mmssms(dbase,report):
	db = sqlite3.connect("%s/mmssms.db" % dbase)
	c = db.cursor()
	c.execute("select _id, thread_id, address, person, datetime(date/1000,'unixepoch','localtime') as date, protocol, read, status, type, reply_path_present, subject, body, service_center, locked from sms")

	writer = UnicodeWriter(open("%s/mmssms.csv" % report, "wb"))
	writer.writerow(["ID", "Thread ID", "Address", "Person", "Date/Time", "Protocol" , "Read", "Status", "Type", "Reply Path Present", "Subject", "Body", "Service Center", "Locked"])
	writer.writerows(c)
	c.close()
	db.close()

def read_history(dbase,report):
	db = sqlite3.connect("%s/browser.db" % dbase)
	c = db.cursor()
	c.execute("select title, url, visits, datetime(date/1000,'unixepoch','localtime') as date from bookmarks where user_entered = 0 or user_entered=1;")

	writer = UnicodeWriter(open("%s/history.csv" % report, "wb"))
	writer.writerow(["Title", "URL", "Visits", "Date"])
	writer.writerows(c)
	c.close()
	db.close()

def read_account(dbase, report):
	db = sqlite3.connect("%s/accounts.db" % dbase)
	c = db.cursor()
	c.execute('select * from accounts;')

	writer = UnicodeWriter(open("%s/accounts.csv" % report, "wb"))
	writer.writerow(["ID", "Name", "Type", "Password"])
	writer.writerows(c)
	c.close()
	db.close()