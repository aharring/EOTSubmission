# I wanted to see how you could run an os command from inside a python script
# I referenced stackoverflow to understand I needed to import the subprocess command so I could execute the unix command ls -alrt
# subprocess_os_system.py
import subprocess

LOF = subprocess.run(['ls', '-alrt' ])
print('returncode:', LOF.returncode)
