# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.SENKWATE.com"  # Give your site a name

def welcome(): #+++++++++++++++++ Finish +++++++++++++++++
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)
#===========================================================================
def print_stores(): #+++++++++++++++++ Finish +++++++++++++++++
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for i in stores:
        print("-", i.name)
    print("Pick a store by typing its name. Or type 'checkout' to pay your bills\nand say your goodbyes:")
    
#===========================================================================
def get_store(store_name): #+++++++++++++++++ Finish +++++++++++++++++
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    name_list = []
    for i in stores:
        name_list.append(i.name.lower())

    if store_name in name_list:
        for i in stores:
            if i.name.lower() == store_name:
                return i
    else:
        return False
#===========================================================================
def pick_store(cart): #+++++++++++++++++ Finish +++++++++++++++++
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    total = 0
    while True:
        temp = input()
        temp_store = get_store(temp.lower())
        if temp_store != False:
            total = pick_products(cart, temp_store)
            if total != True:
                print_stores()
            else:
                break

        elif temp.lower() == "checkout":
            cart.print_receipt(total)
            cart.checkout(total)
            break
        else:
             print("~The name you entered does'nt exist on the option's list. Please choose the exists names~")
            
#===========================================================================
def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    total = 0
    picked_store.print_products(picked_store.name.lower())
    print("Pick the items you'd like to add in your cart by typing\nthe product name exactly as it shown above.")
    print("-Type 'back' to go back to the main menu where you can continue shopping.")
    print("-Type 'checkout' to proceed checkout directly without going back to the menu.")
    while True:
        temp = input()
        if check_product(picked_store.products,temp.lower()) == True:
            cart.add_to_cart(temp.lower())
            total = cart.get_total_price(picked_store.products)

        elif temp.lower() == "checkout":
            cart.print_receipt(total)
            cart.checkout(total)
            return True
        
        elif temp.lower() == "back":
            print("------------------------------")
            break
        else:
             print("~Please enter the exact product name as shown above~")

    return total
       
#===========================================================================
def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    pick_store(cart)
    
#===========================================================================
def thank_you(): #+++++++++++++++++ Finish +++++++++++++++++
    print("Thank you for shopping with us at %s" % site_name)
#===========================================================================
def check_product(products,p_name):
    name_list = []
    for i in products:
        name_list.append(i.name.lower())

    if p_name in name_list:
        return True
    else:
        return False
