class Jar:
  # initialization method that has the private n (NUMBER OF COOKIES) and capacity instance variables
  def __init__(self, capacity=12):
    self._capacity = capacity
    if capacity < 0:
      raise ValueError("Enter a positive capacity!")

    self._n = 0

  # dunder str method returns the cookies as emojis
  def __str__(self):
    return f"🍪" * self._n

  # deposit method adds the n argument to the private instance variable n which becomes the sum of cookies in the jar
  def deposit(self,n):
    if self._n + n > self._capacity:
      raise ValueError("Exceeding capacity!")
    self._n += n

  # withdraw method removes n cookies from the sum of the private instance variable n
  def withdraw(self , n):
    if self._n - n < 0:
      raise ValueError("Too many to be removed!")
    self._n -= n

  # capacity getter method that reads the self.capacity and add additional logic to it
  @property
  def capacity(self):
    return self._capacity

  # size getter method reads the number of cookies and add additional logic to them
  @property
  def size(self):
    return self._n


def main():

  cookie_capacity = int(input("What capacity do you want in the jar: "))
  jar = Jar(cookie_capacity)
  print(jar.capacity)
  cookie_deposit = int(input("How many cookies do you want to put in the jar: "))
  jar.deposit(cookie_deposit)
  print(jar.size)
  print(jar)
  cookie_withdraw = int(input("How many cookies do you want to remove from the jar: "))
  jar.withdraw(cookie_withdraw)
  print(jar.size)
  print(jar)


if __name__ == "__main__":
  main()
