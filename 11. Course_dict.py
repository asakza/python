# Task 1: Write program in which student can register in different courses:
# 1- Ask student name, age, email, phone no etc
# 2- Ask to choose from courses like ai, cnc, bcc,iot, web3 etc
# 3- Allow  student to select multiple courses
# 4- Save courses as list in student dictionary

selected_courses = []
courses_available = ["AI", "CNC", "BCC", "IOT", "WEB3"]
std_dict = {}

std_name = input('Please Enter You Name ')
std_age= int(input('Please Enter your age '))
courses_enrollment = int(input('Please Enter number of courses you want to enroll? '))

for crs in range(courses_enrollment):
    selected_course=input('Please Enter your course name Options available are \n "AI", "CNC", "BCC", "IOT", "WEB3"\n')
    selected_courses.append(selected_course)

std_dict = {"Student_name": {std_name} ,"Courses_selected" : selected_courses}

for crrs in std_dict.items():
    print(crrs)
    