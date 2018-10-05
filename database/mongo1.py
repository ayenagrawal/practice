import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # pymongo.MongoClient("localhost",27017)
mydb = myclient["mydatabase"]  # myclient.mydatabase
mycol = mydb["collection1"]  # mydb.collection1
mycol.delete_one({'name': 'pqr'})
result = mycol.find().sort('name', -1)
for i in result:
    print(i)
print(myclient.list_database_names())
print(mydb.list_collection_names())
