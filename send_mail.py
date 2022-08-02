from pydoc import plain
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import constants as keys


def sendMail(toWho, subject, content):

    fromWho = keys.senderMail
    password = keys.passofsd
    
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.ehlo() 
    server.starttls() 

    server.login(fromWho, password)  

    massage = MIMEMultipart()

    massage["From"] = fromWho
    massage["To"] = toWho
    massage["Subject"] = subject

    body_text = MIMEText(content)
    massage.attach(body_text)
    
    server.sendmail(massage["From"], massage["To"],massage.as_string()) 
    print("Mail Basari Ile Gonderildi")
    server.close()
