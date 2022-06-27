
# Python program to read
# json file
  
  
import json
from unicodedata import category
  
# Opening JSON file
f = open('result.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['list'][0:1000000000]:
    text = "'" + i["name"] + "',"
    with open('copyToMain.txt','a',encoding = 'utf-8') as f:
        print(text)
        f.write(text)
    
# Closing file
f.close()
