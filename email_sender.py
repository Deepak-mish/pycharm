import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = "kjndsvjnj@gmail.com"
to_address = ['hdbhbvs@gmail.com']

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = " ,".join(to_address)

msg['subject'] = 'just to check'
body = "the beast again rise up"

msg.attach(MIMEText(body,'plain'))

email = "YOUR EMAIL"
password = "YOUR PASSWORD"
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text = msg.as_string()
mail.sendmail(from_address,to_address,text)

mail.quit()
