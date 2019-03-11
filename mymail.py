#sending mail using python
import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='rashmithanu2000@gmail.com'
	receiver='rashmithanu2017@gmail.com'
	msg='forgot my password'
	s.login(sender,'7090688733')
	s.sendmail(sender,receiver,msg)
except:
	print("something went worng")
else: 
	print("msg sent")
	s.quit()