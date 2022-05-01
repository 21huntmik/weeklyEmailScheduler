import smtplib

gmail_user = "missionarymailwebapp@gmail.com"
gmail_password = "mobat&them"
to = "mhunt@missionary.org"
subject = "Test Test 1 2 3"
body = "I hope that this works. If it does, than that's great."

try:
	smtp = smtplib.SMTP("smtp.gmail.com", 587)
	smtp.starttls()
	smtp.login(gmail_user, gmail_password)
	smtp.sendmail(gmail_user, to, body)
	smtp.quit()
	print("Email sent!")
except Exception as ex:
	print("Something went wrong ", ex)
