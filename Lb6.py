def year():
	year = int(input("Enter a year: ")) 
	#Leap year is a year that has an extra day in february. If you were born on February 29th, then you  can onky celebrate your birthday every 4 years on that date 
	#Every year february ends on the 28th
	#Every 4 years we have a leap year that makes february longer by a day
	#Tropical Year = 365 days, 5 hours , 48 minutes, 45 seconds, 138 milliseconds
	if year <=1752: #Start of the Gregorian Calendar 
		print("Leap years didn't exist back then!")
	#Every 4 years make it leap year , it's the Julian Calendar
	#If the year is a multiple of 100 , it's not a leap year
	#If the year is a multiple of 400, it is a leap year
	#If the year is more of 10000 or multiple 10000 + 2800 it's not a leap year
	elif year>10000 and (year-2800)%10000==0 and (year%100)==0:
		print(str(year)+" was NOT a leap year. ")
	# If the year ends in 2800 or 5600 or 8400 then that is not a leap year
	elif year<10000 and (year-2800)%10000==0:
		print(str(year)+" was NOT a leap year.")
	elif year<10000 and (year-5600)%10000==0:
		print(str(year)+" was NOT a leap year.")
	elif year<10000 and (year-8400)%10000==0:
		print(str(year)+" was NOT a leap year.")
	else: #It tells what is a leap year2
		if year %400==0:
			print(str(year)+ " is a leap year!")
		elif year%100!=0 and year%4==0:
			print(str(year)+" is a leap year! ")
		else:
			print(str(year)+" was NOT a leap year.")