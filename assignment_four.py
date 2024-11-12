# class Cohort : #Termination
#     name
#     description
#     start_date
#     stop_date
#Research on constructors.
#1.Add a constructor for the cohort class.
#2.Add a method to the class that prints the cohort name and the total number of students.
#3.Creates a new instance for the cohort class. 


#Adding a constructor
class Cohort:
    def __init__(self, name, description, start_date, stop_date, total_students) :
        self.name = name
        self.description = description
        self.start_date = start_date
        self.stop_date = stop_date
        self.total_students = total_students

# Method to print cohort name and the total number of students, in this case will be considered the cohort details.
    def cohort_details(self) :
        print(f"The name of the cohort is {self.name}.")
        print(f"The number of the students in {self.name} is {self.total_students}")

# Creaing an instance.
cohort_4 = Cohort(
    "Cohort 4", "The latest Computer Science intake at WITI.", "25th August 2024", "25th May 2026", 54
)

cohort_4.cohort_details()