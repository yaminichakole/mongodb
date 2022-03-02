#Write a program to take ID as input, search and display the document with mobile information

from pymongo import MongoClient
import urllib.parse
import pymongo

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobile"]

id=int(input('enter id'))
qr={}
qr['id']=id
print(qr)

for doc in coll.find(qr):
    print(doc)


