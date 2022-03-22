import json
from flask import Flask, abort
from mock_data import catalog

app = Flask("Server")


@app.route("/")
def home():
    return "Hello from Flask"


@app.route("/me")
def about_me():
    return "Maira Quinones"



############ API ENDPOINT #############
@app.route("/api/catalog", methods=['get'])
def get_catalog():
    return json.dumps(catalog)


#post save 
@app.route("/api/catalog", methods=['post'])
def save_product():
    pass

#we wont need these: just practice
#GET /http://127.0.0.1:5000/api/catalog/count how many product exist

@app.route("/api/catalog/count")
def product_count():
    count = len(catalog)
    return json.dumps(count)

#GET api/catalog/total sum all the prices on all the products and return (prod) can be whatever you want
@app.route("/api/catalog/total")
def product_total():

    total = 0 

    for prod in catalog:
        total += prod['price']

    return json.dumps(total)

#GET 

@app.route("/api/product/<id>")
def get_by_id(id):
    #find the product with _id is equal to id
    for prod in catalog:
        if prod["_id"] == id:
            #return that product as json
            return json.dumps(prod)

    #if not found return...an erropr 404
    return abort(404, "No product found")

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

    cat = []
    for prod in catalog:
        category = prod["category"]
        if not category in cat:
            cat.append(category)

    return json.dumps(cat)
   

@app.get("/api/catalog/<category>")
def prod_by_category(category):
    result = []
    for prod in catalog:
        if prod["category"] == category:
            result.append(prod)

    return json.dumps(result)    

app.run(debug=True)
