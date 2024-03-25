def divisible():
	x=int(input("How many numbers do you need to check? "))
	true=0
	false=0
	for i in range(x):
	    x-=1
	    y=int(input("Enter number: "))
	    if y % 3==0:
	        print(str(y)+" is divisible by 3.")
	        true+=1
	    else:
	        print(str(y)+" is not divisible by 3.")
	        false+=1
	print("You entered "+str(true)+" number(s) that are divisible by 3.")
	print("You entered "+str(false)+" number(s) that are not divisible by 3.")
