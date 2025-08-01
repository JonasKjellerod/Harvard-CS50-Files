import sys
import requests

try:
    if len(sys.argv) > 1:
        amount = float(sys.argv[1])
        data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        print(f'${data['bpi']['USD']['rate_float']*amount:,.4f}')
except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')





