import os
import subprocess

os_name = os.name
os_current_login = os.getlogin()

def createFile(name, login):
    new_file = open("C:\\temp\\tempfile.txt", "w")
    new_file.write(f"OS info: {name}\nLogin info: {login}\n")
    new_file.close()

    if os.path.isdir("C:\\Windows\\System32\\OpenSSH"):
        new_file = open("C:\\temp\\tempfile.txt", "a")
        new_file.write("SSH is installed.")
        new_file.close()
    else:
        new_file = open("C:\\temp\\tempfile.txt", "a")
        new_file.write("SSH is not installed :(")
        new_file.close()
    
createFile(os_name, os_current_login)