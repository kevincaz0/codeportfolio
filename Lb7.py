def age():
	age=int(input("Enter your age: "))
	if age>=18 and age  <85:
		print("You can vote!")
		print("You can get a driver's license and drive!")
		print("You can watch any movie without adult supervison.")
	elif age<13:
		print("You cannot vote.")
		print("You cannot get a driver's license and cannot drive.")
		print("You can only watch G movies. But must be with a parent to watch PG movies.")
	elif age>=16 and age<=17:
		print("You cannot vote.")
		print("You could get a driver's license but a adult with a lincense must be present to drive.")
		print("You can only watch PG movies,PG-13 movies ,and G movies. But must be be with a parent to watch R movies.")	
	elif age>85:
		print("You can vote but you probably need some help.")
		print("You can get a driver's license and drive but at your age , it's suggested that others drive for you.")
		print("You can watch any movie without adult supervison but suggested not to watch horror movies.")
	elif age>=13 and age<17:
		print("You cannot vote.")
		print("You cannot get a driver's license and cannot drive.")
		print("You can only watch PG movies, and G movies. But must be be with a parent to watch PG-13 and R movies.")
