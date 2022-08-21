import pymongo
client = pymongo.MongoClient("mongodb+srv://Naveen:naveen123@cluster0.pcnjvkb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data= {
    "name" : "naveen",
    "email" : "naveen@123",
    "subject" : ["datasciece", "Big Data", "data analytic"]
}
database = client["myinfo"]
collection = database['sudh']
record = collection.find()
for i in record:
    print(i)

data= collection.find({"name" : "sudh"})
for i in data:
    print(i)