#Write a program to accept ID and new price of the mobile. Update the document with new price. Display the document after updating.

from pymongo import MongoClient
import urllib.parse
import pymongo

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobile"]

id=int(input('Enter mobile ID : '))
qr={}
qr["id"]=id
print(qr)

price=float(input('Enter mobile new price : '))
ch={}
ch["new price"]=price
print(ch)

upd={"$set":ch}

coll.update_one(qr,upd)
print('mobile price updated...')


