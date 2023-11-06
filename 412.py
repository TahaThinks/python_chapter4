my_pizza = ["Pepperoni","Shrimps Lover","Chicken Supreme"]
friends_pizza = my_pizza[:]

my_pizza.append("Vegetarian")
friends_pizza.append("Super Supreme")

for pizza in my_pizza:
    print(pizza)

print("\n")

for pizza in friends_pizza:
    print(pizza)