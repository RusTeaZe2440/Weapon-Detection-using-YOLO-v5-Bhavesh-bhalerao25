import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def mail_bot():
    # Connection with the server
    server = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
    server.starttls()
    server.login('2020ca30f@sigce.edu.in','pwhgdhumldeybbae' )

    # Creation of the MIMEMultipart Object
    message = MIMEMultipart()

    # Setup of MIMEMultipart Object Header
    message['From'] = 'bhaleraobhavesh69@gmail.com'
    message['To'] = 'bhaveshbhalerao98@gmail.com'
    message['Subject'] = "Automated Email with Attachment"

    # Creation of a MIMEText Part
    textPart = MIMEText("This is my first plain text automated Email with an Attachment.\n\nAlessio", 'plain')

    # Creation of a MIMEApplication Part
    filename = "2.jpg"
    filePart = MIMEApplication(open(filename,"rb").read(),Name=filename)
    filePart["Content-Disposition"] = 'attachment; filename="%s' % filename

    # Parts attachment
    message.attach(textPart)
    message.attach(filePart)

    # Send Email and close connection
    server.send_message(message)
    server.quit()