import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create an empty dictionary to store key-value pairs
key_value_dict = {}

# Open the file in read mode
with open('data.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Strip leading/trailing whitespace and split by the colon
        key, value = line.strip().split(':')
        
        # Optionally, strip the value to remove extra spaces
        key_value_dict[key.strip()] = value.strip()

# Email sender and recipient
sender_email = key_value_dict['sender_email']
receiver_email = key_value_dict['receiver_email']
password = os.getenv("APP_PASS")

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
