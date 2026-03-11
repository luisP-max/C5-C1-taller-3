from collections import Counter
from user import register_sales

def calculate_totals(sales):
    """
    Function to calculate total quantities per product and total revenue.
    Uses Counter for efficient quantity summation.
    Returns quantities (Counter) and total_revenue (float).
    """
    quantities = Counter()
    total_revenue = 0.0
    for sale in sales:
        quantities[sale['product']] += sale['quantity']
        total_revenue += sale['price'] * sale['quantity']
    return quantities, total_revenue

def generate_summary(quantities, total_revenue):
    """
    Function to generate and print the daily sales summary.
    """
    print("=== DAILY SALES SUMMARY ===")
    for product, qty in quantities.items():
        print(f"Product: {product}")
        print(f"Total quantity sold: {qty}")
    print(f"Total revenue: ${total_revenue:.2f}")
    
    
def generate_summary(quantities, total_revenue):
    """
    Function to generate and print the daily sales summary.
    """
    print("=== DAILY SALES SUMMARY ===")
    for product, qty in quantities.items():
        print(f"Product: {product}")
        print(f"Total quantity sold: {qty}")
    print(f"Total revenue: ${total_revenue:.2f}")
