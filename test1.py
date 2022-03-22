


def younger_person():
    ages= [12,42,32,50,56,14,78,30,51,89,12,38,67,10]

    solution = ages[0]
    for age in ages:
        if age < solution:
            solution = age
            
    print(solution)

def statistics():
    data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]
    #1 - how many elemtns are there in the list ----count += 1----
    count = 0
    for num in data:
        count = count + 1

    #2 - what is the sum of all the numbers
    total = 0
    for num in data:
        total = total + num
        #--- total += num ----is the same expressinon as above
    negetive = 0
    if num < 0:
        negetive =negetive = 1


    #3 - Sum the negetive numbers
    sum = 0
    for num in data:


    #4 Count how many are over 500
        over_500 = 0
        if(num >500):
            over_500 += 1
    

    print(f"sum:{count}")
    print(f"total:{total}")

def print_some_nums():
    #print the multiples of 10 up to 100
    for num in range(1,11):
        print(num*10)

    # the second # is the stoping condition, the third is the increment 
    for x in range(10,110,10):
        print(x)

print("Test test test")
younger_person()
statistics()
print_some_nums()
