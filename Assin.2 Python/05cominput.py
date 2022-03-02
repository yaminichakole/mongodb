#Write a program to take company as an input and display documents of all mobiles of the company

from pymongo import MongoClient
import urllib.parse
import pymongo

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobile"]

com=input('enter company :')
qr={}
qr['company']=com
print(qr)

for doc in coll.find(qr):
    print(doc)