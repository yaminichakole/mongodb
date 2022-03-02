#Write a program to accept price and display all documents having price less than the input value
from pymongo import MongoClient
import urllib.parse
import pymongo

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobile"]

price=float(input('Enter mobile price : '))

myquery={"Price":{"$lt":price}}
mydoc=coll.find(myquery)

print("Documents having price less than the input value is :")
for x in mydoc:
    print(x)