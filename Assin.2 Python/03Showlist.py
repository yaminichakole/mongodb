#Write a program to show list of all documents from the collection
from pymongo import MongoClient
import urllib.parse
import pymongo

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobile"]

for dic in coll.find():
    print(list(dic.value()))