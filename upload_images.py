#Script to upload an image to a django form

#supplier_image_upload.py
#!/usr/bin/env python3
import requests
import os

url = 'http://35.184.118.129/upload/'
os.chdir("/home/student-01-3e3ebab1336d/supplier-data/images")
for file in os.listdir():
  name, ext = os.path.splitext(file)
  if ext == '.jpeg':
    image_path = os.path.join("/home/student-01-3e3ebab1336d/supplier-data/images/", file)
    with open(image_path, 'rb') as opened:
      r = requests.post(url, files = {'file': opened})
