message = 'Hello Anutosh'
print(message) #print's what is inside the message
print(len(message)) #print's the length 
print(message[6]) #print's the index (first word's index is cosidered to be 0)
print(message[6:14])

#methods

print(message.upper())
print(message.lower())

#string concatenation

greeting = 'Hello'
name = 'Anto'

new_message = greeting + ', ' + name #simple method

new_way = '{}, {}'.format(greeting, name) #String formatting (placeholders and format method)

fString_way = f'{greeting}, {name}' #newest format

print(new_message)
print(new_way)
print(fString_way)

#casting (its basically changing one data type to another)
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)