import smtplib
from email.message import EmailMessage

def send_user_email(subject, body, user_email, user_app_password):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = user_email
    msg['To'] = user_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user_email, user_app_password)
        smtp.send_message(msg)