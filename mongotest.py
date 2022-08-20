import pymongo
client = pymongo.MongoClient("mongodb+srv://Naveen:naveen123@cluster0.pcnjvkb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name" : "naveen",
    "email" : "naveen@123",
    "surname" : "kumar"
}
db1= client["mongotest"]
coll = db1['test']
coll.insert_one(d)

