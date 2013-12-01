import serial
try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time
import datetime

#Initialize the Serial connection in COM3 or whatever port your arduino uses at 9600 baud rate
ser = serial.Serial("/dev/some_arduino", 9600)
i = 1
didFindEvents = '0'
# #delay for stability while connection is achieved
time.sleep(5)
while i == 1:
     client = gdata.calendar.client.CalendarClient(source='gCal-watch-v1')
     client.ClientLogin('user@gmail.com', 'password', client.source)

     query = gdata.calendar.client.CalendarEventQuery()
     # quick way to RFC 3339 timestamp format
     query.start_min = datetime.datetime.utcnow().isoformat("T") + "Z"
     query.start_max = (datetime.datetime.utcnow() + datetime.timedelta(minutes=15)).isoformat("T") + "Z"
     print 'Date range query for events on Primary Calendar: %s to %s' % (query.start_min, query.start_max,)
     feed = client.GetCalendarEventFeed(q=query)
     for i, an_event in enumerate(feed.entry):
          print '\t%s. %s' % (i, an_event.title.text,)
          for a_when in an_event.when:
               didFindEvents = '1'
               print '\t\tStart time: %s' % (a_when.start,)
               print '\t\tEnd time:   %s' % (a_when.end,)
     ser.write(didFindEvents)
     # reset the finder
     didFindEvents = '0'
     print 'Waiting for '
     # wait 5 minutes before rechecking RSS and resending data to Arduino
     time.sleep(300)

