#Andrew Robinson
#8/17/2022
#Rock Paper Scissors Game

from asyncio.windows_events import NULL
import time
import random

print("Lets Play:")
print("Rock, Paper Scissors")

#delay asking for user Input to feel more game-like
#time.sleep(1)


userWins = 0
computerWins = 0

while(userWins < 3 and computerWins < 3):
    
    time.sleep(1)
    userMove = input("Enter move:")

    userMoveNumber = 0

    if (userMove == "rock" or userMove == "Rock"):
        userMoveNumber = 1
    
    elif (userMove == "paper" or userMove == "Paper"):
        userMoveNumber = 2
    
    elif (userMove == "scissors" or userMove == "Scissors"):
        userMoveNumber = 3
    else:
        time.sleep(1)
        print("Invalid move")
    
    #computerMoveNumber ID:
    #1 for rock, 2 for paper, 3 for scissors
    computerMoveNumber = random.randrange(1, 4)
    computerMove = NULL                             #each round of game randomize enemy move number
    
    if(computerMoveNumber == 1):
        computerMove = "rock"
    if(computerMoveNumber == 2):
        computerMove = "paper"
    if(computerMoveNumber == 3):
        computerMove = "scissors"
        
    
    if(userMoveNumber == 1 and computerMoveNumber == 2):        #Player has Rock
        computerWins += 1                                           #Computer has Paper            
                                    #Player Wins
        time.sleep(1)
        print("computer move: paper")
        time.sleep(1)
        print("computer wins round and scores a point")
        time.sleep(1)
        print(f"The score is now {userWins} to {computerWins}")
    
    elif(userMoveNumber == 1 and computerMoveNumber == 3):
        userWins += 1
       
        time.sleep(1)
        print("computer move: scissors")
        time.sleep(1)
        print("player wins round and scores a point")
        time.sleep(1)
        print(f"The score is now {userWins} to {computerWins}")
        
    elif(userMoveNumber == 1 and computerMoveNumber == 1):
       
        time.sleep(1)
        print("computer move: rock")
        time.sleep(1)
        print("This round is a draw")
        time.sleep(1)
        print(f"The score is still {userWins} to {computerWins}") 
        
    elif(userMoveNumber == 2 and computerMoveNumber == 1):        #Player has Rock
        userWins += 1                                           #Computer has Paper            
                                     #Player Wins
        time.sleep(1)
        print("computer move: rock")
        time.sleep(1)
        print("player wins round and scores a point")
        time.sleep(1)
        print(f"The score is now {userWins} to {computerWins}")
    
        
    elif(userMoveNumber == 2 and computerMoveNumber == 3):
        computerWins += 1
        
        time.sleep(1)
        print("computer move: scissors")
        time.sleep(1)
        print("computer wins round and scores a point")
        time.sleep(1)
        print(f"The score is now {userWins} to {computerWins}")

        
    elif(userMoveNumber == 2 and computerMoveNumber == 2):
       
        time.sleep(1)
        print("computer move: paper")
        time.sleep(1)
        print("This round is a draw")
        time.sleep(1)
        print(f"The score is still {userWins} to {computerWins}")   
        
    elif(userMoveNumber == 3 and computerMoveNumber == 1):
        computerWins += 1
        
        time.sleep(1)
        print("computer move: rock")
        time.sleep(1)
        print("computer wins round and scores a point")
        time.sleep(1)
        print(f"The score is now {userWins} to {computerWins}")
        
    elif(userMoveNumber == 3 and computerMoveNumber == 2):
        userWins += 1
       
        time.sleep(1)
        print("computer move: paper")
        time.sleep(1)
        print("player wins round and scores a point")
        time.sleep(1)
        print(f"The score is now {userWins} to {computerWins}")
    elif(userMoveNumber == 3 and computerMoveNumber == 3):
       
        time.sleep(1)
        print("computer move: scissors")
        time.sleep(1)
        print("This round is a draw")
        time.sleep(1)
        print(f"The score is still {userWins} to {computerWins}")              
                 
        
   
        
  
    
    
   

#check whether game should continue or end
time.sleep(1)

if(userWins == 3 and computerWins == 0):
    print("Player has 3 points and wins the Match!")
    time.sleep(1)
    print("Flawless Victory!")
    
elif(computerWins == 3 and userWins == 0):
    print("Computer has 3 points and wins the match!")
    time.sleep(1)
    print("Flawless Victory!")
    
elif(userWins == 3):
     print("Player has 3 points and wins the Match!")
     
elif(computerWins == 3):
    print("Computer has 3 points and wins the match!")
    
time.sleep(1)
print("Game Over")
    
