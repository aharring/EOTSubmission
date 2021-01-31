# The code example below creates a secure connection with Gmail’s SMTP server, 
# using the SMTP_SSL() of smtplib to initiate a TLS-encrypted connection. 
# The default context of ssl validates the host name and its certificates then  optimizes the security of the connection.
# One this is done a simple text email is sent
# Important OAuth2 was enabled to improve security. Instructions found here https://developers.google.com/gmail/api/quickstart/python


import smtplib, ssl

sender_email = "devprogtechtest@gmail.com"
receiver_email = "adele.harrington@gmail.com"
message = """\
Subject: Test Email from Python 

This message is sent from sendmailSMTP_SSL.py."""

port = 465  # For SSL

password = input("Type your password and press enter: ")
print(password)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("devprogtechtest@gmail.com", password)

server.sendmail(sender_email, receiver_email, message)
