from mymodule.helper_utils import square

print("Practicing Variables")

myvar = 5
print(f"Variable myvar : {myvar} is an {type(myvar)}")

print("Done Practicing Variables")

print("Hello World") #Output hello world

#taking in user input and assigning it to variable myname
myname = input("What is your name: ")

#printing and concatenating as a string the user input of myname
print("Hello " + str(myname))

#printing using formatting
print("Hello %s" % myname)

i = 600
print(f"Var i contains the value {i}")

f= 3.1415926 
print(f"Var f contains the value {f} and its of type {type(f)}")

b = False
print(f"Var b has the value {b}")

n = None
print(f"Var n has the value {n}")

#Tuple
c = (5,15,25)


#List
l = ["Sabrina", "Dilpreet", "Grace"]
l = [400, 43.34]
print(f"l[0] contains the val {l[0]} and is of type: {type(c)}") 

#sets the variables

s = set()
s.add(10)
s.add(20)
s.add(40)
print(s)

#dictionary with values
grades = {
    "Thomas" : "A+",
    "Marcus" : "C+"
}

grades["Thomas"]
grades["Annasophia"] = "D+"

#empty dictionary
mydictionary1 = dict()


#conditionals
x =100

if (x > 0):
    print("X is positive")
elif(x < 0):
    print("X is negative")
else:
    print("X is zero")


#loops
for i in range(5):
    print(i)

for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}")

#functions
def is_even(x):
    if (x% 2) == 0:
        return True
    else:
        return False
        

print(square(100))