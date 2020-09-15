# input no 1
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really? \n")

# input test 2
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really? \n")

# # input wrong
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# input right
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something, "\n")

# Hypotenuse 
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo, "\n") # as same as print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# Hypotenuse Using str without commas
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# string input
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# Replication
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Final
a = 6.0
b = 3.0

# output the result of addition here
add = a+b
# output the result of subtraction here
sub = a-b
# output the result of multiplication here
mul = a*b
# output the result of division here
div = a/b
print("Result is : Add = ",add," Sub = ",sub," Multiply = "+str(mul)+" Div = "+str(div))
print("\nThat's all, folks!")

# TestLAB
x = float(input("Enter value for x: "))

y = 1/(x+1/(x+1/(x+1/x)))

print("y =", y)