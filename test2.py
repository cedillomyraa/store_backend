

def test_dict():
    me = {
        "first": "Maira",
        "last": "Quinones",
        "age": 30,
        "hobbies":[],
        "address":{ 
            "street":"123 Elmo St",
            "city": "Denver, Co 80129"
        },
    }
    print(me["first"] + "" + me["last"])

    address = me["address"]
    print(address["street"])

    #check if key exist in dictionary
    if "age" in me:
        print ("Age exist")




print("---Dictionary Test---")
test_dict()

# # install packages----python -m pip install <name>

# create the venv---python -m venv venv

# activate the venv---win:---venv\Scripts\activate

