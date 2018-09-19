# CLASSES AND METHODS
class Store():
    products = []
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
 
    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product) 

    def print_products(self,store_name):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for i in self.products:
            if i.S_name.lower() == store_name:
                print(i)


class Product():
    def __init__(self,S_name ,name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.S_name = S_name
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        # your code goes here!
        return '\tProduct Name: %s\n\tDescription: %s\n\tPrice: %s\n' % (self.name,self.description,self.price)


class Cart():
    items = []
    prices = []
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.items = []
        self.prices = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.items.append(product)

    def get_total_price(self,products):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        self.prices = []
        total = 0
        for i in self.items:
            for j in products:
                if i.lower() == j.name.lower():
                    total += j.price
                    self.prices.append(j.price)

        return total

    def print_receipt(self,total):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        if total != 0:
            print("\nHere is your receipt:")
            for i in range(len(self.items)):
                print("- %s,  price: %s KD" % (self.items[i],self.prices[i]))
    
            print("\nThe total price is %s KD." % total)
        else:
            print("\n~Your receipt is empty~")

    def checkout(self,total):
        """
        Does the checkout.
        """
        # your code goes here!
        if total != 0:
            while True:
                x = input("Confirm?(yes/no): ")
                if x.lower() == "yes":
                    print("\nYou order has been placed.")
                    break
                elif x.lower() == "no":
                    print("\nYour order has been canceled.")
                    break
                else:
                    print("~Please confirm by either 'yes' or 'no'~")
