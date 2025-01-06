import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email sender and recipient
sender_email = "vinit.world2015@gmail.com"
receiver_email = "007.vinit@gmail.com"
password = "rugjxvfisladdtpz"

# Create the email subject and body
subject = "Test Email"
body = "This is a test email sent from Python."

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add the body text to the email
message.attach(MIMEText(body, "plain"))

# SMTP server configuration (for Gmail in this case)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Send the email
try:
    # Establish a secure session with Gmail's SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login to the email account
        text = message.as_string()  # Convert the message to string format
        server.sendmail(sender_email, receiver_email, text)  # Send the email

    print("Email sent successfully!")

except Exception as e:
    print(f"Error occurred: {e}")
