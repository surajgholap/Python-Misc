import smtplib


conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('e*******@gmail.com', '*********')
conn.sendmail('*******@gmail.com', 'su****@gmail.com', 'Subject: HI\n\nhow you doing?')
conn.quit()
