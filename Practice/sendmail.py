# First, becuase I do not want to record password info or set up a dummy gmail
# I'm going to start a SMTP debug on localhost to run with python
# The command to start it is python -m smtpd -c DebuggingServer -n localhost:1025
# I was going to check to see if it was running and if not start it but this was distracting from main goal of sending a gmail so I have parked 
# that idea for now & just started the process in the background on a terminal
# So for this program to run you will need to have executed the command -m smtpd -c DebuggingServer -n localhost:1025 on your terminal first
# My primary reference was realpython.com

#import subprocess
#subprocess.Popen(['python', '-m', 'smtpd', '-c', 'DebuggingServer', '-n', 'localhost:1025' ])

import smtplib, ssl

smtp_server = "localhost"
port = 1025 # For starttls
sender_email = "gmitcsadele@gmail.com"
receiver_email = "your@gmail.com"  # Enter receiver address
message = """\
Subject: Hi .. 

This is the output of a python program using the smtp debugger process so I'm not really sending mail, my mail is just sent to the terminal, stdout."""

# Because we are running a background smtp python debugger against localhost port 1025 we don't need to supply user/pw
# I think this is only useful when you are learning to format different msg types and you don't want to be  using a login/password
try:
    server = smtplib.SMTP(smtp_server,port)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 



