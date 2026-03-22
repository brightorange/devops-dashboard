import os
import socket
import getpass

def show_sysinfo():
    hostname = socket.gethostname()
    user = getpass.getuser()
    cwd = os.getcwd()

    print(f"Hostname: {hostname}")
    print(f"Current user: {user}")
    print(f"Current working directory: {cwd}")  
  
