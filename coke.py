coin_inserted = 0
soda_price = 50
def main():
  global soda_price
  balance = soda_price - coin_inserted
  check_input(balance)
  balance = soda_price - coin_inserted
  while balance > 0:
    check_input(balance)
    balance = balance - coin_inserted
  else:
    absolute_balance = abs(balance)
    print(f"Change owed: {absolute_balance}")

  

def check_input(amount_due):
  global coin_inserted
  global soda_price 
  y = True
  while y == True:
    
    print(f"Amount Due: {amount_due}")
    coin_inserted = int(input("Insert a coin: "))
    if coin_inserted == 25 or coin_inserted == 10 or coin_inserted == 5 :
      y = False
    else:
      y = True


  return coin_inserted

 



     

  
  
    



  


main()