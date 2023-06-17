import requests
import sys

API = "https://api.coindesk.com/v1/bpi/currentprice.json"

if len(sys.argv) > 2:
    sys.exit("Usage: bitcoin.py <number>")

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(API)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
except requests.RequestException:
    sys.exit(f"Error requesting response from {API}")
except KeyError:
    sys.exit("Invalid key")
else:
    if "," in price:
        price = price.replace(",", "")

    total = float(price) * n
    print(f"${total:,}")
