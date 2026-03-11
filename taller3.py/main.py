from collections import Counter
from user import register_sales
from calculate import calculate_totals, generate_summary

if __name__ == "__main__":
    
    sales = register_sales()
    quantities, total_revenue = calculate_totals(sales)
    generate_summary(quantities, total_revenue)
    print("===========================")