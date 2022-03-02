#Write a program to accept ID, fetch the document from collection, copy it in another collection "outofstock" and delete the document from the "mobiles" collection
from pymongo import MongoClient
import urllib.parse
import pymongo

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobile"]
col=db["outofstock"]

id=int(input('Enter mobile ID : '))
qr={}
qr["id"]=id
print(qr)

for doc in coll.find(qr):
    print(doc)
    col.insert_one(doc)
    coll.delete_one(doc)

    print("Document Copied and Deleted Successfully!")




