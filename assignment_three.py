#Research on: List Update, Slicing, Printing
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
student_marks = [80, 56, 78, 90]
#a)Print from Patricia to Phionah
#b)Add marsha at the fourth position
#c)Update  the name Phionah to Phionah Aladddina
#d)Display the length of the students' name list
#e)Print all the students' name using a for loop.
#f)Calculate the total marks for the student marks' variable. 

#a)
print(student_names[1:4])

#b)
student_names.insert(4,'Marsha')

#c)
student_names[3] = 'Phionah Aladddina'
print(student_names)

#d)
print(f"The length of the students' name list is {len(student_names)}.")

#e)
for students in student_names :
 print(students)

#f)
total_marks = sum(student_marks)
print(f"The sum of the students' marks is {total_marks}.")







