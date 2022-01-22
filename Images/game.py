import time
import random
def initial(x):
	return str(x[0]) 
def sorterOfCards(p):
	for i in range(len(p)):
		mini=i
		for j in range (i+1,len(p)):
			if((p[j][0]=="T") and (p[mini][0]=="J" or p[mini][0]=="Q" or  p[mini][0]=="K")):
				mini=j
			elif (p[j][0]=="Q" and p[mini][0]=="K"):
				mini=j
			elif(p[j][0]=="9") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="8") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="7") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="6") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="5") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="4") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="3") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="2") and (p[mini][0]=="T"):
				mini=j
			elif(p[j][0]=="1") and (p[mini][0]=="T"):
				mini=j	
			elif(p[j][0]<p[mini][0]):
				mini=j
		p[i],p[mini]=p[mini],p[i]
	
def pause(minute,second):
	height=650
	width=1300
	white=(255,255,255)
	black=(0,0,0)
	display3=pygame.display.set_mode((width,height),pygame.RESIZABLE)
	icon_image=pygame.image.load("bg2.jpg").convert()
	backpause=pygame.image.load("bg32.png").convert()
	pygame.display.set_icon(icon_image)
	pygame.display.set_caption("PAUSE PAGE")
	display3.blit(backpause,[0,0])
	myfont2=pygame.font.Font('LCALLIG.ttf',40)
	display_text1=myfont2.render("Press \"space\" to continue",True,white)
	TextRect1=display_text1.get_rect()
	TextRect1.center = ((width/2),height/2)

	timerbegin = pygame.time.get_ticks() 

	pause=True
	while pause:
		timepassed=pygame.time.get_ticks()-timerbegin
		display3.blit(display_text1,TextRect1)	
		timerfont=pygame.font.Font('GOUDOSB.ttf',20)
		timer_text=timerfont.render(str(minute+":"+second),True,black,white)
		timerRect=timer_text.get_rect()
		timerRect.center = ((width/3+600),50)
		display3.blit(timer_text,timerRect)
		pygame.display.update()			
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
				if event.key==pygame.K_SPACE:
					pause=False
					return timepassed
			if event.type==pygame.QUIT:
				pause=False
				#Quit button is pressed
				pygame.quit()
				quit()			
	
def second_page():
	#pygame.init()
	flag=0

	height=650
	width=1300
	display2=pygame.display.set_mode((width,height),pygame.RESIZABLE)
	white=(255,255,255)
	black=(0,0,0)
	blue=(0,0,255)
	thodalightblack=(44,44,44)
	#loading the images
	icon_image=pygame.image.load("bg2.jpg").convert()
	back=pygame.image.load("bg3.png").convert()
	pygame.display.set_icon(icon_image)
	pygame.display.set_caption("PLAYING PAGE")
	display2.blit(back,[0,0])
	
	myfont2=pygame.font.Font('LCALLIG.ttf',24)

	display_text1=myfont2.render("PAUSE",True,white,black)
	TextRect1=display_text1.get_rect()
	TextRect1.center = ((width/3),50)
	
	display_text2=myfont2.render("QUIT",True,white,black)
	TextRect2=display_text2.get_rect()
	TextRect2.center = ((width/3+200),50)
	
	display_text3=myfont2.render("REPLAY",True,white,black)
	TextRect3=display_text3.get_rect()
	TextRect3.center = ((width/3+400),50)

	display_text4=myfont2.render("PRESS \"SPACE\" TO DRAW A CARD",True,white)
	TextRect4=display_text4.get_rect()
	TextRect4.center = (width/2,height/4)

	display_text8=myfont2.render("PRESS \"SHIFT\" TO DRAW A CARD",True,white)
	TextRect8=display_text8.get_rect()
	TextRect8.center = (width/2-200,height/4)

	myfont3=pygame.font.Font('BASKVILL.ttf',24)
	display_text5=myfont3.render("",True,white)
	TextRect5=display_text5.get_rect()
	TextRect5.center = (width/2+200,height/4+100)

	display_text6=myfont3.render("",True,white)
	TextRect6=display_text6.get_rect()
	TextRect6.center = (width/2+200,height/4+200)

	display_text7=myfont3.render("",True,white)
	TextRect7=display_text7.get_rect()
	TextRect7.center = (width/2+200,height/4+200)

	lst =["1club","2club","3club","4club","5club",
	"6club","7club","8club","9club","Tclub",
	"Jclub","Qclub","Kclub","1spade","2spade",
	"3spade","4spade","5spade","6spade","7spade",
	"8spade","9spade","Tspade","Jspade","Qspade",
	"Kspade","1diamond","2diamond","3diamond","4diamond",
	"5diamond","6diamond","7diamond","8diamond","9diamond",
	"Tdiamond","Jdiamond","Qdiamond","Kdiamond","1heart",
	"2heart","3heart","4heart","5heart","6heart","7heart",
	"8heart","9heart","Theart","Jheart","Qheart","Kheart"] 

	card_dict = {}
	img = pygame.image.load("playing_cards/ace_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["1club"] = img
	img = pygame.image.load("playing_cards/2_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["2club"] = img
	img=pygame.transform.scale(img, (150, 200))
	img = pygame.image.load("playing_cards/3_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["3club"] = img
	img = pygame.image.load("playing_cards/4_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["4club"] = img
	img = pygame.image.load("playing_cards/5_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["5club"] = img
	img = pygame.image.load("playing_cards/6_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["6club"] = img
	img = pygame.image.load("playing_cards/7_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["7club"] = img
	img = pygame.image.load("playing_cards/8_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["8club"] = img
	img = pygame.image.load("playing_cards/9_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["9club"] = img
	img = pygame.image.load("playing_cards/10_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Tclub"] = img
	img = pygame.image.load("playing_cards/jack_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Jclub"] = img
	img = pygame.image.load("playing_cards/queen_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Qclub"] = img
	img = pygame.image.load("playing_cards/king_clubs.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Kclub"] = img
	img = pygame.image.load("playing_cards/ace_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["1spade"] = img
	img = pygame.image.load("playing_cards/2_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["2spade"] = img
	img = pygame.image.load("playing_cards/3_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["3spade"] = img
	img = pygame.image.load("playing_cards/4_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["4spade"] = img
	img = pygame.image.load("playing_cards/5_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["5spade"] = img
	img = pygame.image.load("playing_cards/6_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["6spade"] = img
	img = pygame.image.load("playing_cards/7_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["7spade"] = img
	img = pygame.image.load("playing_cards/8_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["8spade"] = img
	img = pygame.image.load("playing_cards/9_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["9spade"] = img
	img = pygame.image.load("playing_cards/10_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Tspade"] = img
	img = pygame.image.load("playing_cards/jack_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Jspade"] = img
	img = pygame.image.load("playing_cards/queen_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Qspade"] = img
	img = pygame.image.load("playing_cards/king_spades.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Kspade"] = img
	img = pygame.image.load("playing_cards/ace_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["1heart"] = img
	img = pygame.image.load("playing_cards/2_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["2heart"] = img
	img = pygame.image.load("playing_cards/3_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["3heart"] = img
	img = pygame.image.load("playing_cards/4_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["4heart"] = img
	img = pygame.image.load("playing_cards/5_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["5heart"] = img
	img = pygame.image.load("playing_cards/6_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["6heart"] = img
	img = pygame.image.load("playing_cards/7_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["7heart"] = img
	img = pygame.image.load("playing_cards/8_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["8heart"] = img
	img = pygame.image.load("playing_cards/9_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["9heart"] = img
	img = pygame.image.load("playing_cards/10_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Theart"] = img
	img = pygame.image.load("playing_cards/jack_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Jheart"] = img
	img = pygame.image.load("playing_cards/queen_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Qheart"] = img
	img = pygame.image.load("playing_cards/king_hearts.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Kheart"] = img
	img = pygame.image.load("playing_cards/ace_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["1diamond"] = img
	img = pygame.image.load("playing_cards/2_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["2diamond"] = img
	img = pygame.image.load("playing_cards/3_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["3diamond"] = img
	img = pygame.image.load("playing_cards/4_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["4diamond"] = img
	img = pygame.image.load("playing_cards/5_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["5diamond"] = img
	img = pygame.image.load("playing_cards/6_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["6diamond"] = img
	img = pygame.image.load("playing_cards/7_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["7diamond"] = img
	img = pygame.image.load("playing_cards/8_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["8diamond"] = img
	img = pygame.image.load("playing_cards/9_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["9diamond"] = img
	img = pygame.image.load("playing_cards/10_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Tdiamond"] = img
	img = pygame.image.load("playing_cards/jack_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Jdiamond"] = img
	img = pygame.image.load("playing_cards/queen_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Qdiamond"] = img
	img = pygame.image.load("playing_cards/king_diamonds.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["Kdiamond"] = img
	img = pygame.image.load("deck.png").convert()
	img=pygame.transform.scale(img, (150, 200))
	card_dict["deck"] = img
	centerlist=[]
	p1,p2,remlist=cards(lst)
	count=0	
	flag=0
	flag1=0
	flag2=0
	player_2=False
	# def win(p):
	# 	h=p[:]
	# 	h.sort()
	# 	for i in h:
	# 		if(i[0])
	def no_of_occ(p,number):
		count=0
		for i in range(len(p)):
			if(p[i][0]==number):
					count+=1
		return count
	def keep(p2,c2):
		p2.append(c2)
		p2.sort()
		sorterOfCards(p2)
		anycard=random.choice(p2)
		p2.remove(anycard)
		centerlist.append(anycard)
	def pick_card():
		if (len(remlist)>0):
			c1=random.choice(remlist)
		else:
			c1="deck"

		remlist.remove(c1)
		return c1
	def player2(p2,centerlist):
	#------------IN A CASE IT FORMS A SET ---------------------------------
		opencard=centerlist.pop()
		occurances=no_of_occ(p2,opencard[0])
		if(occurances==2):
			keep(p2,opencard)
		else:
			centerlist.append(opencard)
		c2=pick_card()
		occurances=no_of_occ(p2,c2[0])
		if(occurances==2):
			keep(p2,c2)
		else:
			centerlist.append(opencard)
		#-----------------------------------------------------------------------------
		#-------------IN A CASE PURE SEQUENCE IS BEING FORMED -------------------------
		club=[]
		diamond=[]
		heart=[]
		spade=[]
		for i in p2:
			if(i[1:]=="club"):
				club.append(i)
			elif(i[1:]=="diamond"):
				diamond.append(i)
			elif(i[1:]=="spade"):
				spade.append(i)
			else:
				heart.append(i)
		#print(heart)
		#print(club)
		#print(spade)
		#print(diamond)
		opencard=centerlist.pop()
			
		if(opencard[1:]=="club"):
			for i in range(len(club)-2):
				seq_list=club[i:i+3]
				seq_list.append(club[i])
				#seq_list.sort()
				print(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,opencard)
				else:
					centerlist.append(opencard)			
		elif(opencard[1:]=="diamond"):
			for i in range(len(diamond)-2):
				seq_list=diamond[i:i+3]
				seq_list.append(diamond[i])
				#seq_list.sort()
				#print(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,opencard)
				else:
					centerlist.append(opencard)	
		elif(opencard[1:]=="spade"):
			for i in range(len(spade)-2):
				seq_list=spade[i:i+3]
				seq_list.append(spade[i])
				#seq_list.sort()
				#print(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,opencard)
				else:
					centerlist.append(opencard)	
				
		else:
			for i in range(len(heart)-2):
				seq_list=heart[i:i+3]
				seq_list.append(heart[i])
				#seq_list.sort()
				#print(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,opencard)
				else:
					centerlist.append(opencard)


		c2=pick_card()
		if(c2[1:]=="club"):
			for i in range(len(club)-2):
				seq_list=club[i:i+3]
				seq_list.append(clu[i])
				#seq_list.sort()
				#print(seq_list)
				sorterOfCards(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,c2)
				else:
					centerlist.append(c2)			
		elif(c2[1:]=="diamond"):
			for i in range(len(diamond)-2):
				seq_list=diamond[i:i+3]
				seq_list.append(diamond[i])
				#seq_list.sort()
				#print(seq_list)
				sorterOfCards(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,c2)
				else:
					centerlist.append(c2)	
		elif(c2[1:]=="spade"):
			for i in range(len(spade)-2):
				seq_list=spade[i:i+3]
				seq_list.append(spade[i])
				#seq_list.sort()
				#print(seq_list)
				sorterOfCards(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,c2)
				else:
					centerlist.append(c2)	
				
		else:
			for i in range(len(heart)-2):
				seq_list=heart[i:i+3]
				seq_list.append(heart[i])
				#seq_list.sort()
				#print(seq_list)
				sorterOfCards(seq_list)
				if(list(map(initial,seq_list))==["1","2","3","4"] or ["2","3","4","5"] or ["3","4","5","6"] or ["4","5","6","7"] or ["5","6","7","8"] or ["6","7","8","9"] or["7","8","9","T"] or ["8","9","T","J"] or ["9","T","J","Q"] or ["T","Q","K","1"] or ["Q","K","1","2"] or ["K","1","2","3"] ):
					keep(p2,c2)
				else:
					centerlist.append(c2)	
		#------------------------------------------------------------------------------
		return

	#for the timer	
	c1="deck"
	card_select_karna_hai=False
	timerbegin = pygame.time.get_ticks() 
	pause_time=0
	print(p2)
	keep_running=True
	while keep_running:
		#print(centerlist)
		p1.sort()
		p2.sort()
		sorterOfCards(p1)
		sorterOfCards(p2)
		
		display2.blit(back,[0,0])
		display2.blit(display_text1,TextRect1)
		display2.blit(display_text2,TextRect2)
		display2.blit(display_text3,TextRect3)
		display2.blit(display_text4,TextRect4)
		if count!=0:
			display2.blit(display_text8,TextRect8)
		display2.blit(display_text5,TextRect5)
		display2.blit(display_text6,TextRect6)
		display2.blit(card_dict[c1],[width/2-100,height/3])

		display2.blit(display_text7,TextRect7)
		mouse_position=pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		#DISPLAY PLAYER1 CARDS
		n=1
		for i in p1:
			display2.blit(card_dict[i],[-100+120*n,height-200])
			n+=1
		#DISPLAY THE WASTE PILE(OPEN)
		for i in centerlist:
			display2.blit(card_dict[i],[width/4-100,height/3])

		timepassed=pygame.time.get_ticks()-timerbegin-pause_time
		minute=str(int(timepassed/60000)).zfill(2)
		second=str(int((timepassed%60000)/1000)).zfill(2)
		timerfont=pygame.font.Font('GOUDOSB.ttf',20)
		timer_text=timerfont.render(str(minute+":"+second),True,black,white)
		timerRect=timer_text.get_rect()
		timerRect.center = ((width/3+600),50)
		display2.blit(timer_text,timerRect)
		pygame.display.update()
		clock.tick(25)
		#if QUIT IS PRESSED
		if width/3+200+50>mouse_position[0]>width/3+200-50 and 65>mouse_position[1]>45:
			#print("aaya quit")
			if(click[0]==1):
				#print("aaya quit ke andar")
				pygame.quit()
				quit()

		#replay is pressed
		elif width/3+400+50>mouse_position[0]>width/3+400-50 and 65>mouse_position[1]>45:
			#print("aaya rep,ay")
			if(click[0]==1):
				#print(no_of_set(p1))
				second_page()
				pygame.quit()
				quit()

		#pause is pressed
		elif width/3+50>mouse_position[0]>width/3-50 and 65>mouse_position[1]>45:
			if(click[0]==1):			
				pause_time+=pause(minute,second)
				#print(pause_time)
				#timepassed-=pause_time

		#if keep is pressed
		elif width/2+200+100>mouse_position[0]>width/2+200-100 and height/4+100+25>mouse_position[1]>height/4+100-25:
			if(click[0]==1 and flag1==0):			
				p1.append(c1)
				display_text5=myfont3.render("",True,white)
				display_text6=myfont3.render("",True,white)
				display_text7=myfont3.render("CHOOSE A CARD TO REPLACE",True,white)
				c1="deck"
				flag1=1
				flag2=0
				card_select_karna_hai=True
		
		#if discard is pressed
		elif 960>mouse_position[0]>850 and 370>mouse_position[1]>350:
			if(click[0]==1 and flag1==0):			
				centerlist.append(c1)
				display_text5=myfont3.render("",True,white)
				display_text6=myfont3.render("",True,white)
				#display_text7=myfont3.render("CHOOSE A CARD TO REPLACE",True,white)
				c1="deck"
				flag1=1
				flag2=0
				player_2=True			
								
		#-------THIS IS FOR CARD PICKING---------
		#for card no. 1
		if 20<mouse_position[0]<140 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[0])
						p1.pop(0)
						display_text7=myfont3.render("",True,white)
						flag2=1	
						card_select_karna_hai=False
						player_2=True
		#for card no. 2
		if 140<mouse_position[0]<260 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[1])
						p1.pop(1)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True
		#for card no. 3
		if 260<mouse_position[0]<380 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[2])
						p1.pop(2)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True
		#for card no. 4
		if 380<mouse_position[0]<500 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[3])
						p1.pop(3)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True	
		#for card no. 5
		if 500<mouse_position[0]<620 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[4])
						p1.pop(4)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True
		#for card no. 6
		if 620<mouse_position[0]<740 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[5])
						p1.pop(5)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True
		#for card no. 7
		if 740<mouse_position[0]<860 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[6])
						p1.pop(6)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True
		#for card no. 8
		if 860<mouse_position[0]<980 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[7])
						p1.pop(7)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True
		#for card no. 9
		if 980<mouse_position[0]<1100 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[8])
						p1.pop(8)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True
		#for card no. 10
		if 1100<mouse_position[0]<1220 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[9])
						p1.pop(9)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True	
		#for card no. 11
		if 1220<mouse_position[0]<1340 and 450<mouse_position[1]<650 and card_select_karna_hai:
					#print("HI")
					if(click[0]==1 and flag2==0):	
						#print("mila")
						centerlist.append(p1[10])
						p1.pop(10)
						flag2=1	
						card_select_karna_hai=False
						display_text7=myfont3.render("",True,white)
						player_2=True	
		#------------------------------------------------------------------------------------	
		if(player_2):
			print(p2)
			player2(p2,centerlist)
			display_text7=myfont3.render("YOUR TURN",True,white)
			flag=0
			count+=1
			print(p2)
			player_2=False																																													
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_SPACE and flag==0:
					display_text7=myfont3.render("",True,white)
					display_text4=myfont2.render("",True,white)
					display_text8=myfont2.render("",True,white)
					display_text5=myfont3.render("KEEP",True,white,blue)
					display_text6=myfont3.render("DISCARD",True,white,blue)
					c1=pick_card()
					flag=1
					flag1=0
			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_RSHIFT and flag==0:
					display_text7=myfont3.render("",True,white)
					display_text4=myfont2.render("",True,white)
					display_text8=myfont2.render("",True,white)
					display_text5=myfont3.render("KEEP",True,white,blue)
					display_text6=myfont3.render("DISCARD",True,white,blue)
					c1=centerlist.pop()
					flag=1
					flag1=0
			if event.type == pygame.KEYDOWN:
				#FOR THE HELP TO KNOW THE COORDINATES SO THAT MAKING BUTTONS IS EASIER
				if event.key==pygame.K_SPACE and flag==1:
					print("X coordinate",mouse_position[0],"y coordinate",mouse_position[1])
			if event.type==pygame.QUIT:
				#Quit button is pressed
				keep_running=False


def start_page():
	pygame.init()
	height=650
	width=1300
	display=pygame.display.set_mode((width,height),pygame.RESIZABLE)
	white=(255,255,255)
	black=(0,0,0)
	thodalightblack=(44,44,44)
	#loading of all the image
	icon_image=pygame.image.load("bg2.jpg").convert()
	background=pygame.image.load("bg1.jpg").convert()
	pygame.display.set_icon(icon_image)
	pygame.display.set_caption("START PAGE:RUMMY")
	
	#displaying bckground
	display.blit(background,[0,0])
	#text display
	myfont1=pygame.font.Font('MATURASC.ttf',32)

	display_text=myfont1.render("LET'S PLAY RUMMY",True,white,black)
	TextRect=display_text.get_rect()
	TextRect.center = ((width/2),(height/5))

	display_text2=myfont1.render("PLAY",True,white)
	TextRect2=display_text2.get_rect()
	TextRect2.center = (width/4+100,height/2+50)
	
	
	display_text3=myfont1.render("QUIT",True,white)
	TextRect3=display_text3.get_rect()
	TextRect3.center = (3*width/4+100,height/2+50)

	#for the continue or quit buttons
	pygame.draw.rect(display, black,(width/4,height/2,200,100))
	pygame.draw.rect(display, black,(3*width/4,height/2,200,100))
	#if mouse is hovered a slight colour change is observed
	#This is to keep the game running untill an event occurs to quit it
	keep_running=True
	while keep_running:
		display.blit(display_text,TextRect)
		
		mouse_position=pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if width/4+200>mouse_position[0]>width/4 and height/2+100 > mouse_position[1] > height/2:
			pygame.draw.rect(display,thodalightblack,(width/4,height/2,200,100))
			if(click[0]==1):
				second_page()
				pygame.quit()
				quit()
		elif 3*width/4+200>mouse_position[0]>3*width/4 and height/2+100 > mouse_position[1] > height/2:
			pygame.draw.rect(display,thodalightblack,(3*width/4,height/2,200,100))
			if(click[0]==1):
				pygame.quit()
				quit()
		else:
			pygame.draw.rect(display, black,(width/4,height/2,200,100))	
			pygame.draw.rect(display, black,(3*width/4,height/2,200,100))

		display.blit(display_text2,TextRect2)
		display.blit(display_text3,TextRect3)
		pygame.display.update()
		clock.tick(15)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				#Quit button is pressed
				keep_running=False
def cards(lst):
	list=[]
	remlist=lst[:]
	lst=set(lst)
	list=random.sample(lst,20)
	for i in list:
		#print(i)
		remlist.remove(i)
	return list[:10],list[10:],remlist

if __name__=="__main__":
	import pygame
	clock=pygame.time.Clock()
	pygame.init()
	#initialise the game
	start_page()
