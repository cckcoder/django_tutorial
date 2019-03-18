# Open a file
my_file = open('my_file.txt', 'w')


# Get some info
print('Name: ', my_file.name)
print('Is Closed: ', my_file.closed)
print('Opening Mode: ', my_file.mode)

# Write to file
my_file.write('I love python')
my_file.write(' and JavaScript')
my_file.close()

# Append to file
my_file = open('my_file.txt', 'a')
my_file.write(' I also like PHP')
my_file.close()

# Read from file
my_file = open('my_file.txt', 'r+')
text = my_file.read(100)

print(text)