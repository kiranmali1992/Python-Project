#...........................Tic Tac Toe project..............................................

print("\t\t\tWellcome to Tic Tac Toe")

#Empty list for name of Player
myname = []

x = ["st","nd"]

#Empty list for postion on board
pos = [0,0]

#Empty list for taking input from player
player_input = []
i = 0

#Inializing board value
myboard =["_"for i in range(9)]

#Taking player name
for i in range(2):
    name = input(f"Enter {i+1}{x[i]} Player name::")
    myname.insert(i,name)
    name = 0
print("")
print(f"\t\t {myname[0]} and {myname[1]} start playing game")
 
#Draw board for tictactoa
def board(myboard):
    #myboard.insert(pos1,Player1_input) 
    print("\t\t  ",myboard[0],"\t\t",myboard[1],"\t\t",myboard[2])
    print("\t\t","_"*10, "|" ,"_"*10,"|","_"*10)
    print("\t\t  ",myboard[3],"\t\t",myboard[4],"\t\t",myboard[5])
    print("\t\t","_"*10,"|","_"*10,"|","_"*10)
    print("\t\t  ",myboard[6],"\t\t",myboard[7],"\t\t",myboard[8])
    print("\t\t","_"*10,"|","_"*10,"|","_"*10)
#Call function borad
print("")
board(myboard)

#Check if any pair match
def Check_pair(myboard):
    
        if(myboard[0] == myboard[1]== myboard[2]):
            result = myboard[0]
            final(result)

        elif(myboard[6] == myboard[7]== myboard[8]):
            result = myboard[6]
            final(result)
            
        elif(myboard[3] == myboard[4]== myboard[5]):
            result = myboard[3]
            final(result)
            
        elif(myboard[0] == myboard[3]== myboard[6]):
            result = myboard[0]
            final(result)
            
        elif(myboard[1] == myboard[4]== myboard[7]):
            result = myboard[1]
            final(result)
            
        elif(myboard[2] == myboard[5]== myboard[8]):
            result = myboard[2]
            final(result)
            
        elif(myboard[0] == myboard[4]== myboard[8]):
            result = myboard[0]
            final(result)
            
        elif(myboard[2] == myboard[4]== myboard[6]):
            result = myboard[2]
            final(result)
            
        else:
            print("Game is tie")
            
    
#Function for deciding winner of game
def final(result):
    if(result == "X"):
            if(pos[0] == "X"):
                print(f"Hurry! {myname[0]} has won the game")
            else:
                print(f"Hurry! {myname[1]} has won the game")
                          
    if(result == "O"):
        if(pos[0] == "O"):
            print(f"Hurry! {myname[0]} has won the game")
            
        else:
            print(f"Hurry! {myname[1]} has won the game")
            
            
    
    
#Make player to select their mark X or O
print("Player please select noughts(O) and crosses(X) ")
for i in range(2):
    Input = input(f"{myname[i]}::")
    player_input.append(Input)


#list for selecting position of block
Board_position =[0,1,2,3,4,5,6,7,8]

# Check if any position in board is empty
while("_" in myboard):
    
#Taking Position on board from user
    if((player_input[0] == "X" or player_input[0] == "O") and (player_input[1] == "X" or player_input[1] == "O")):
        #Ask player to select position from board
        print("\nSelect Positon from board",tuple(Board_position))
        try:
            #Enter the position as input
            pos[i] =int(input(f"{myname[0]} Please tell at what position you want to fill {player_input[i]}::"))
        except Exception as e:
            print(e)

        #Check if given position is present in the board            
        if((pos[i] in Board_position)):
            print("You have selected position on board",pos[i])
            myboard[pos[i]] = player_input[i]
            print("")
            #Call the function of board
            board(myboard)
            print("")
            #Removing the position from block
            Board_position.remove(pos[i])
            
            Board_position.insert(pos[i],player_input[i])
            if i == 0:
                i = 1
            else:
                i = 0
            continue         
        else:
            print("Position you enter is allready filled")
           
    else:
        print("Please enter correct noughts(O) and crosses(X)")
        break

else:
    Check_pair(myboard)
        

