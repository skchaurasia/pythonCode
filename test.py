#!/usr/bin/python3
import subprocess

#subprocess.run (['cp', '-p', '/etc/passwd', '/tmp/passwd'])
#subprocess.run ('rm -f /tmp/passwd', shell=True)

print('Enter the source path and destination path of which you want to copy')
sourcePath = input('Enter the source path with file name: ')
destPath = input('Enter the destinatin path with file name: ')

subprocess.run(['cp', '-p', sourcePath, destPath])
