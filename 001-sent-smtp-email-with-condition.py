import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_with_password():
    sender_email = "noreply@gmail.com"
    receiver_email = "norepy@gmail.com"
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    smtp_password = ""  # App password

    subject = "SMTP Email Test - With Password"
    html_body = """
    <html>
        <body>
            <h2>Email Sent via SMTP with Password</h2>
            <p>This message was sent using SMTP login credentials.</p>
        </body>
    </html>
    """

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(html_body, 'html'))

    try:
        print(f"Connecting to {smtp_host}:{smtp_port}...")
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.ehlo()
        server.starttls()
        print("Logging in...")
        server.login(sender_email, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("✅ Email sent successfully using password.")
    except Exception as e:
        print(f"❌ Failed to send email with password. Error: {str(e)}")


def send_email_without_password():
    sender_email = "minj1992@gmail.com"
    receiver_email = "minj1992@gmail.com"
    smtp_host = "localhost"
    smtp_port = 1025  # Use 25 or 1025 for testing with local SMTP server

    subject = "SMTP Email Test - Without Password"
    html_body = """
    <html>
        <body>
            <h2>Email Sent via SMTP without Password</h2>
            <p>This message was sent without SMTP login.</p>
        </body>
    </html>
    """

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(html_body, 'html'))

    try:
        print(f"Connecting to {smtp_host}:{smtp_port} (no login)...")
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.ehlo()
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("✅ Email sent successfully without password.")
    except Exception as e:
        print(f"❌ Failed to send email without password. Error: {str(e)}")


# 🔧 Control flow using these two flags
USE_WITH_PASSWORD = True
USE_WITHOUT_PASSWORD = False

# 🚀 Call the appropriate function based on flags
if USE_WITH_PASSWORD:
    send_email_with_password()
elif USE_WITHOUT_PASSWORD:
    send_email_without_password()
else:
    print("⚠️ No email option selected. Set one of the flags to True.")
