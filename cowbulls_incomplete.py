import random
# the functions : getDigits / noDublicates / generateNumber where added 
# to avoid user confusion and program error in case the random number has duplicate digits
# by Muhammad bagosher
def getDigits(number): # define a function that counts the number of digits and makes them into a list by muhamamd bagosher
    return [int(i) for i in str(number)] 


def noDuplicates(number): #uses digits list to check for dublicates by muhamamd bagosher
    num_li = getDigits(number) 
    if len(num_li) == len(set(num_li)): 
        return True
    else: 
        return False

def generateNumber(): #function that generates a random 4 digit number by muhamamd bagosher
    while True: 
        num = random.randint(1000,9999) 
        if noDuplicates(num): #uses the noDuplicate function to keep looping until the random number generated has no dublicate digits
            return num 

def compare_numbers(number, user_guess):
    ## your code here / added function code by muhammad bagosher
     cowbullcount = [0 , 0] #starts a list to save number of cows in index 0 and bulls in 1  
     number_str = str(number) #changes int to str and assigns to a new variable to check for similarity in digits
     user_guess_str = str(user_guess) #changes int to str and assigns to a new variable to check for similarity in digits
     for i in range(4): #starts a loop to check for similarity in digits of the number and userguess
        # common digit exact match 
        if user_guess_str[i] == number_str[i]: 
            cowbullcount[1] += 1 # adds 1 to the bull index[1]
            
        # common digit match but in wrong position 
        elif user_guess_str[i] in number_str:
            cowbullcount[0] += 1 # adds 1 to the cow index [0]
     return cowbullcount
        

playing = True #gotta play the game
number = generateNumber() #random 4 digit number / changed 0 to 1000 to make it always 4 digit by muhammad bagosher
guesses = 0

#print (number)  -  removed the print function before the program starts by muhammad bagosher

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = int(input("Give me your best guess!(enter 4 digits)")) #removed raw_ and replaced it with int() by muhammad bagosher
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + " tries! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
