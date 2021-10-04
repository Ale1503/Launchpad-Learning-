#Pulpería
list_of_products = [
  { 'Code': '1000', 'Name': 'Coke', 'Price': 5 },
  { 'Code': '1001', 'Name': 'Tropical', 'Price': 5 },
  { 'Code': '3001', 'Name': 'Alcohol', 'Price': 6 },
  { 'Code': '3002', 'Name': 'Cacique', 'Price': 10},
  { 'Code': '1212', 'Name': 'Komplete', 'Price': 15}
]

#Shopping cart  
cart = []
#Facts about the customer
def customer_information():
    print("Hello I hope you are doing well. Please let me get your information in oder to procceed with the purchase ")
    customers_name = input("What is your name? ")
    payment_method = input("What is your payment method? (Debit/Cash)" )
    amount = int (input("How much money do you have? In dollars "))

#Choosing the products category
def selection_of_products():
    purchase_step = input("Write the initial: [S]earch Product, [E]nter product code, [P]ay ")
    if purchase_step == 's':
        search_for_name()
    if purchase_step == 'e':
        search_for_code()
    if purchase_step == 'p':
        print (cart)
            
#Search for name
def search_for_name():
    product_chosen = input("Choose the name of the product ")
    for product in list_of_products:
        if product_chosen == product['Name']:
            cart.append(product['Name']),cart.append(product['Price']) 
            print("Item added"), print('These are your current products', cart)
            selection_of_products() 
     
#Search for code                    
def search_for_code():
    product_chosen = input("Choose the code of the product ")
    for product in list_of_products:
        if product_chosen == product['Code']:
            cart.append(product['Code']),cart.append(product['Price']) 
            print("Item added"), print('These are your current products', cart)
            selection_of_products()

customer_information()
selection_of_products()

##    - Ask if the user wants to enter the product code or wants to search for a product. 
##           [S]earch Product, [E]nter product code, [P]ay
##      -> For Search Product: Enter a string and show the user all the products that match that string (Code, Name and price).
##      -> For Enter product code: get the product code, look for the product with that code and add it to the shopping cart if it exists.

##      -> After adding a new product, show the current shopping cart and total amount due.
##      -> Ask again the first step. Repeat steps above if needed. If pay is chosen, check if the user can afford it (including taxes).
##      -> Show an error if the amount of money is less than the required. Show a Thank you message if the amount of money is ok. Show to the user if there is any money left.

##  OPTIONAL: be able to remove products from the shopping cart: [S]earch Product, [E]nter product code, [R]emove product from shopping cart or [P]ay.


