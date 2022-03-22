#DATE: 3/21/22

from mock_data import catalog

#it is case sensetive but can be pase to not case sensetive
def find_prod():
    text = "dress"

    #1 for loop and print the titles for every product
    count = 0
    for prod in catalog:
        title = prod["title"]
        if text.lower() in title.lower():
            print(f"{title} ${prod['price']}")


def unique_cat():
    categories = []
    for prod in catalog:
        category = prod["category"]
        if not category in categories:
            categories.append(category)

    print(categories)




find_prod()
unique_cat()