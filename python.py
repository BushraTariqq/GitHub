import smtplib
import csv, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmailUser = 'username@gmail.com'
gmailPassword = 'Gmail Password'

message = f"""
Your Message here
"""

def sendEmail(name, email):
    msg = MIMEMultipart()
        msg['From'] = f'"Your Name" <{gmailUser}>'
            msg['Subject'] = "Subject for the Email"
                msg.attach(MIMEText(message))
    recipient = f'\"{name}\" <{email}>'
        msg['To'] = recipient
    try:
            mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                    mailServer.ehlo()
                            mailServer.starttls()
                                    mailServer.ehlo()
                                            mailServer.login(gmailUser, gmailPassword)
                                                    mailServer.sendmail(gmailUser, recipient, msg.as_string())
                                                            mailServer.close()
                                                                    print ('Email sent!')
                                                                            time.sleep(5)
                                                                                except:
                                                                                        print ('Something went wrong...')
with open("responses.csv") as file:
    reader = csv.reader(file)
        # Skipping the first row with the titles
            next(reader)
                for row in reader:
                        sendEmail(row[1], row[2])