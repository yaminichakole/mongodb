#Write a program to accept ID, ram and rom. Update the document with new ram and rom of the model. (memory size – temp & permanent)

from pymongo import MongoClient
import urllib.parse
import pymongo

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobile"]

id=int(input('Enter mobile ID  : '))
qr={}
qr["id"]=id
print(qr)

ram=int(input('Enter mobile ram : '))
ch={}
ch["ram"]=ram
print(ch)

rom=int(input('Enter mobile rom : '))
cm={}
cm["rom"]=rom
print(cm)

upd={"$set":ch}
upd={"$set":cm}

coll.update_one(qr,upd)
print("ram Updated Successfully!!")

coll.update_one(qr,upd)
print("rom Updated Successfully!!")