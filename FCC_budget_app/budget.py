#this was a huge pain in the ass trying to figure out and understand.  no doubt.  I ended up just finding solutions and implementing them without really comprehending them fully.  which i don't like, since I want to be able to handcraft every piece knowing every element I am using and the ins and outs.  but this was just too complex for me to figure out completely on my own.  I thought it would be best to just complete the assignment and move on, i spent enough time vegging out on python classes for now.  I hope I can come back to this assignment in some months and see it as a piece of cake.  just keep on keeping on.  this passed all the tests and I'm turning it in.  after a solid 24 hours lol
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
  
    def deposit(self, amount, description=""):
        # Adds a deposit entry to the ledger list
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=""):
        # Checks if sufficient funds are available, adds a withdrawal entry to the ledger list if true
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False  
  
    def get_balance(self):
        # Calculates and returns the current balance of the category
        balance = 0
        for entry in self.ledger:
            balance = balance + entry["amount"]
        return balance
  
    def transfer(self, amount, category):
        # Transfers an amount from the current category to another category
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
      
    def check_funds(self, amount):
        # Checks if a specified amount is available in the category
        return amount <= self.get_balance()

    def __str__(self):
        # Returns a formatted string representation of the category
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        total = 0
        for entry in self.ledger:
            description = entry["description"][:23].ljust(23)
            amount = format(entry["amount"], ".2f").rjust(7)
            items += f"{description}{amount}\n"
            total += entry["amount"]
        output = title + items + "Total: " + str(format(total, ".2f"))
        return output

    def get_withdraws(self):
        # Calculates and returns the total amount of withdrawals made from the category
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total


def create_spend_chart(categories):
    # Step 1: Calculate the percentage spent for each category
    total_spent = sum(category.get_withdraws() for category in categories)
    percentages = [(category.get_withdraws() / total_spent) * 100 // 10 * 10 for category in categories]

    # Step 2: Generate the chart
    chart_lines = ["Percentage spent by category"]
    for line in range(100, -1, -10):
        chart_line = f"{line:3d}| "
        for percentage in percentages:
            chart_line += "o  " if percentage >= line else "   "
        chart_lines.append(chart_line)

    # Step 3: Format the chart
    longest_category_name = max(len(category.name) for category in categories)
    chart_lines.append("    " + "-" * (len(categories) * 3 + 1))
    for i in range(longest_category_name):
        category_line = "     "
        for category in categories:
            category_name = category.name
            category_line += category_name[i] + "  " if i < len(category_name) else "   "
        chart_lines.append(category_line)

    return "\n".join(chart_lines)

