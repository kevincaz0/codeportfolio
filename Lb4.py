import random #Makes it possible to use Random 

def dice():# Defines Dice
	print("Let's Play a Game!!") #Prints words 
	print("Try Guess The Number , Two Dice will be Rolled and Equaled , You have to guess the Output")  #Prints words 	
	ask=input("What Number Do you Guess?") #A input
	D1=random.randint(1,6) #Randomly picks a number 1-6
	D2=random.randint(1,6)#Randomly picks a number 1-6
	Shake= D1 +D2 #Adds Dice 1 and Dice 2 together
	print("My Number : ") # Prints words
	print(Shake) #Print the sum of dice 1 and dice 2
	print("Your Number :") #Prints words
	print(ask) #Prints the user's output
	if ask==Shake:#A command triggered when both my number and the user's number are the same 
		print("You win")#Prints words when outputs are equal





