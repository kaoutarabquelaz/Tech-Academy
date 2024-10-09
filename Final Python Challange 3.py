# Get the user's name
Name = input('Name: ')

# Greet the user and explain the purpose of the program
print("Hello " + Name + "! We are going to find out how long you have been alive!")

# Get age from user and convert to integer
Age = int(input('How old are you? '))

# Let the user know their age
print('You are ' + str(Age) + ' years old.')

# Convert years to months
Months = Age * 12

# Convert years to days
Days = Age * 365

# Show calculated number of months and days to user
print(Name + ' has been alive for about: ' + str(Months) + ' months or ' + str(Days) + ' days!')