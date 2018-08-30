import smtplib as mail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def compose_and_send(fromaddr, frompass, toaddr, name):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "GSS website visit reminder"
    body = "Dear " + name + \
        ",\n\nThis is a gentle reminder to please visit our website as we see that you havent\n\n\nNote: " + \
        "This is an auto-generated email, in case of questions please contact " + \
        "info@example.gov.in or +918805577007\n\nBest Regards,\nGIS Team"
    msg.attach(MIMEText(body, 'plain'))
    send(msg, fromaddr, frompass, toaddr)


def send(msg, fromaddr, frompass, toaddr):
    text = msg.as_string()
    s = mail.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, frompass)
    s.sendmail(fromaddr, toaddr, text)
    print("email has been sent")
