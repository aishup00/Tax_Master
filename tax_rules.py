import csv

TAX_FILE = 'tax_structure.csv'

def load_tax_rules():
    rules = {}
    with open(TAX_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rules[row['CountryCode']] = float(row['TaxRate'])
    return rules

def add_tax_rule(country_code, tax_rate):
    with open(TAX_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([country_code, tax_rate])
    print(f"Added/Updated tax rule for {country_code} with rate {tax_rate}%")

def calculate_tax(item_rate, country_code, tax_rules):
    if country_code != 'INDIA':
        return 0
    if item_rate > 2000:
        return item_rate * (tax_rules.get('INDIA', 10) / 100)
    return 0
