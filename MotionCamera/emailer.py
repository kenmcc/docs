import sys
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me="motioncam@s3group.com"
to=None#"your.name@s3group.com"
if to is None:
   print "Need to specify who to send email to"
   sys.exit(1)

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'MOTION DETECTED'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = me
msg['To'] = to
msgText = MIMEText('See for yourself', "plain")
msg.attach(msgText)

filePointer = open("image.jpg", 'rb')
img = MIMEImage(filePointer.read())
filePointer.close()
msg.attach(img)

# Send the email via our own SMTP server.
s = smtplib.SMTP('localhost')
s.sendmail(me, to, msg.as_string())
s.quit()
