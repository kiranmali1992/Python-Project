#Mini project on Snake and Ladder Game
import time
import random

#Pointer used for passing dice from one player to another 
flage = 0

# Variable hold ladder dictionary value for corresponding key
position_inc = 0

#Variable hold Snake dictionary value for corresponding key
position_dec = 0

#Hold Score of player
Current_Position1 = Current_Position2 = 0

print("\t\t\tWellcome to Snake and Ladder Game")
#Taking First Player name from user
name1 =input("\n>>Please enter name of first player:")

#Taking second player name from user
name2 =input(">>Please enter name of Second player:")

print("\n\t\t\tStart playing game")
    
    
    

#Function return score with help of snake and ladder dictionary
def Snake_Ladder(x):
#User define snake bite dictionary
    snake ={
        62:19,
        17:7,
        54:34,
        87:36,
        98:76,
        93:73,
        54:34,
        64:60
        }
#Condition for checking given key is present in snake dictionary
    if(snake.get(x)):
        global position_dec
        position_dec = snake.get(x)
        print(">>So Sorry, You have been bite by snake,Now your score come down by:",position_dec)

#User define ladder dictionary      
    ladder = {
        1:38,
        4:14,
        9:31,
        28:84,
        80:99,
        51:67,
        72:91,
        21:42
        }
    
#Condition for checking given key is present in ladder dictionary
    if(ladder.get(x)):
        global position_inc
        position_inc = ladder.get(x)
        print(">>hooray!,You are on Ladder, Now your Score increase by:",position_inc)
    return position_dec,position_inc



while(1):    
    if(Current_Position1 <= 100 and Current_Position2 <= 100):
        if(flage == 0):
            Enter1 = input(f"\n>>{name1} Press enter key to roll a dice:")
            print("Dice is rolling........")
            #wait for 3s delay
            time.sleep(3)
            
            # output for dice rolled given by random value
            Num1 = random.randint(1,6)
            
            print(Num1)

            #Place output of dice rolled in Current_Position1
            Current_Position1 += Num1 

            #Calling Snake_Ladder function
            Snake_Ladder(Current_Position1)
            
            if(position_inc != 0):
                
                #Update Current_Position1 variable with position_inc
                Current_Position1 =  position_inc
                
            elif(position_dec != 0):
                
                #Update Current_Position1 with position_dec
                Current_Position1 =  position_dec
            
            
            
            if(Current_Position1 == 100):
                print(f"{name1} Congratulation you have won the game")
                break
            elif(Current_Position1 > 100):
                print(f"Your score exceed by {Current_Position1 - 100},Please wait next chance")
                Current_Position1 -= Num1
                
            print(f"Your total score is: ",Current_Position1)
            flage = 1
            position_inc = position_dec = 0
            
        elif(flage == 1):
            Enter1 = input(f"\n{name2} Press enter key to roll a dice")
            print("Dice is rolling........")
            #wait for 3s delay
            time.sleep(3)
            
            Num2 = random.randint(1,6)
            print(Num2)
            
            #Place output of dice rolled in Current_Position2
            Current_Position2 += Num2
            
            #Calling Snake_Ladder function
            Snake_Ladder(Current_Position2)
            
            if(position_inc != 0):
                #Update Current_Position2 with position_inc
                Current_Position2 =  position_inc
            elif(position_dec != 0):
                #Update Current_Position2 with position_dec
                Current_Position2 =  position_dec

            if(Current_Position2 == 100):
                print(f"{name2} Congratulation you have won the game")
                break
            elif(Current_Position2 > 100):
                print(f"Your score exceed by {Current_Position2 - 100},Please wait next chance")
                Current_Position2 -= Num2
                
            print("Your total score is:",Current_Position2)
            flage = 0
            position_inc = position_dec = 0
    










        
        
    
   

