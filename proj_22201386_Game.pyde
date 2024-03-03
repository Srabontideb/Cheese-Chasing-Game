 # add the minim library
add_library('minim') 

def setup(): 
    global bg, img, exitButton, restartButton 
    global rat, ratX,ratY, ratW, ratH
    global stageNum
    global score, lives
    global img2, cheeseW, cheeseH, cheeseX, cheeseY
    global cheeseDx, cheeseDy, numCheese
    global minim, player
    
    
    # create a minim object
    minim = Minim(this)
    
    # load the song into the player
    player = minim.loadFile("song1.mp3")
    
    
    #size of the window
    size(950,650)
    
    
    #load images
    bg = loadImage("background.jpg")
    img = loadImage("rat.png")
    exitButton = loadImage("exit.png")
    restartButton = loadImage("restart.png")
    img2 = loadImage("cheese.png")
    
    
    # rat dimensions
    ratX = 420
    ratY = 480
    ratW = 110
    ratH = 120
    
    
    # cheese dimensions
    cheeseX = random(200,600)
    cheeseY = random(0,200)
    cheeseW = 80
    cheeseH = 100 
    cheeseDy = int(random(2,3))
    
    
    #stageNum will control the stage you are in
    # 0: Welcome Page
    # 1: Game Play Page
    # 2: Game Over Page
    stageNum = 0
    
    
    #beginning number of lives of the RAT
    score = 0
    lives = 5
    
    
    # load number of c
    numCheese = 1
     
             
def draw():
    
     
    # display the different stages of the game
    if (stageNum == 0):
        drawWelcome()
    elif (stageNum == 1):
        drawGamePlay()
    elif (stageNum == 2):
        drawGameOver()
        

def keyPressed():
    if key == 'r':  # start playing
        player.rewind() #rewind to the begining of the song
        player.play()
        print("Play once only")
    elif key == 'p': # pause
        if player.isPlaying():
            player.pause()
            print("Pause")    
    elif key == 'q':  # resume
        player.play()  # resume at the current position of the song
        print("Resume")
    elif key == 's':  # stop
        player.pause() # pause
        player.rewind() # rewind to the begining of the song
        print("Stop")
    elif (key == 'l'): # loop
        player.loop()
        print("Play song in loop")

# Minim requires this stop() function 
def stop():
    # close the player
    player.close()
    # stop Minim
    minim.stop()
        
        
def drawWelcome():
    global stageNum, rat
    
    #instructions for the game
    image (bg, 0, 0)
    fill (255)
    textSize (17)
    text("WELCOME TO THE GAME!", 10, 10)
    text("Press the left/right keys on keyboard to move the rat.", 20, 40)
    text("Press the up or down keys on keyboard to make the rat stop.", 20, 60)
    text("Dont let cheese fall to ground or you lose life.", 20, 80)
    text("After the score is 20, the speed of the cheese falling will increase.", 20, 100)
    text("Catch the cheese to earn score.", 20, 120)
    text("After score is 40, do not collide with the walls or game will be over.", 20, 140)

    textSize(18)
    text("INSTRUCTIONS FOR THE MUSIC:", 640, 10)
    textSize(17)
    text("Press 'r' to play the song once", 660, 40)
    text("Press 'l' to play the song in loop", 660, 60)
    text("Press 'p' to pause the song", 660, 80)
    text("Press 'q' to resume the song", 660, 100)
    text("Press 's' to stop the song", 660, 120)
    
    
    # draw RAT
    image(img, ratX, ratY, ratW, ratH)
    
    
    # how to start playing the game
    fill(random(255), random(255), random(255))
    textSize(20)
    textAlign(LEFT, TOP)
    text("PLEASE PRESS ANY KEY TO START PLAYING", 280, 280)

    if keyPressed == True:
        stageNum = 1 #stageNum + 1
        
        
def drawGamePlay():
    global stageNum, numCheese
    global score, lives
    global rat, ratX, ratY   
    global img2, cheeseX, cheeseY, cheeseW, cheeseH, cheeseDy
    
    image(bg,0,0)
    
    # how to move to next stage
    if lives == 0:
        stageNum = 2 #stageNum + 1
    else:
        # draw rat
        image(img, ratX, ratY, ratW, ratH)
        
        
        # move rat either left or right
        if keyCode == RIGHT:
            ratX = ratX + 3.2
            
        elif keyCode == LEFT:
            ratX = ratX - 3.2
            
            
                
        # cheese move
        for i in range(numCheese):
            image(img2, cheeseX, cheeseY, cheeseW, cheeseH)
            cheeseY = cheeseY + cheeseDy

                
            if (cheeseX > width):
                continue
            
                
            # how life of rat is deducted
            # if cheese collides with the ground
            if (cheeseY + cheeseH >= height - ratH/2):
                 lives = lives - 1
                 cheeseX = random(50,850)
                 cheeseY = random(0,250)
                 
                 
            # code for score
            if (cheeseX + cheeseW>=ratX and cheeseX<=ratX + ratW and cheeseY + cheeseH >=ratY and cheeseY <=ratY + ratH):
                score = score + 1
                cheeseX = random(50,850)  
                cheeseY = random(0,250)  
                
            # after score is 20
            if score > 20:
                cheeseDy = random(3,3.5)
                if keyCode == RIGHT:
                    ratX = ratX + 0.8
            
                elif keyCode == LEFT:
                    ratX = ratX - 0.8
                
                        
        # display lives and score
        fill(0)
        rect(5, 10, 88, 20)
        rect(5, 30, 88, 20)
        fill(255)
        textSize(20)
        textAlign(LEFT, TOP)
        text("Lives:" + str(lives), 10, 10)
        text("Score:" + str(int(score)), 10, 30)
        
        if (score == 20):
            fill(0)
            text("STAGE 2", 240, 160) 
            
        if (score == 40):
            fill(0)
            text("STAGE 3", 240, 160) 


        if (score >= 40):
            if ratX >= 950 or ratX <= 0:
                numCheese = 0
                drawGameOver()
        

def drawGameOver():
    
    # display game over
    fill(255, 255, 255)
    textSize(100)
    textAlign(CENTER)
    text("GAME OVER!", width/2, height/4 + 20)
    
    fill(255,255,255)
    textSize(30)
    textAlign(CENTER)
    text("Better luck next time!", width/2 ,height/3 + 20)
    
    # display score
    fill(255, 255, 255)
    textSize(50)
    textAlign(CENTER)
    text("Your score: " + (str(int(score))), width/2, height/2 + 20)
    
    # display restart and end game button
    fill(0, 255, 0)
    rect(width/2 - 225, height/3 * 2 - 25, 150, 150)
    image(restartButton, width/2 - 225, height/3 * 2 - 25, 150, 150)
    
    fill(255, 0, 0)
    rect(width/2 + 75, height/3 * 2 - 25, 150, 150)
    image(exitButton, width/2 + 75, height/3 * 2 - 25, 150, 150)

    # code for next steps
    if mousePressed == True:
        # if restart button pressed
        if mouseX > width/2 - 225 and mouseX < width/2 - 225 + 150 and mouseY > height/3 * 2 - 25 and mouseY < height/3 * 2 - 25 + 150:
            setup(),
        # if end game button pressed
        elif mouseX > width/2 + 75 and mouseX < width/2 + 75 + 150 and mouseY >  height/3 * 2 - 25 and mouseY <  height/3 * 2 - 25 + 150:
            exit()
    
    
    
