student_name = input(' Please Enter Your Name ')

#*********Information for Total alloted marks
mx_marks_maths = int(input(' Please Enter Total marks for Mathematics '))
mx_marks_English = int(input(' Please Enter Total marks for English '))
mx_marks_Physics = int(input(' Please Enter Total marks for Physics '))
mx_marks_Chemistry = int(input(' Please Enter Total marks for Chemistry '))
mx_marks_Urdu = int(input(' Please Enter Total marks for Urdu '))
mx_marks_Social_science = int(input(' Please Enter Total marks for Social_science '))
mx_marks_total = mx_marks_maths + mx_marks_English + mx_marks_Physics + mx_marks_Chemistry + mx_marks_Urdu + mx_marks_Social_science
#********* Total marks obtained
obt_marks_maths = int(input(' Please Enter Obtain marks for Mathematics '))
obt_marks_English = int(input(' Please Enter Obtain marks for English '))
obt_marks_Physics = int(input(' Please Enter Obtain marks for Physics '))
obt_marks_Chemistry = int(input(' Please Enter Obtain marks for Chemistry '))
obt_marks_Urdu = int(input(' Please Enter Obtain marks for Urdu '))
obt_marks_Social_science = int(input(' Please Enter Obtain marks for Social_science '))
mx_marks_obt = obt_marks_Chemistry + obt_marks_English + obt_marks_maths + obt_marks_Physics + obt_marks_Social_science + obt_marks_Urdu
# #************** %age obtained
pct_math = (obt_marks_maths / mx_marks_maths) * 100
pct_English = (obt_marks_English / mx_marks_English) * 100
pct_physics = (obt_marks_Physics / mx_marks_Physics) * 100
pct_Chemistry = (obt_marks_Chemistry / mx_marks_Chemistry) * 100
pct_urdu = (obt_marks_Urdu / mx_marks_Urdu) * 100
pct_Social_science = (obt_marks_Social_science / mx_marks_Social_science) * 100
pct_overall = (mx_marks_obt / mx_marks_total) * 100


# print("************Report Card for Finals 2022***********")

print('Marks obtained for Mathematics are ' + str(obt_marks_maths) + ' Out of total alloted ' + str(mx_marks_maths) + ' with percentage achieved ' + str(pct_math) )
print('Marks obtained for English are ' + str(obt_marks_English) + ' Out of total alloted ' + str(mx_marks_English) + ' with percentage achieved ' + str(pct_English))
print('Marks obtained for Physics are ' + str(obt_marks_Physics) + ' Out of total alloted ' + str(mx_marks_Physics)+ ' with percentage achieved ' + str(pct_physics))
print('Marks obtained for Chemistry are ' + str(obt_marks_Chemistry) + ' Out of total alloted ' + str(mx_marks_Chemistry) + ' with percentage achieved ' + str(pct_Chemistry))
print('Marks obtained for Urdu are ' + str(obt_marks_Urdu) + ' Out of total alloted ' + str(mx_marks_Urdu) + ' with percentage achieved ' + str(pct_urdu))
print('Marks obtained for Social_Science are ' + str(obt_marks_Social_science) + ' Out of total alloted ' + str(mx_marks_Social_science) + ' with percentage achieved ' + str(pct_Social_science))

print('Overall Marks obtained are ' + str(mx_marks_obt) + ' Out of total alloted ' + str(mx_marks_total) + ' with percentage achieved' + str(pct_overall))

# # #*************** Define Rating
if pct_overall > 70 :
    print('Congratulaions !!!!!!!!!! You have cleared the exam')
else :
        print('Please try Next Year')
