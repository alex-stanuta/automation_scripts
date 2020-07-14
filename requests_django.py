#Script that uploads data from different files to django form

#run.py
#!/usr/bin/env python3

import os
import requests

feed_dict = {}

os.chdir("/home/student-01-3e3ebab1336d/supplier-data/descriptions")
for filetxt in os.listdir():
  path = os.path.join("/home/student-01-3e3ebab1336d/supplier-data/descriptions/", filetxt)
  file = open(path,'r')
  name = file.readline().strip()
  feed_dict['name'] = name
  weight = file.readline().strip()
  feed_dict['weight'] = int(weight.split()[0])
  description = file.readline().strip()
  feed_dict['description'] = description
  filename, ext = os.path.splitext(filetxt)
  feed_dict['image_name'] = filename + ".jpeg"

  response = requests.post("http://35.184.118.129/fruits/", data = feed_dict)
  print (response)
  file.close()
