#!/usr/bin/python3

f = open('/etc/passwd')
#content = f.read()
content = f.readlines()
print(content)
f.close()
