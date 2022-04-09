import pymongo
import certifi

mongo_url = "mongodb+srv://Maira31:5683Class@cluster0.pdqwq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

db = client.get_database("MettaClothing")


## packages for DB connection
#python -m pip install Flask-PyMongo
#python -m pip install "pymongo[srv]"
#python -m pip install certifi
