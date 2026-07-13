import sys
import requests

def main():
  
  try:
    cmd_float = float(sys.argv[1])
    try:
      btc_response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=9d63a05d59ca96e6815d8d6a6e6062ed07db5476aa5c54727f6eb9560f3da15c")
      json_response = btc_response.json()
      data_dict = json_response['data']
      price_key = float(data_dict['priceUsd'])
      no_of_btcs = cmd_float * price_key
      print(f"${round(no_of_btcs, 4):,}")
    except requests.RequestException:
      sys.exit("API Error will be fixed")
   
   
  except ValueError:
    sys.exit("Command-line argument is not a number")
  except IndexError:
    sys.exit("Missing command-line argument")

main()