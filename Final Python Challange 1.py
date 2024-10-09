# Assign an integer to a variable
int_var = 5

# Assign a string to a variable
str_var = "Hello, World!"

# Assign a float to a variable
float_var = 3.14

# Use the print() function to print out the variables
print(int_var, str_var, float_var)

# Use each of these operators: +, *, /, =, %
sum_var = int_var + float_var  # addition
mult_var = int_var * float_var  # multiplication
div_var = int_var / float_var  # division
mod_var = int_var % 3  # modulus
# The '=' operator was used in all assignment statements above

# Logical operators: and, or, not
if (int_var < 10) and (float_var < 4.0):
    print("Both conditions are true")

if (int_var > 10) or (float_var < 4.0):
    print("At least one condition is true")

if not (int_var == 10):
    print("int_var is not equal to 10")

# Conditional statements: if, elif, else
if int_var > 5:
    print("int_var is greater than 5")
elif int_var == 5:
    print("int_var is equal to 5")
else:
    print("int_var is less than 5")

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# For loop
for i in range(3):
    print("For loop iteration:", i)

# Create a list and iterate through that list using a for loop
my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)

# Create a tuple and iterate through it using a for loop
my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)

# Define a function that returns a string variable
def get_greeting():
    return "Hi there!"

# Call the function defined above and print the result
result = get_greeting()
print(result)