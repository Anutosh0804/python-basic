courses = ['Math', 'Physics', 'Computer', 'Economics']

print(courses)

print(len(courses))

#methods
print(courses[0]) #prints the 1st character
print(courses[-1]) #prints the last character
print(courses[:2]) #prints every index from start to one before the mentioned index
print(courses[2:]) #prints every index from the mentioned no in the start till the end index

#adding more character in the list

courses.append('Finance') #adds the character in the last of the list
courses.insert(2, 'Python') #adds the character at the index we mention

courses_2 = ['Quant', 'Stats']
courses.extend(courses_2) #merge the values of one list into another

print(courses)

#removing values from the list
courses.remove('Stats') #remove the mentioned vlue from the list
popped = courses.pop()

print(popped)

print(courses)

#sorting
courses.sort() #sort in alphabetical order(if list contains no then it sorts in ascending order)
print(courses)

print(courses.index('Python')) #tells the index of the given value
print('Art' in courses) #tells weather the given value is in the list or not

#list to str and vice-versa
name = ['Anutosh', 'Ajay', 'Anant', 'Aryan']

name_str= ', '.join(name)
print(name_str)

name_list= name_str.split(', ')
print(name_list)