
## Hello world
welcome = "Hello World"    # define a new variable containing a string
print(welcome)             # print the variable we created

###############################################################################


## user input
print ("What is your name?")   # print a question to the screen
name = input()                 # wait for the user to input the variable 'name'
print ("Hello " + name)        # concatenation: adding strings, and output

###############################################################################


## the random module
import random                  # loads functions which create random values
value = random.randint(1,6)    # generate a random integer between 1 and 6
print ("our random integer is " + str(value))
# NOTE: 'value' is an integer - we convert it to a string with 'str(value)'
#        so that we can print it out with the string "our random integer is "

###############################################################################


## rolling three dice: exercise 4
# asking the user how many sides each dice should have:
print (" ")
print ("How many sides would you like dice 1 to have?")
sides1 =  int(input())
print ("How many sides would you like dice 2 to have?")
sides2 =  int(input())
print ("How many sides would you like dice 3 to have?")
sides3 =  int(input())
# NOTE: The input from the user is a string.  We need to convert it to an
#       integer using int()

# rolling each dice:
roll1 = random.randint(1,sides1)
roll2 = random.randint(1,sides2)
roll3 = random.randint(1,sides3)

# adding the roll of each dice together and outputting the answer
roll =  roll1 + roll2 + roll3
print ("The sum of the three rolls is " + str(roll))
print(" ")

###############################################################################


## conditionals: exercise 5
# setting some variables
a = 5
b = 10
# outputting the results of some conditional statements
print("a > b : " + str(a > b))                 # > greater than
print("a < b : " + str(a < b))                 # < less than
print("a+b == b+a : " + str(a+b == b+a))       # == exactly equal to
print("a-b == b-a : " + str(a-b == b-a))
print("a*b == b*a : " + str(a*b == b*a))
print("a/b != b/a : " + str(a/b != b/a))       # != not equal to
print("a+b >= b+a : " + str(a+b >= b+a))       # >= greater than or equal to
print("a-b <= b-a : " + str(a-b <= b-a))       # >= less than or equal to
print(" ")

###############################################################################


## While loops - remember the colon!
x = 0
while (x<5):         # indented code runs while x is less than 5
    print(x)
    x = x+1          # adds 1 to x
print(" ")

###############################################################################


## If loops - remember the colon!
randomNumber = random.randint(1,20)           # create a random number
print("Please guess a number between 1 and 20")
guess = int(input())                          # convert user input to integer
if (randomNumber > guess):                    
    print ("Your guess was too low!")         # runs only if randomNo > guess
elif (randomNumber < guess):
    print("Your guess was too high!")         # runs only if randomNo < guess
else :                            # runs if randomNo is neither < nor > guess
    print("Congratulations! You guessed right!")
print(" ")

###############################################################################


## Guessing game - exercise 5
print("This is a guessing game!")
print ("You need to guess the number, between 1 and 20")
print("How many guesses would you like?")
NoGuessesAllowed = int(input()) # asking the user for the no. of allowed guesses
guessestaken = 0                # no guesses have been taken at the start

answer = random.randint(1,20)   # setting our random number

# while loop runs while the number of guesses taken is
# less or equal to than the number of guesses allowed
while (guessestaken < NoGuessesAllowed):
    print("Make a guess!")
    guess = int(input())       # get user's guess

    if (guess > answer):       # runs if guess > answer
        print("Too high! ")     
    elif (guess < answer):     # runs if guess < answer
        print("Too low! ")
    else:                      # runs if guess == answer
        print("Congratulations! You win!")
        break                  # exits the if loop

    guessestaken = guessestaken + 1    # counts no. of guesses taken

    if (guessestaken == NoGuessesAllowed):
        print("Game over! The number was " + str(answer))  # ends the game

###############################################################################

        
## functions
print(" ")
def greeting(name):                   # everything in this indented block is
    print("Welcome " + name)          # part of the function called "greeting"

greeting("Sophy")          # This calls the function "greeting"
greeting("Angus")          # The entry in the bracket is the argument
greeting("Callum")
print(" ")

###############################################################################

## A function for guess quality indicator -  exercise 7
def quality(guess,answer):                # This is a guess-quality function
    diff = guess - answer                 
    if ((diff >= -2) and (diff <= 2)):    # This uses the boolean operator 'and'
        print("You're getting hot!")
    elif ((diff >= -4) and (diff <= 4)):
        print("You're getting warm!")
    else:
        print("You're still cold!")

print("This is a guessing game with functions!")
print ("You need to guess the number, between 1 and 20")
print("We'll let you know if your guess is hot, warm or cold")
print("How many guesses would you like?")
NoGuessesAllowed = int(input()) # asking the user for the no. of allowed guesses
guessestaken = 0                # no guesses have been taken at the start

answer = random.randint(1,20)   # setting our random number

# while loop runs while the number of guesses taken is
# less or equal to than the number of guesses allowed
while (guessestaken < NoGuessesAllowed):
    print("Make a guess!")
    guess = int(input())       # get user's guess

    if (guess > answer):       # runs if guess > answer
        print("Too high! ")
        quality(guess,answer)
    elif (guess < answer):     # runs if guess < answer
        print("Too low! ")
        quality(guess,answer)
    else:                      # runs if guess == answer
        print("Congratulations! You win!")
        break                  # exits the if loop

    guessestaken = guessestaken + 1    # counts no. of guesses taken

    if (guessestaken == NoGuessesAllowed):
        print("Game over! The number was " + str(answer))  # ends the game
