#Write a python program to take input from the user and add employee data as a document in the collection (ex. ID, company, model,processor, screensize, ram,rom, connectivity, price, rating, etc.)

from pymongo import MongoClient
import urllib.parse
import pymongo


id=int(input('Enter ID:'))
com=input('enter company:')
mod=input('enter model name:')
cam=int(input('enter camera(MP):'))
scr=float(input('enter screensize:'))
ram=int(input('enter ram:'))
rom=int(input('enter rom:'))
pri=float(input('enter price:'))
rat=float(input('enter rating:'))

dic={}
dic["id"]=id
dic["company"]=com
dic["model name"]=mod
dic["camera"]=cam
dic["screensize"]=scr
dic["ram"]=ram
dic["rom"]=rom
dic["price"]=pri
dic["rating"]=rat

username=urllib.parse.quote_plus('yaminichakole37')
password=urllib.parse.quote_plus('Chakole@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.xyrbb.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client["shopping"]
coll=db["mobiles"]

coll.insert_one(dic)
print("New mobile added to MongoDB cloud collection")