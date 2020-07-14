#Script that checks the health of the computer, by checking
#the disk space, the cpu usage, the available memory and the localhost
#If there is something wrong, an email is being sent

#health_check.py
#! usr/bin/env python 3
import shutil
import psutil
import socket
import emails

def check_disk_space(disk, min_percent):
  du = shutil.disk_usage(disk)
  percent_free = 100 * du.free / du.total
  if percent_free < min_percent:
    return False
  return True

def check_cpu_usage(max_percent):
  cpu = 100 * psutil.cpu_percent()
  if cpu > max_percent:
    return False
  return True

def check_memory(min_value):
  mem = psutil.virtual_memory()
  if (mem.available / 2**20) < min_value :
    return False
  return True

def check_localhost():
  if socket.gethostbyname('localhost') != '127.0.0.1' :
    return False
  return True

if __name__ == '__main__':
  if not check_disk_space ("/", 20):
    title = 'Error - Available disk space is less than 20%'
  if not check_cpu_usage (80):
    title = 'Error - CPU usage is over 80%'
  if not check_memory (500):
    title = 'Error - Available memory is less than 500MB'
  if not check_localhost ():
    title = 'Error - localhost cannot be resolved to 127.0.0.1'
  body = 'Please check your system and resolve the issue as soon as possible.'
  if title:
    message = emails.generate_email('automation@example.com', 'xxxxx@example.com', title, body)
    emails.send_email(message)
