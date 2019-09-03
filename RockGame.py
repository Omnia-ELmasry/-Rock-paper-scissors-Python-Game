
# coding: utf-8

# In[ ]:

from random import randint
player1Score=0 
player2Score=0
computerScore=0


# game logic to choose who is the winer and calculate Scores for players
def gameLogic(player1,player2,score1,score2):
        
        if player1 == player2:
           print('Tie')
        elif player1 =="rock":
        
            if player2 == "Paper":
                score2=+1
                print(f"Score Player 1 is {score1} , Score Player 2 is {score2}")
            else:
                score1=+1
                print(f"Score Player 1 is {score1} , Score Player 2 is {score2}")
            
        elif player1 == "paper":
            if player2 == "scissors":
                score2=+1
                print(f"Score Player 1 is {score1} , Score Player 2 is {score2}")
            else:
                score1=+1
                print(f"Score Player 1 is {score1} , Score Player 2 is {score2}")
            
        elif player1 == "scissors":
            if player2 == "rock":
                score2=+1
                print(f"Score Player 1 is {score1} , Score Player 2 is {score2}")
            else:
                score1=+1
                print(f"Score Player 1 is {score1} , Score Player 2 is {score2}")
        else:
            print("That's not a valid play. Check your spelling!")   
        if score1 > score2 :
            print(f"You Win ! Your Choose was {player1} and Computer choose was {player2}  ")
   
        elif score1==score2:
            print(f"Tie ! Your Choose was {player1} and Computer choose was {player2}  ")
        else :
            print(f"Computer Win ! Your Choose was {player1} and Computer choose was {player2}  ")
# *************************************************************************
  #  Single Mood function user choose his input to be compared with random value from computer
def singlePlayer():
    print("It's your Turn Enter (Rock or Paper or Scissors):")
    playerTurn=input("Rock ,Paper , Scissors   :"  )
    listOfInputs=["Rock" ,"Paper","Scissors"]
    ComputerTurn=listOfInputs[randint(0,2)]
    print(f"computer choose ->{ComputerTurn}")
    gameLogic(playerTurn.lower(),ComputerTurn.lower(),player1Score,computerScore)
    continuo=input("if you want to continuo press 1 to end press 2    :")

    if continuo == 1:
        singlePlayer() 
    else :
        print(f"Your Score final score is {player1Score} and Computer Score is {computerScore}  ")
# *****************************************************************
#twoPlayers Methoud 
def twoPlayers():
    print("It's player1 Turn Enter (Rock or Paper or Scissors):")
    playerTurn=input("Rock ,Paper , Scissors   :")
    print("It's player2 Turn Enter (Rock or Paper or Scissors):")
    player2Turn=input("Rock ,Paper , Scissors   :")
  
    gameLogic(playerTurn.lower(),player2Turn.lower(),player1Score,player2Score)
    continuo=input("if you want to continuo press 1 to end press 2  :")
    if continuo == 1:
        singlePlayer() 
    else :
        print(f"Your Score final score is {player1Score} and Computer Score is {player2Score}  ")

#  methoud to navigate to playing mood
def start(): 
  

    print("Welcome TO Rock,paper,scissors Game")
    print("For single player with Computer ->press 1")
    print("For double players              ->Press 2")
    print("Please , Select Your Playing Mood")
    mood = int(input("select 1, 2  :"))

    if mood in (0,1) :
        singlePlayer()
    elif mood in (0,2):
        twoPlayers()

    else:
        print("That's not a valid mood! Try again")
        start()
# *************************************************************************
        

# main to start play    
start()       
      
