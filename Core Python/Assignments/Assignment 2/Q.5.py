#WAP to calculate selling price of book based on cost price and discount.

cost_price=float(input("Enter the cost price of book:"))
dis=float(input("Enter the dis percentage on book:"))
dis_value=(cost_price*dis)/100
sell_price=(cost_price-dis_value)
print(f'The book cost price is: {cost_price} and after {dis} % of discount the selling price is: {sell_price}')