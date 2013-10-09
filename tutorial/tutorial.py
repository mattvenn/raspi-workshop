#mathematical operators +,-,*/
10 - 20
2 * 300
25 / 5
2 + 3 * 5
(2 + 3) * 5


#challenge! find a sum that gives you a result you didn't expect...












#answer
25 / 6


#floats
5.0 / 25

#strings
"hello"
"hello" + "world"
"hello" * 25
"hello" + 5


#question: why doesn't the last example work?









#python can't concatenate strings and integers (or floats)
#so we have to convert them:

int("5") #converts a string to an int
float("5.0") #a string to a float
str(5.2) #an int or a float to a string

print "hello " + str(5.2)


#variables, assign with =
my_num = 25
my_str = "hello"
my_num = my_num + 5
my_str * my_num




#getting user input
name = raw_input("what's your name? ")
print name
number = int(raw_input("type a number? "))
print number

#challenge! 
#write a program that asks your name and then prints it out 10 times




name = raw_input("your name? ") 
print name * 10








#challenge! 
#write a program that asks for a number and prints out its square




my_number = raw_input("a number? ")
print int(my_number) * int(my_number)












#conditionals
10 > 20
10 != 10
my_str == "hello"

time = 12
if time < 12:
    print "morning!"
elif time >= 12 and time < 18:
    print "afternoon!"
else:
    print "evening!"
    


#challenge! (save this to a new program)
#write a program that picks a number, and then asks you to guess it.
#if you get it right, print a message, otherwise print "higher" or "lower"



secret = 10

guess = int(raw_input("a number? "))

if guess == secret:
    print "you got it right!"
elif guess < secret:
    print "higher"
else:
    print "lower"








#loops!
#loop forever
while True:
    print "hello"
    print "matt"



#loop for a certain number of times
loops = 0
while loops < 10:
    print loops
    loops = loops + 1




#break out of a loop
while True:
    password = raw_input("password: ")

    if password == "secret":
        print "correct"
        break
    else:
        print "wrong!"


#challenge!
#go back to your guessing number game:
#add a loop so you have to keep guessing
#when you get the right answer, break out of the loop.
#for bonus marks, limit the number of guesses to 10





guesses = 0
secret = 10

while True:
    guesses = guesses + 1
    if guesses > 10:
        print "too many guesses!"
        break

    guess = int(raw_input("a number? "))

    if guess == secret:
        print "you got it right!"
        break
    elif guess < secret:
        print "higher"
    else:
        print "lower"









#libraries
import time
time.sleep(5)



#challenge!
#make a loop that prints 'hello' on one line, then 'world' on the next
#with a 1 second delay between each line









import time
while True:
    print "hello"
    time.sleep(1)
    print "world"
    time.sleep(1)
    


#random number library
import random
random.randint(1,10)


#challenge!
#go back to your guessing game:
#set the secret number to be computer generated







secret = random.randint(1,10)
print "you have 10 guesses to pick a number from 1 to 10"





#functions
def my_func(a,b):
    return a * b

print my_func(20,30)

#challenge!
#write a function that when you call with a number, prints its
#times table out from 1 to 10











def times(number):
    print "the " + str(number) + " times table"
    loop = 1
    while loop <= 10:
        print loop, loop * number
        loop += 1

times(5)
times(3)








#arrays
array = [ "cat", 100.5, False ]

print array[1]

for i in array:
    print i

array = range(10)

for x in range(5,10):
    print x



#challenge!
#use your function that printed a times table, and wrap it in a for loop to print 
#the 1 to 10 times tables









for table in range(1,11):
    times(table)









