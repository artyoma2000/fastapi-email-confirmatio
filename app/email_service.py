import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import HTTPException
from app.config import settings


def send_confirmation_email(recipient_email: str, token: str):
    try:
        message = MIMEMultipart()
        message['From'] = settings.SENDER_EMAIL
        message['To'] = recipient_email
        message['Subject'] = 'Email Confirmation'

        confirmation_url = f"http://localhost:8000/confirm-email/?token={token}"
        body = f"Please click the following link to confirm your email: {confirmation_url}"

        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.sendmail(settings.SENDER_EMAIL, recipient_email, message.as_string())
    except smtplib.SMTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
