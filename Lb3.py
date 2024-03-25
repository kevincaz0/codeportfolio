def speak():
	import play
	w=300
	h=300
	@play.when_program_starts
	def do ():
	  play.screen.width = w
	  play.screen.height = h 
	
	box= play.new_box(
	 color= (255,105,180),
	 x=250,
	 y=100,
	 width = w,
	 height= h,
	)
	play.set_backdrop((0,0,0))
	# The head starts here #
	k_collar = play.new_circle(
	color = "pink",
	  x=160,
	  y=15,
	  radius=45,
	)
	k_medal = play.new_circle(
	color = "yellow",
	  x=160,
	  y=-35,
	  radius=10,
	)
	ear_k = play.new_box(
	color= "gray",
	x=135,
	y=53,
	width=40,
	height=35,
	)
	ear2_k = play.new_box(
	color= "gray",
	x=185,
	y=53,
	width=40,
	height=35,
	)
	k_head = play.new_circle(
	 color = "gray",
	  x=160,
	  y=25,
	  radius=45,
	)
	eye_R_K= play.new_circle(
	color= "black",
	x=175,
	y=35,
	radius=5,
	)
	eye_L_K= play.new_circle(
	color= "black",
	x=145,
	y=35,
	radius=5,
	)
	
	random_K= play.new_circle(
	color= (255,105,180),
	x=160,
	y=73,
	radius=7,
	) 
	lick_k= play.new_circle(
	 color="pink",
	x=162,
	y=-5,
	radius=5, 
	)
	mouth_K= play.new_circle(
	color="black",
	x=150,
	y=10,
	radius=15,
	)
	
	mouth3_K= play.new_circle(
	color="black",
	x=175,
	y=10,
	radius=15,
	)
	mouth2_K= play.new_circle(
	color="gray",
	x= 175,
	y=15,
	radius=13,
	)
	mouth4_K= play.new_circle(
	color="gray",
	x=150,
	y=15,
	radius=13,
	)
	whis_K= play.new_box(
	color= "black",
	x=115,
	y=20,
	width=30,
	height=3,  
	)
	whis2_K= play.new_box(
	color= "black",
	x=115,
	y=10,
	width=25,
	height=3,  
	)
	whis3_K= play.new_box(
	color= "black",
	x=205,
	y=20,
	width=30,
	height=3,  
	)
	whis4_K= play.new_box(
	color= "black",
	x=205,
	y=10,
	width=25,
	height=3,  
	)
	nose_K= play.new_circle(
	color= "black",
	x=160,
	y=25,
	radius=5,
	)  
	nose2_K= play.new_box(
	color= "gray",
	x=160,
	y=31,
	width=10,
	height=10,
	)  
	# The head ends here and the text starts here#
	text= play.new_text(
	color="pink",
	words="Meow meow meow meow, Meow Meow?",
	x=250,
	y=150,
	font_size=20,
	)
	#Switch to the second text#
	@play.repeat_forever
	async def speak_slowly():
	  await play.timer(seconds=6)
	  text.words="Purrrrrrrr Purrrrrrrr , Meow!"
	#The text ends here and mouse starts here #  
	mouse_text= play.new_text(
	color="pink",
	words="blank",
	x=0,
	y=0,
	font_size=20,
	)
	@play.repeat_forever
	def mouse_coords():
	  mouse_text.go_to(play.mouse)
	  mouse_text.words = str(int(play.mouse.x))+","+str(int(play.mouse.y))
	
	play.start_program()
	
	
	