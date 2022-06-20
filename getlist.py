
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
# s1=data["list"][0:100]["name"]
for i in data['list'][0:100]:
    text = "'" + i["name"] + "',"
    with open('copyToMain.txt','a',encoding = 'utf-8') as f:
        print(text)
        f.write(text)
    
# Closing file
f.close()
