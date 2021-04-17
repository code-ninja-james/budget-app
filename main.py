# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main
#food
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant")
print(food.get_balance())

#clothing
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55,"shirts")
clothing.withdraw(100)

#entertainment

entertainment = budget.Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(10.15, "netflix")
entertainment.withdraw(15.89, "spotify")
print(entertainment.get_balance())


print(food)
print(clothing)
print(entertainment)

print(create_spend_chart([food, clothing,entertainment]))

# Run unit tests automatically
main(module='test_module', exit=False)
