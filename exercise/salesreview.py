from statistics import mean

#data provided for azubi project
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate",
            "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee",
            "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]



#TASK 1: Calculate the total price average for all products
price_average = mean(prices)
print(round((price_average), 2))

#End of Task 1##################################################################



#TASK 2: Create a new price list that reduces the old prices by $5
new_price_list = [ ]

for price in prices:
    newPrice = price - 5
    new_price_list.append(newPrice)
print(new_price_list)

#End of Task 2##################################################################



#TASK 3: Calculate the total revenue generated from the products

#Creat an empty list.
last_week_revenue = [ ]

#multiply the prices and last_week sales to generate the last_week_revenue list.
for i in range(len(last_week)):
    last_week_revenue.append(new_price_list[i] * last_week[i])
print(last_week_revenue) 

#Calculate the sum of the revenue
print(f'Total Revenue Generated: ${sum(last_week_revenue)}')

#End of Task 3##################################################################



#TASK 4: Calculate the averge daily revenue generated
average_daily_revenue = mean(last_week_revenue)

print(f'Average daily revenue: ${round((average_daily_revenue),2)}')

#End of Task 4#################################################################

#TASK 5: Based on the new price list which product is less than $30
products_list = [ ]
for i in range(len(products)):
    if new_price_list[i] < 30:
        products_list.append(products[i])
print(products_list)

#End of Task 5#################################################################