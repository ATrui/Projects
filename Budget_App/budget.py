class Category():
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": (amount), "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -(amount), "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, destination):
    if self.check_funds(amount) == True:
      self.withdraw(amount, description=f"Transfer to {destination.name}")
      destination.deposit(amount, description=f"Transfer from {self.name}")
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    else:
      return False
    
  def __str__(self):
    name = self.name
    title = name.center(30, "*")
    s = f"{title}"

    for item in self.ledger:
      if len(item["description"]) > 23:
        descr = item["description"][0:23]
        a = str("{:.2f}".format(item['amount']))
        s += f"\n{descr.ljust(23)}{a.rjust(7)}"
      else:
        descr = item["description"]
        a = str("{:.2f}".format(item['amount']))
        s += f"\n{descr.ljust(23)}{a.rjust(7)}"

    total = str(self.get_balance())
    s += f"\nTotal: {total}"

    return s

def create_spend_chart(categories):
  # Get total of withdraws per category and store in dictionary
  withdraw_dict = {}
  for category in categories:
    total_withdraw = 0
    for i in category.ledger:
      if i["amount"] < 0:
        total_withdraw += abs(i["amount"])
    withdraw_dict[category.name] = round(total_withdraw, 2)
  # Get total of all withdrawals of all categories
  total_all = sum(withdraw_dict.values())
  # Get percentage of total withdraws per category
  percent_dict = {}
  for category in withdraw_dict.keys():
    percent_dict[category] = int(round(withdraw_dict[category]/total_all, 2)*100)

  chart_s = "Percentage spent by category"
  for x in range(100, -10, -10):
    y = "\n" + str(x).rjust(3) + "| "
    chart_s += y
    for percent in percent_dict.values():
      if percent >= x:
        chart_s += "o  "
      else:
        chart_s += "   "

  x_line = "-"
  for c in percent_dict.keys():
    x_line += "---"
  chart_s += f"\n    {x_line}\n"

  cat_list = list(percent_dict.keys())
  longest_cat = max(len(category) for category in percent_dict)
  for i in range(longest_cat):
    chart_s += "     "
    for cat in cat_list:
      if len(cat) > i:
        chart_s += cat[i] + "  "
      else:
        chart_s += "   "
    if i < longest_cat-1:
      chart_s += "\n"
            
  return chart_s