
from collections import Counter

def register_sales():
    """
    Function to register multiple sales until the user decides to stop.
    Returns a list of sales, each as a dictionary.
    """
    sales = []
    another = 'y'
    while another.lower() == 'y':
        product = input("Enter product name: ")
        
        try:
            price = float(input("Enter unit price: "))
        except ValueError:
            print("Invalid input. Defaulting price to 0.0")
            price = 0.0
        
        try:
            quantity = int(input("Enter quantity sold: "))
        except ValueError:
            print("Invalid input. Defaulting quantity to 0")
            quantity = 0
        
        sales.append({'product': product, 'price': price, 'quantity': quantity})
        print(f"Sale registered: {quantity} x {product} at ${price:.2f} each.")
        
        another = input("Do you want to register another sale? (y/n): ")
    return sales
