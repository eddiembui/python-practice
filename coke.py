def main():
  soda_price = 50
  balance = soda_price
  
  while balance > 0:
    user_coin = check_input(balance)
    balance -= user_coin
  else:
    print(f"Change owed: {abs(balance)}")


def check_input(amount_due):
  while True:
    print(f"Amount Due: {amount_due}")
    coin_inserted = int(input("Insert a coin: "))
    if coin_inserted == 25 or coin_inserted == 10 or coin_inserted == 5 :
      return coin_inserted
 
 
main()