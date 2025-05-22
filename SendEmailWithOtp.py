import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()

otp = random.randint(11111,99999)
name = input("Enter the Senders Name: ")
sender = os.getenv('sender_email') 
password =os.getenv('password') 

#print("Sender EmailId is ", sender)


recipient = input("Enter the Senders Email Id: ")
subject = "OTP Verification For Accessing the NIT Files!!!"
body = f"Dear {name},\n Your confidential OTP to access the Data Analytics 5:30 PM batch - NIT batch files is - {otp}."

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    #msg['To'] = ', '.join(recipients)
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipient, password)

userinput = input("Please enter the OTP sent to your email: ")
if userinput == str(otp):
    print("✅ OTP verified successfully!")
else:
    print("❌ Incorrect OTP.")