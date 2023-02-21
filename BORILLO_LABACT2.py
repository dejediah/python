name = 'Raphael Jedidiah R. Borillo'
cys = "Course/Year/Section: BCS12"

print(name)
print(cys)

print("===============================================LEGEND==============================================="
      "\nAttendance/Class Participation = 20%"
      "\nEnabling Assessment            = 50%"
      "\nSummative Assessment           = 30%"
      "\n---------------------------------------------------"
      "\nTotal                          = 100%"
      "\n"
      "\n"
      "\n\tAttendance (10 pts)                    Enabling                           Summative (50 pts)"
      "\n\tClass Participation (20 pts)           Short Quiz 1 (10 pts)"
      "\n                                           Short Quiz 2 (10 pts)"
      "\n                                           Short Quiz 3 (10 pts)"
      "\n                                           Long Exam    (30 pts)"
      "\n====================================================================================================")

print("\n")
attn = float(input("Attendance for this course: "))
coursePart = float(input("Participation for this course: "))
A_C = ((attn+coursePart)/30)*0.20*100
print("20% of Attendance/Class Participation: " + (str(A_C)))

SQ1 = float(input("Short Quiz 1:"))
SQ2 = float(input("Short Quiz 2:"))
SQ3 = float(input("Short Quiz 3:"))
LongE = float(input("Long Exam: "))
EA = ((SQ1+SQ2+SQ3+LongE)/60)*0.50*100
print("50% of Enabling Assessment: " + (str(EA)))

summa = float(input("Summative Exam: "))
SA = (summa/50)*0.30*100
print("30% of Summative Exam: " + (str(EA)))

FG = A_C + EA + SA
print("Hello, " + name + "! Your final grade is " + (str(FG)))
if FG>=60:
    print("Congratulations! You passed!")
else:
    print("Sorry, you failed.")
