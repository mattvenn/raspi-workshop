#mathematical operators +,-,*/
10 - 20
2 * 300
25 / 5
2 + 3 * 5
(2 + 3) * 5


#challenge! find a sum that gives you
#a result you didn't expect...












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









#python can't concatenate strings and integers,
#or floats, so we have to convert them:

int("5") #converts a string to an int
float("5.0") #a string to a float
str(5.2) #an int or a float to a string

print("hello " + str(5.2))


#variables, assign with =
my_num = 25
my_str = "hello"
my_num = my_num + 5
my_str * my_num




#getting user input
name = input("what's your name? ")
print(name)
number = int(input("type a number? "))
print(number)

#challenge! 
#write a program that asks your name and how many times to print it
#then prints your name that number of times






name = input("your name? ") 
number = input("number of times? ") 
print(name * int(number))








#challenge! 
#write a program that asks for a number
#and prints out its square




my_number = input("a number? ")
print(int(my_number) * int(my_number))











#conditionals
10 > 20
10 != 15
my_str == "hello"

#note the spaces at the start of some of the lines
#python separates blocks of code with indentation
#good time to start creating programs with file->new

time = 12
if time < 12:
    print("morning!")
elif time >= 12 and time < 18:
    print("afternoon!")
else:
    print("evening!")
    


#challenge!
#write a program that picks a number, and then
#asks you to guess it. if you get it right, print
#a message, otherwise print "higher" or "lower"



secret = 10

guess = int(input("a number? "))

if guess == secret:
    print("you got it right!")
elif guess < secret:
    print("higher")
else:
    print("lower")







#challenge! write a simple user interface to:

#if the user types 1, print hello
#if the user types 2, print goodbye
#otherwise say "computer says no"









print("press 1 to say hello")
print("press 2 to say goodbye")
choice = int(input("your choice? "))
if choice == 1:
    print("hello")
elif choice == 2:
    print("goodbye")
else:
    print("computer says no")





#loops!
#loop forever
while True:
    print("hello")
    print("matt")
    break



#loop for a certain number of times
loops = 0
while loops < 10:
    print(loops)
    loops = loops + 1

#beginners - jump to library import below...






#break out of a loop
while True:
    password = input("password: ")

    if password == "secret":
        print("correct")
        break
    else:
        print("wrong!")


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
        print("too many guesses!")
        break

    guess = int(input("a number? "))

    if guess == secret:
        print("you got it right!")
        break
    elif guess < secret:
        print("higher")
    else:
        print("lower")









#libraries
import time
time.sleep(5)



#challenge!
#make a loop that prints 'hello' on one line, 
#then 'world' on the next
#with a 1 second delay between each line









import time
while True:
    print("hello")
    time.sleep(1)
    print("world")
    time.sleep(1)
    


#random number library
import random
random.randint(1,10)


#challenge!
#go back to your guessing game:
#set the secret number to be computer generated







secret = random.randint(1,10)
print("you have 10 guesses to pick a number from 1 to 10")





#functions
def my_func(a,b):
    return a * b

print(my_func(20,30))

#challenge!
#write a function that when you call with a number, 
#prints its times table out from 1 to 10











def times(number):
    print("the " + str(number) + " times table")
    loop = 1
    while loop <= 10:
        print(loop, loop * number)
        loop += 1

times(5)
times(3)

#challenge!
#now add something that asks you for the number.













#sabotage!!















#list
my_list = [ "cat", "dog", "mouse" ]
print(my_list[1])

#joining lists into a string - contents of my_list must be strings
":".join(my_list)

#print each item in the list
for i in my_list:
    print(i)

#an easy way to get a range of numbers
my_list = range(10)

#a simpler way of doing a loop a certain number of types
for x in range(5,10):
    print(x)

#splitting a string into an list
string = "cat,dog,mouse"
string.split(',')


#challenge!
#use your function that printed a times table,
#and wrap it in a for loop to print 
#the 1 to 10 times tables









for table in range(1,11):
    times(table)











"""
exceptions
remember the type conversions from the beginning? int(),str(),float()
what happens when we try to convert a string to a float, 
but the string doesn't contain a float?
"""
float("hello")

"""
we can handle exceptions with 2 new keywords, try and except
"""
try:
    float("hello")
except ValueError:
    print("not a float")


#challenge: write a little program that repeatedly asks for the user
#to type a number, and it will only finish when user types a number
#more than 0. The program must be able to handle the case when the 
#user types in something that python can't convert to a number...










while True:
    try:
        a = input("type a float more than 0: ")
        a = float(a)
        if a > 0:
            break
    except ValueError:
        print("not a float")









"""
file IO (input/output)
writing a file
"""
fh = open("myfile.txt",'w')
fh.write("hello world")
fh.close()


    

#file reading:
fh = open("myfile.txt",'r')
print(fh.readlines())



"""
challenge: write a program that reads all the lines of your file,
and prints them out one after the other. 
At the end, display how many lines there were in the file.
"""









fh = open("myfile.txt",'r')
lines = fh.readlines()
line_counter = 0
for line in lines:
    #python2 and 3 differ for suppressing newline with print()
    print(line,end='') #python3 use the end argument set to nothing 
    #print(line), #python2 use a comma after print()
    line_counter += 1
print("there were", line_counter, "lines in the file")



"""
challenge: go back to your times table example. Modify the program so 
instead of printing to the screen, it writes each table to a separate
file
"""












#our function
def times(number):
    file_name = str(number) + ".txt"
    fh = open(file_name,'w')
    fh.write("the " + str(number) + " times table\n")
    loop = 1
    while loop <= 10:
        fh.write( str(number) + " x " + str(loop) + " = " + str( loop * number ) + "\n")
        loop += 1


#run it for the first 10 tables
for table in range(1,11):
    times(table)
