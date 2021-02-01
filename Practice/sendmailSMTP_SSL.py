# The code example below prompts for the email senders email address & password as well as the recipients email address
# This just avoids any information being kept in this program

import smtplib

sender_email = input("Please enter Sender's  email: " )
password = input("Type Sender's email password and press enter: ")

receiver_email = input ("Please enter recipent's email address: ")

# For now the message is hardcoded

message = """\
Subject: Hi there

This message is sent from Python."""

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(sender_email,password)

server.sendmail(sender_email, receiver_email, message)
