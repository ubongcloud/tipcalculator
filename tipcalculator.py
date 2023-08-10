#ask the user to enter food cost
meal_cost = int(input('Please enter the cost of the mean: '))

#ask the user to enter to percentage of tip
tip_percentage = float((input('Please enter the tip percentage you want to leave: '))) / 100

#calculate the tip
tip = tip_percentage * meal_cost

#output the tip
print(f'Tip Amount: ${tip}')

#assumee fix tax to be 7%
sales_tax = 0.07 * meal_cost

#print sales_tax
print(f'Sales Tax: ${round(sales_tax, 2)}')

#calculate the total_bill
total_bill = (meal_cost + tip + sales_tax)
print(f'Total Bill: ${total_bill}')