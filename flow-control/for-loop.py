'''
for val in sequence:
	Body of for
'''

abc = [2, 6, 4, 9, 1, 7, 8]
sum_of_array = 0

for i in abc:
    sum_of_array = i + sum_of_array

print("The sum of array/list abc[] is {}".format(sum_of_array))

# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index

for i in range(len(genre)):
    print("I like", genre[i])

# for loop with else

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# for with if-else : program to display student's marks from record

student_name = 'James'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
