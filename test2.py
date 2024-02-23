#!/usr/bin/python3

#f = open('/tmp/testfile', 'a')
#f = open('/tmp/testfile', 'w')
with open('/tmp/testfile') as f:
#content = f.read()
#content = f.readlines()
#content = f.write('Hey how are you?\nadded new line\n')
#print(content)
  fread = f.read().splitlines()
print(fread)
f.close()
