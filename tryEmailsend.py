import smtplib


conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('erbabydriv@gmail.com', 'arihantreddit')
conn.sendmail('erbabydriv@gmail.com', 'surajgholap27@gmail.com', 'Subject: HI\n\nhow you doing?')
conn.quit()