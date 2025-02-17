import requests
import sys


def main():


    url = 'https://api.coincap.io/v2/assets/bitcoin'
    try:
        response = requests.get(url)
    except requests.RequestException:
        print("Something's wrong with thw API.")
    else:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit('Command doesn\'t exist.')
        except IndexError:
            sys.exit('Please enter exactly argument.')
        else:
            bitcoin = float(response.json()['data']['priceUsd'])
            print(f'${(n * bitcoin):,.4f}')


main()
