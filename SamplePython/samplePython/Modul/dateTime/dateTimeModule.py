import datetime

t = datetime.time(1, 2, 3)
print t
print 'hour  :', t.hour
print 'minute:', t.minute
print 'second:', t.second
print 'microsecond:', t.microsecond
print 'tzinfo:', t.tzinfo


print "\n ===================== date ====================="
today = datetime.date.today()
print today
print 'ctime:', today.ctime()
print 'tuple:', today.timetuple()
print 'ordinal:', today.toordinal()
print 'Year:', today.year
print 'Mon :', today.month
print 'Day :', today.day

print "\n ===================== variabel date ====================="
d1 = datetime.date(2008, 3, 12)
print 'd1:', d1
d2 = d1.replace(year=2009)
print 'd2:', d2

print "\n ===================== operasi terhadap date ====================="
today = datetime.date.today()
print 'Today    :', today
one_day = datetime.timedelta(days=1)
print 'One day  :', one_day
yesterday = today - one_day
print 'Yesterday:', yesterday
tomorrow = today + one_day
print 'Tomorrow :', tomorrow
print 'tomorrow - yesterday:', tomorrow - yesterday
print 'yesterday - tomorrow:', yesterday - tomorrow

tgl1 = datetime.date(2014,01,20)
tgl2 = datetime.date.today()
selisih = tgl2-tgl1
print tgl1, "-",tgl2, "=",selisih
print "selisih hari = ",selisih.days
print "\n ===================== komparasi date & time ====================="
import time

print 'Times:'
t1 = datetime.time(12, 55, 0)
print '\tt1:', t1
t2 = datetime.time(13, 5, 0)
print '\tt2:', t2
print '\tt1 < t2:', t1 < t2

print 'Dates:'
d1 = datetime.date.today()
print '\td1:', d1
d2 = datetime.date.today() + datetime.timedelta(days=1)
print '\td2:', d2
print '\td1 > d2:', d1 > d2


