
## functions and returning values
def atm(initialBalance):
    print("How much do you want to withdraw?")
    withdrawl = input()
    finalBalance = initialBalance - int(withdrawl)
    print("inside fn " + str(finalBalance))
    return finalBalance # finalBalance is returned by the function

balance = 100
balance = atm(balance) # balance is equal to the returned value
print("outside fn " + str(balance))

print(" ")


## functions and global variables
def temperature(celsius):
    global fahrenheit              # making a variable global means it is 
    fahrenheit = celsius*9/5 + 32  # recognised outside the function

print("Please input a temperature in Celsius")
celsius = float(input())
temperature(celsius)
print("That temperature is " + str(fahrenheit) + " in Fahrenheit")
print(" ")

################################################################################


## lists - these are lists of values, stored in square brackets, separated by
##         commas
coloursA = ["purple","red"]
coloursB = ["orange","blue"]
print("coloursA = " + str(coloursA))
print("coloursB = " + str(coloursB))

# you can add lists together (concatenation)
coloursC = coloursA + coloursB
print("coloursA + coloursB = " + str(coloursC))

# you can add strings to list using the method "append"
coloursA.append("green")
print("appending green to coloursA = " + str(coloursA))

# you can reverse the order of a list using the method "reverse"
coloursB.reverse()
print("reversing coloursB = " + str(coloursB))

print(" ")

################################################################################


## string methods
print("Please input a string - use at least 2 words, and upper and lower case (and use quotation marks!)")
testString = input()

# converting a string to upper case
testString = testString.upper()
print("In upper case your string is : " + testString)

# converting a string to lower case
testString = testString.lower()
print("In lower case your string is : " + testString)

# splitting a string into a list of its component words
testList = testString.split()
print("A list of your string's words is : " + str(testList))

print(" ")

################################################################################


## for loops: these are used when we want to repeat a block of code a certain
## number of times
# running over integers
print("running over the integer range (0,5)")
for i in range(0,5):          # NOTE: range(0,5) is 0,1,2,3,4
    print(i)
print(" ")
# running over lists
print("running over the list [red,green,blue]")
for i in ["red","green","blue"]:
    print(i)
print(" ")
# running over strings
print("running over the string Hello")
for i in "Hello":
    print(i)
print(" ")

################################################################################


## you can do the same thing with while loops as with for loops - but for loops
## are quicker!  This while loop does the same thing as the first for loop above
## exercise 3
print("Re-creating the last for loop with a while loop:")
n = 0
while (n < 5):
      print(n)
      n = n + 1
print(" ")
