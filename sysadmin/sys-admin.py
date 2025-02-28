import os
import subprocess

# os.system("ls")
# subprocess.run(["ls", "-l"])

subprocess.run(["ls", "-l", "README.md"])

# Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


#  Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

