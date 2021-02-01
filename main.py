import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

from sms import send_sms


def send_email():
    html = Template(Path('Template/index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Ayush'
    email['to'] = '*****@gmail.com'
    email['subject'] = 'Python'

    email.set_content(html.substitute({'name':'Ayush'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('email id', 'password')
        smtp.send_message(email)
        print('sent mail')
        send_sms()
        print('sent sms')

send_email()