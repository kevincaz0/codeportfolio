def change():
	num_pennies = int(input("Enter the number of pennies: "))
	num_nickels = int(input("Enter the number of nickels: "))
	num_dimes = int(input("Enter the number of dimes: "))
	num_quarters = int(input("Enter the number of quarters: "))
	num_loonies = int(input("Enter the number of loonies: "))
	num_toonies = int(input("Enter the number of toonies: "))
	
	total_value = (num_pennies + 5*num_nickels+10* num_dimes+25*num_quarters+100*num_loonies+200*num_toonies)/100
	  
	print()  # this prints a blank line
	print("Number of pennies:", num_pennies)
	print("Number of nickels:", num_nickels)
	print("Number of dimes:", num_dimes)
	print("Number of quarters:", num_quarters)
	print("Number of loonies:", num_loonies)
	print("Number of toonies:", num_toonies)
	print("")
	print("Total value of coins: $" + "{:.2f}".format(total_value))