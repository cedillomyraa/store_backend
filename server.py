import json
from flask import Flask, abort, request
from mock_data import catalog
from config import db
from bson import ObjectId



app = Flask("Server")


@app.route("/")
def home():
    return "Hello from Flask"


@app.route("/me")
def about_me():
    return "Maira Quinones"


#######################################
############ API ENDPOINT #############
############ RETURN JSON ##############
@app.route("/api/catalog", methods=['get'])
def get_catalog():
    products = []
    cursor = db.products.find({})#cursor is a collection

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        products.append(prod)

    return json.dumps(products)


#post save 
@app.route("/api/catalog", methods=['post'])
def save_product():
    product= request.get_json()
    
    db.products.insert_one(product)
    print(product)

    #fix _id
    product["_id"] = str(product["_id"])
    
    return json.dumps(product)

#we wont need these: just practice
#GET /http://127.0.0.1:5000/api/catalog/count how many product exist

@app.route("/api/catalog/count")
def product_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count += 1

    return json.dumps(count)

#GET api/catalog/total sum all the prices on all the products and return (prod) can be whatever you want
@app.route("/api/catalog/total")
def product_total():
    cursor = db.products.find({})
    total = 0 

    for prod in catalog:
        total += prod['price']

    return json.dumps(total)

#GET 

@app.route("/api/product/<id>")
def get_by_id(id):
    #find the product with _id is equal to id
    prod=db.products.find_one({"_id":ObjectId(id)})

    if not prod:
          #if not found return...an erropr 404
        return abort(404, "No product found")

    prod["_id"]= str(prod["_id"])
    return json.dumps(prod)

    #for prod in catalog:
        #if prod["_id"] == id:
            #return that product as json
            #return json.dumps(prod)

    #if not found return...an erropr 404
    #return abort(404, "No product found")

#return the cheapest product api/product/cheapest
#end point
@app.route("/api/product/cheapest")
def product_cheapest():

    cheapest = catalog[0]
    #for loop
    for price in catalog:
        #compare the prices
        if price["price"] < cheapest["price"]:
            cheapest = price
        

    return json.dumps(cheapest)

#GET /api/categories
#should return a lsit of strings representing the unique categories
@app.route("/api/categories")
def product_categories():

    categories = []
    for prod in catalog:
        category = prod["category"]
        if not category in categories:
            categories.append(category)

    return json.dumps(categories)
   

@app.get("/api/catalog/<category>")
def prod_by_category(category):
    products = []
    cursor = db.products.find({"category":category})
    for prod in cursor:
        prod["_id"]= str(prod["_id"])
        products.append(prod)

    return json.dumps(products)    


@app.get("/api/abc")
def abc():
    return "Works"

@app.get("/api/someNumbers")#end point
def some_numbers():
    numbers = [] 
    for num in range(1,51):#return a list with numbers 1-50
        numbers.append(num)
    
    return json.dumps(numbers)


#######################################
#########Coupon Code Endpoints#########
#######################################
allCoupons = []

@app.route("/api/couponCode", methods=["GET"])#GET APIcoupon code: get the coupon from the request
def get_coupon():
    coupons = []
    cursor = db.coupons.find({})
    for code in cursor:
        code["_id"] = str(code["_id"])
        coupons.append(code)
    return json.dumps(coupons)

@app.route("/api/couponCode", methods=["POST"])#end point #create the post .api/couponCode
def save_coupon():
    coupon = request.get_json()
 #validate must contain code, discount, should have 5 character and not lower than () or greater than 50%
     #validate
    if not 'code' in coupon or not "discount" in coupon:
        return abort(400, "coupon not valid")

    #validate the value
    if len(coupon["dicount"])>50 or len(coupon["dicount"])<5 or len(coupon["code"])<5:
            return abort(400, "missing field, please complete")

    db.coupons.insert_one(coupon)
#fix _id
    coupon["_id"] = str(coupon["_id"])
    return json.dumps(coupon) #return the coupon Json
    

@app.route("/api/couponCode/<code>")
def get_coupon_by_code(code):

    coupon = db.couponCodes.find_one({"code": code})
    coupon["_id"] = str(coupon["_id"])
    return json.dumps(coupon)



    #coupon = request.get_json() #get the coupon from the request
    #coupon["_id"]=20 #assign an _id
    #allCoupons.append(coupon) #add to all coupons


#######################################
###########Users  Endpoints############
#######################################



@app.route("/api/users", methods=["GET"])
def get_users():
    all_users = []
    cursor = db.users.find({})
    for user in cursor:
        user["_id"] = str(user["_id"])
        all_users.append(user)
    return json.dumps(all_users)

@app.route("/api/users", methods=["POST"])#end point #create the post .api/couponCode
def save_user():
    user = request.get_json()
    db.users.insert_one(user)
    #validate
    if not 'userName' in user or not "password" in user or not "email" in user:
        return abort(400, "missing field, please complete all")

    #validate the value
    if len(user["userName"])<1 or len(user["password"])<1 or len(user["email"])<1:
            return abort(400, "missing field, please complete")

    user["_id"] = str(user["_id"])
    return json.dumps(user) #return the coupon Json
    

@app.route("/api/users/<email>")
def get_user_by_email(email):

    user = db.users.find_one({"email": email})
    if not user:
        return abort(404,"No user found")
    user["_id"] = str(user["_id"])
    return json.dumps(user)


@app.route("/api/login",methods=["POST"])
def validate_user_data():
    data = request.get_json()
    print(data)

    if not 'user' in data:
        return abort(400, "user required login")
    if not 'password' in data:
        return abort(400, "password invalid")

    user=db.users.find_one({"userName": data["user"], "password": data["password"]})
    if not user:
            abort(401,"No user found")
    user["_id"] = str(user["_id"])
    
    user.pop("password")#removes the password from dictionary
    return json.dumps(user)


app.run(debug = True)