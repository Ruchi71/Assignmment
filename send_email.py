import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# create sender email,reciever email,subject,body
fromaddr = "ruchi71choubey@gmail.com"
password = "ruchi@123"
subjj = input(str('Subject? '))

toaddr = input(str('Recipient? '))
# initiate the class
msg = MIMEMultipart()

msg['From'] = fromaddr
msg['Subject'] = subjj
msg['To'] = toaddr

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,password)

text = msg.as_string()

server.send_message(msg)
print('Email sent!')

server.quit()