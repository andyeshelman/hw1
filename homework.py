
#======= Question 1 ========

# Task 1: Indentation Correction

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

# Task 2: Your Mood Today

mood = input("How do you feel today?\n")

if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I hope your day gets better!")
else:
    print("I am unfamiliar with that mood!")

#======= Question 2 =======

#Task 1: Correct Variable Names

PI_VALUE = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

#======= Question 3 =======

#Task 1: Grocery Store Math

cost_of_bread = 4.99
cost_of_peanut_butter = 4.49
cost_of_jelly = 4.49

total_cost = cost_of_bread + cost_of_peanut_butter + cost_of_jelly
print(f"Total cost is {total_cost}.")

#Task 2: Bank Interest

def bank_interest(principal, rate):
    return principal + principal * rate

print(bank_interest(10000,.07))
