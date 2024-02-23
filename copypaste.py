#!/usr/bin/python3
import os
import shutil

#shutil.copy('/tmp/testfile', '/srv/testfile')
#shutil.move('/srv/testfile', '/tmp/centos/')
#shutil.move('/tmp/sachin', '/tmp/centos/sachin')
shutil.copytree('/tmp/linux', '/tmp/centos/devops/linux')
