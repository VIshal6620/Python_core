import smtplib
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()
mailto:connection.login('vishalvish7099@gmail.com','wbsr eqvu ufmn abwa')
mailto:connection.sendmail('vishalvish7099@gmail.com','aniketsirota64@gmail.com','subject: this is the subject \n\n hello user')
print("Email sent")
connection.quit()

