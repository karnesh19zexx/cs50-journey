#VARIABLES, ARGUMENTS, COMMENTS 

name = input("What's your name?: ")  #08/02/2026  Day -1
print("Hello "+name+"!")             


###################################   #09/02/2026  Day -2

# Alternative way to print the greeting


# name = input("What's your name?: ")
# greeting = ("Hello " , name + " !")
# print(name)

#comments

#This is a regular comment

""" This is a multi-line comment"""  #Uses three conseutive str


###################################

#Topic end= :

name = input("What's your name?: ") 
print("Hello, ", end="")
print(name)             

####################################

#Topic sep= :

name = input("What's your name?: ") 
print("Hello, ", name,sep="!")
            

#Rare case - I - need string in output

# print("hello, 'friend' !") 
                #or

# print('hello, "friend" !') 
                #or

print("hello, \"friend\" !")  #known as escaping the double quotes

#############################################

#Topic strip() - removes the leading and trailing spaces

name = input("What's your name?: ")
#name = name.lstrip() #removes the leading spaces
#name = name.rstrip() #removes the trailing spaces
name = name.strip()  #removes both leading and trailing spaces
print("Hello, ", name)

################################################

#Topic capitelize() - converts the first character to uppercase and the rest to lowercase

name = input("What's your name?: ")
name = name.capitalize()    
print("Hello, ", name)

#################################################

#Topic title() - converts the first character of each word to uppercase and the rest to lowercase

name = input("What's your name?: ")
name = name.title()
print("Hello, ", name)

##################################################

#Topic multi-function chaining

name = input("What's your name?: ")
name = name.strip().capitalize()   #does both strip and capitalize in one line
print("Hello, ", name)

####################################################

#Topic f string / split() splits a string into a list of substrings based on a specified delimiter (default is whitespace)

name = input("What's your name?: ")
first, last = name.split()  #splits the name into first and last name
print(f"Hello,{first}" )