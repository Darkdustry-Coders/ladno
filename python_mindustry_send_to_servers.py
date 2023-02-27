#!/bin/python3
import fcntl
import sys
import termios
import subprocess

#lol = subprocess.run(, stdout=subprocess.PIPE)
servers = subprocess.getoutput("ps -ef | grep 'java -jar ../' | tr -s ' ' | cut -d ' ' -f2")

command = sys.argv
del command[0]
command = " ".join(command)

for server in servers.split():
    try:
        with open(f'/proc/{server}/fd/0', 'w') as fd:
            for char in f"\n{command}\n":
                fcntl.ioctl(fd, termios.TIOCSTI, char)
            fd.close()
    except Exception as e:
        pass
