class Category:

  def __init__(self, category):
    self.name = category
    self.ledger = [] # Creating dictionary to store values


  def deposit(self, amount, description=''):
    # Function to append items to the ledger
    self.ledger.append({'amount':amount, 'description':description})

  def withdraw (self, amount, description=''):
    # Function to withdraw funds from the ledger
    if self.check_funds(amount):
      self.ledger.append({'amount':-amount, 'description':description})
      return True
    return False

  def get_withdrawals(self):
    withdraw = 0
    for l in self.ledger:
      if l['amount']<0:
        withdraw += -l['amount']
    return withdraw

  def get_balance(self):
    # It returns the current balance
    bal = 0
    for l in self.ledger:
      bal += l['amount']
    return bal

  
  def transfer(self, amount, category_object):
 
    if self.withdraw(amount, "Transfer to "+category_object.name):
      category_object.deposit(amount, "Transfer from "+self.name)
      return True
    return False

  def check_funds(self, amount):
    fund = 0
    for l in self.ledger:
      fund += l['amount']
    if amount>fund:
      return False
    return True

  def __str__(self): 
    # Returns formatted output
    brk = '\n'
    title = self.name.center(30, '*') + brk
    list = ''
    for l in self.ledger:
      list += '{:<23}'.format(l['description'])[:23]
      t = '{:.2f}'.format(l['amount'])
      # for display '#######' if amount is too long
      t = '{:>7}'.format(t)[:7]
      list += t + brk 
    total = 'Total: ' + str(self.get_balance())
    return title + list + total

def create_spend_chart(categories):
  # Return a string that is a bar chart
  brk = '\n'
  title = 'Percentage spent by category' + brk

  data = {}   # sum of each category
  sum = 0     # sum over all categories
  longest = 0 
  for category in categories:
    if not category.name in data:
      data[category.name] = 0
    w = category.get_withdrawals()
    data[category.name] += w
    if len(category.name)>longest:
      longest = len(category.name)
    sum += w

  perc = {} 
  tuples = data.items() # dictionary
  for k,v in tuples:
    perc[k] = int(v/sum * 10) * 10 # 75,4 -> 70
  
  # Creating chart
  list = ''
  for lp in range(100,-10,-10):
    list += "{:>3}".format(str(lp))+'| '
    for k,v in perc.items():
      if lp<=v:
        list += 'o  '
      else:
        list += '   '
    list += brk
  
  sep = ('    {:->'+str(4+2*len(categories))+'}').format('') + brk

  legend = ''
  for i in range(longest):
    legend += '   '
    for category in categories:
      if i<len(category.name):
        legend += '  '+category.name[i]
      else:
        legend += '   '
    legend += '  ' + brk

  return title + list + sep + legend.rstrip() + '  '