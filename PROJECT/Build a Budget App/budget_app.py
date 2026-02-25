class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    spent = []
    total = 0
    for category in categories:
        cat_total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                cat_total += -item["amount"]
        spent.append(cat_total)
        total += cat_total

    percentages = []
    for amount in spent:
        percent = (amount / total) * 100 if total > 0 else 0
        percentages.append(int(percent // 10) * 10)

    for i in range(100, -1, -10):
        result += f"{str(i).rjust(3)}| "
        for percent in percentages:
            if percent >= i:
                result += "o  "
            else:
                result += "   "
        result += "\n"


    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        result += "     "
        for category in categories:
            if i < len(category.name):
                result += category.name[i] + "  "
            else:
                result += "   "
        result += "\n"

    return result[:-1] 
