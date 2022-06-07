from math import ceil

people = int(input("Enter the number of people: "))
average_slices = float(input("Enter average number of slices: "))
price = float(input("Enter the cost of a pizza: "))
number_of_pizzas = ceil((people*average_slices)/ 8)
cost_of_pizza =  number_of_pizzas * price
tax = 0.07 * cost_of_pizza
delivery = (cost_of_pizza + tax) * 0.2

print(f"Friday Night Party \n {number_of_pizzas} Pizzas: $ {cost_of_pizza} \nTax: $ {round(tax, 2)}\nDelivery: $ {round(delivery, 2)} ")
