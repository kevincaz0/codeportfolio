import random
def chat():
	nam=input("What is  your first name? ")
	if nam =="Kevin"or nam=="Kevin":
	    print("That's my name too!")
	sho=input("What shoes do you like? ")
	slist=["That's cool, i love "+sho+" too!", "Awesome, "+sho+ " are my favorite!","Nice, "+sho+ " is casual, great pick!"]
	if sho=="converse"or sho=="Converse":
	    print("I love converse , they are my everyday shoe.")
	else:
	    print(random.choice(slist))
	age=int(input("How old are you? "))
	alist=["Oh ,"+str(age)+" nice thats seems like a good age to start exploring fashion!",str(age)+" ,that's cool!","That's great!"]
	if age==16:
	    print("That's my age too!")
	else:
	    print(random.choice(alist)) 
	top=input("So, "+nam+", what is your favorite top? ")
	tlist=["Ooo, I love "+top+" too!","That's a intresting choice.", "Those are a great choice they will good with "+sho]
	if top=="sweater"or top=="Sweater":
	    print("That's my favorite too!")
	else:
	    print(random.choice(tlist))
	bot=input("What about your choice of bottom? ")
	blist=["Umm, Great pick!", "Oohhh, I love that!","I have " +bot+" and they are amazing!","They seem to complete the outfit!"]
	print(random.choice(blist))
	any=input("Anything else you want to add? ")
	if any=="no"or any=="No":
	    print("Well, "+nam+" it was awesome getting to know your style. ")
	elif any =="yes"or any=="Yes":
	    last=input("What else do you have to tell me? ")
	    print("Oh, okay, it was enjoyable talking to you , Goodbye!")
	elif any =="maybe"or any=="Maybe":
	    print("If you arent sure it's okay, dont worry, but goodbye.")
	elif any =="goodbye"or any=="Goodbye":
	    print("Well, GOODBYEEE!!")