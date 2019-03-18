import json

# Sample JSON

user_json = '{"first_name":"Jonh", "last_name": "Doe", "age": 30}'

user = json.loads(user_json)

print(user)
print(user['first_name'])


car = {
	'make': 'Ford',
	'mode': 'Mustang',
	'year': 1970,
}

car_json = json.dumps(car)

print(car_json)