# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open("textfile", 'rb')
a= fp.read()
print "message nya adalah = ",fp.read()

# Create a text/plain message
msg = MIMEText(a)
fp.close()
print "============================="
print "setelah menggunakan MIMEText menjadi : \n", msg
print "============================="

#me == the sender's email address
me = "RizaldiKomar@gmail.com"
password = "KokMurah"
# you == the recipient's email address
you = "oki.priyadi07@gmail.com"

msg['Subject'] = 'The contents of textfile'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.gmail.com', 25)
s.starttls()
s.login(me,password)

s.sendmail(me, [you], msg.as_string())
s.quit()
