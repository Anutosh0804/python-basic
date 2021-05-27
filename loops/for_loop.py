nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

#break
for num_1 in nums:
    if num_1==3:
        print('Found it')
        break
    print(num_1)

#continue
for num_2 in nums:
    if num_2==3:
        print('Found it')
        continue
    print(num_2)

#loop in loop
for num in nums:
    for letters in 'abc':
        print(num, letters)