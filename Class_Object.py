class Banking:
  def __init__(self, balance):
    self.balance = balance
    
    
acc1 = Banking(1000)
print(acc1.balance)

acc2 = Banking(2000)
print(acc2.balance)