import random
def passwordGenerator():
	listOfAnimals=["cat", "dog", "unicorn", "dragon"]
	ani=random.choice(listOfAnimals)
	beginningNum= random.randint(7,213789)
	lastNum= random.randint(1,500)
	listOfChar=["!","#","@","?"]
	char=random.choice(listOfChar)
	newPassword=str(beginningNum)+ani+str(lastNum)+char
	print(newPassword)
	print("I created a new Password, here it is:")