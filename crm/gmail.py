# -*- coding: utf-8 -*-
import datetime
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

t = datetime.datetime.now()

mail_server = 'smtp.gmail.com:587'
from_addr = 'CRM crm@blackinntech.com'
	# Credentials (if needed)
username = 'karazu20@gmail.com'
password = 'cbi%1985'

def sendMail (to_addr, ejecutivo, url):
	print 'sendMessage'
	themsg = MIMEMultipart('alternative')
	themsg['Subject'] = 'Cuenta de CRM'
	themsg['To'] = to_addr
	themsg['From'] = from_addr


	html = '''
		<html>
			<head></head>
			<body>
				
				<br>
				<h3>Cuenta CRM</h3>
				<p>
					Estimado <b>%s</b>, su cuenta de CRM se ha solicitado, por favor para terminar 
					el proceso de alta de su usuario ingrese al siguiente link del CRM :  
				</p>
				<p>
					<a href="%s"> %s </a>
				</p>
				<br>
				<p>
					Gracias!!.
				</p>
				
				<hr>
				
				<img align='center' src='http://crmbt.blacktrust.net/static/img/logo-2.png' width='200'>
			</body>
		</html>
	''' % ( ejecutivo,  url, url)

	#part1 = MIMEText(text, 'plain', 'utf-8')
	part2 = MIMEText(html, 'html', 'utf-8')

	#themsg.attach(part1)
	themsg.attach(part2)
	# The actual mail send
	server = smtplib.SMTP(mail_server)
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(from_addr, to_addr, str(themsg))
	server.quit()


