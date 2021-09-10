#Pulpería
list_of_products = {
    'drinks': {"coke":5, "tropical":5, "pepsi":5, "cacique":3, "water":4},
    'desserts': {"cookies&cream":1, "lemon pie":6, "torta chilena": 10, "vanilla ice cream": 5},
    'cleaning': {"alcohol": 6, "clinex": 6, "cleaning wipes": 10, "gloves": 5}}  

#Choosing the products category
def category_of_products():
    product = input("What are you interested in buying? ")
    for i in list_of_products:
        if product == i: 
            print ("Here are the options:", (list_of_products[i]))
        
#Facts about the customer
print("Hello I hope you are doing good. Please let me get your information in oder to procceed with the purchase ")
customers_name = input("What is your name? ")
payment_method = input("What is your payment method? (Debit/Cash)" )
amount = int (input("How much money do you have? In dollars "))
#Buying steps
category_of_products()    



