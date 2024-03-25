def ping():
	import play #Loading the play library
	import random #Loading the random library
	#Determine a constat Court's width and height
	w=400 #Defines global variable for horizontal size of court
	h=500 #Defines global variable for vertical size of court 
	#Determine a constat for the Middle Court's W & H
	halfWidth=w/2 #Defining global variable for half width of court
	halfHeight=h/2 #Defining global variable for height of court
	#Determine the starting score 
	score = 0 #Defines global variable for score
	#Determine the speed of the ball
	speed = 5 #Defining global variable for the speed of the ball
	@play.when_program_starts #Creates a keyframe to start the gamer
	#Declare a function to build the Court
	def do(): #Defining or initializing the function Do
	  play.set_backdrop((0,0,0)) #Sets a background color black
	#Define the playing Court
	court= play.new_box( #Declaring the variable that will be the court (play) calls the library (.) query for a prebuild function (new_box) the prebuild function to create rectangle the paraentestis hold the parameters
	  color=(120,20,120), #Initializing the parameter 'color' to a purple shade
	  x=0, #Initializing the X value horizantal corrdinates vaule 
	  y=0, #Initializing the Y value vertital corrdinates vaule 
	  width=w, #Initializing the width to preset value 'w'
	  height=h, #Initializing the height to preset value 'h'
	) #Close the parameters
	ball=play.new_circle( #Declaring the variable to hold a function for circle
	  radius=10, #Initializing the parameter radius to 10
	  x=0, #Initializing the X coordinates to 0
	  y=halfHeight -30, #Initializing the Y with the half_height -30 to have a fix starting point
	  color=(200,20,200), #Initializing the parameter for color
	  angle= random.randint(210,330), #Initializing the bouncing angle
	) #Close the parameters
	paddle=play.new_box( #Declaring the variable to hold a function for paddle 
	  color=(50,20,50),#Initializing the parameter for color
	  width=50, #Initializing the width to 50 
	  height=10, #Initializing the height to 10 
	  x=0, #Initializing the  X coordinates to 0
	  y=-halfHeight+10, #Initializing the y with the half_height +10 to have a fix starting point
	) #Close the parameters
	scoreText = play.new_text( #Declaring the variable to hold a function for paddle 
	 words="Score: "+ str(score), #Initializing the score 
	  x=0, #Initializing the X coordinates to 0
	  y=halfHeight +15, #Initializing the y with the half_height +25 to have a fix starting point
	  font= None, #Initializing the font for the words
	  color="white", #Initializing the parameter for color 
	) #Close the parameters
	@play.repeat_forever #Keyframe to do the following as long as the game is playing
	def do(): #Re define the Do function
	  global score #Calling for the global variable score
	  paddle.x = play.mouse.x #Dot notation to recall the x parameter of paddle to ressign vaule to match mouse X coordinates
	  #ensure the paddle isn't off court
	  if(play.mouse.x<-halfWidth + paddle.width/2): #Left side 
	    paddle.x=-halfWidth + paddle.width/2
	  if(play.mouse.x>halfWidth - paddle.width/2): #Right side
	      paddle.x=halfWidth - paddle.width/2
	  ball.move(speed)
	#Top wall
	  if(ball.y + ball.radius > halfHeight):
	    ball.angle = 360 - ball.angle
	#Bottom wall
	  if(ball.y - ball.radius <-halfHeight):
	    ball.angle = 360 - ball.angle
	    score -= 1 #Score = score -1
	#Bounce off left/right : 180 - angle
	#Right wall
	  if(ball.x +ball.radius> halfWidth):
	    ball.angle= 180 -ball.angle 
	#Left wall
	  if(ball.x-ball.radius < -halfWidth):
	    ball.angle= 180 -ball.angle
	#Make it bounce as if it hits the bottom, and give it a little change of trajectory
	  if(ball.is_touching(paddle)):
	    ball.angle =360-ball.angle + random.randint(-30,30)
	    ball.angle %= 360 #Ensures angle is valid
	#Make sure the ball goes up after hitting the paddle 
	    if(ball.angle < 20):
	      ball.angle = 20
	    elif(ball.angle > 160):
	      ball.angle = 160
	    score +=1
	    if(score==5):
	      paddle.width -= 5
	  ball.angle %= 360 #Ensure angle is valid
	  scoreText.words ="Score:" +str(score)
	play.start_program()