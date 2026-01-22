n = 5 # No. of students

fields = ['Name', 'Roll', 'Marks']

student = list()

# Input

for i in range(n):
    print('Student',i,':')
    dict = {}
    for field in fields:
        print('Enter', field,':')
        inp = input()

        match field:
            case 'Roll':
                inp = int(inp)
            
            case 'Marks':
                inp = float(inp)
        
        dict[field] = inp
    student.append(dict)


# Finding highest marks

max_marks = student[0]['Marks']
max_name = student[0]['Name']
max_roll = student[0]['Roll']

for i in range(1,n):
    marks_i = student[i]['Marks']

    if(marks_i>max_marks):
        max_marks = marks_i
        max_name = student[i]['Name']
        max_roll = student[i]['Roll']

# Display
print('Student with highest marks: Name:', max_name, 'Roll:', max_roll, 'Marks:', max_marks)
