import requests

def convert_currency(amount, from_currency, to_currency):
    url = {"API KEY"}{from_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['result'] == 'success':
        rate = data['conversion_rates'].get(to_currency)
        if rate:
            return amount * rate
        else:
            return "Currency not supported."
    else:
        return "Error fetching exchange rates."

# Directly running the code
from_currency = input("From Currency (e.g., USD): ").upper()
to_currency = input("To Currency (e.g., EUR): ").upper()
amount = float(input(f"Amount in {from_currency}: "))

result = convert_currency(amount, from_currency, to_currency)

if isinstance(result, float):
    print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
else:
    print(result)
