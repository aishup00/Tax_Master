import csv
from datetime import datetime
from tax_rules import calculate_tax, load_tax_rules, add_tax_rule

SALES_FILE = 'sales_data.csv'

def add_transaction():
    tax_rules = load_tax_rules()
    
    date = datetime.now().strftime('%Y-%m-%d')
    customer = input("Enter Customer Name: ")
    country = input("Enter Country Code (e.g. INDIA, USA): ").upper()
    item = input("Enter Item Name: ")
    rate = float(input("Enter Item Rate: "))
    qty = int(input("Enter Quantity: "))
    
    item_amount = rate * qty
    tax_amount = calculate_tax(rate, country, tax_rules)
    total_amount = item_amount + tax_amount
    
    with open(SALES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, customer, country, item, rate, qty, item_amount, tax_amount, total_amount])
    
    print(f"\n✅ Transaction recorded successfully for {customer}")
    print(f"Item: {item}, Amount: {item_amount}, Tax: {tax_amount}, Total: {total_amount}")

def show_sales():
    with open(SALES_FILE, 'r') as file:
        print("\n--- Sales Records ---")
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    print("===== TAX MASTER =====")
    print("1. Add Transaction")
    print("2. Show All Sales")
    print("3. Add/Update Tax Rule")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_transaction()
    elif choice == '2':
        show_sales()
    elif choice == '3':
        country = input("Enter Country Code: ").upper()
        rate = float(input("Enter New Tax Rate: "))
        add_tax_rule(country, rate)
    else:
        print("Invalid choice.")
