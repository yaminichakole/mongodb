
from pymongo import MongoClient
import pymongo
import urllib.parse

try:
    username=urllib.parse.quote_plus('yaminichakole37')
    password=urllib.parse.quote_plus('Chakole@123')
    client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
    db=client['shopping']
    coll=db['mobiles']
    print("conected succesfully!!")
except:
    print("sorry!!conection failed!!")

