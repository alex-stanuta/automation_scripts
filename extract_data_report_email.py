#Script that generates a report and send it as an e-mail from text files
#Uses functions from two scripts created previously

#report_email.py
#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

def process_data():
  fruit_data = ''
  for filetxt in os.listdir("/supplier-data/descriptions/"):
    path = os.path.join("/supplier-data/descriptions/", filetxt)
    file = open(path,'r')
    name = file.readline().strip()
    fruit_data += 'name: ' + str(name) + '<br/>'
    weight = file.readline().strip()
    fruit_data += 'weight: ' + str(weight) + '<br/><br/>'
    file.close()

if __name__ == '__main__':
  today = date.today()
  title = 'Processed Update on ' + today.strftime('%B %d, %Y')
  fruit_data = process_data()
  reports.generate_report('/tmp/processed.pdf', title, fruit_data)
  message = emails.generate_email('automation@example.com', 'xxxxx@example.com', 'Upload Completed - Online Fruit Store', 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.', '/tmp/processed.pdf')
  emails.send_email(message)
