student= {'name': 'Anutosh', 'age': 21, 'branch': 'ECE', 'subject': ['Maths', 'Economics']}
print(student)

#adding new entry
student['phone'] = 9001624398
student.update({'city': 'Bhopal', 'year': '2nd'}) #if we want to add/update multiple keys at once

#deleting a key
del student['city']

print(student.get('phone','Not found')) #'phone' here is the key whose value we want to know... and 'Not found' is what we'l get for any key whose value is not there
print(student)

#methods
print(len(student)) 
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key.capitalize(), '-', value)
