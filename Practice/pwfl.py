# subprocess_os_system.py
import subprocess

LOF = subprocess.run(['ls', '-alrt' ])
print('returncode:', LOF.returncode)
