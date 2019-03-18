class User:

	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age

	def greeting(self):
		return f'My name is {self.name} and I am {self.age}'

	def has_birth_day(self):
		self.age += 1



class Customer:

	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age
		self.balance = 0


	def set_balance(self, balance):
		self.balance = balance

	def greeting(self):
		return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

# Init customer

john = Customer('John Doe', 'Jonh@gmail.com', 45)

john.set_balance(500)

print(john.greeting())
