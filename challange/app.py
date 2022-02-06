# import csv

# from app.student import Student


# class FetchStudentDetails:
#     student_list = None
#     headers = None

#     def __init__(self):
#         self.headers = []
#         self.student_list = []

#     @staticmethod
#     def clean_input(row):
#         """
#         Clean and sanitize the input so that it does not contain leading and trailing spaces
#         """
#         return [r.strip() for r in row]

#     @staticmethod
#     def map_csv_to_class(row):
#         """
#         Convert the input row into a Student class
#         """
#         return Student(*row)

#     def get_data(self, file_name="./app/data/student_details.csv"):
#         """
#         Fetch the data from the given csv file and construct the list of Student objects
#         """
#         with open(file_name, newline="") as _file:
#             reader = csv.reader(
#                 _file,
#                 delimiter=",",
#                 quotechar='"',
#                 quoting=csv.QUOTE_ALL,
#                 skipinitialspace=True,
#             )
#             # set here self.headers (first row)
#             self.headers
#             # set here self.student_list consider using clean_input() and map_csv_to_class()
#             self.student_list(self.clean_input(), self.map_csv_to_class())
#             for name , student_id , age, subjects , grade, average_score in reader:
#                 #we convert the numbers to floats.
#                 student_id = float(student_id)
#                 age = float(age)
#                 average_score = float(average_score)
                
#                 # Now we create the Student instance and append it to the list.
#                 self.student_list.append(Student(name, (score1, score2), rank))
                
#         return self.student_list

#     def get_super_student(self):
#         """
#         Get super student
#         """

#     def get_attendance(self, attendance_file_name="./app/data/attendance.csv"):
#         """
#         Fetch data from given csv file and update students attendance