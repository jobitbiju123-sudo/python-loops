num_students=int(input("Enter the number of students"))
for i in range(num_students):
 name=input("Enter the name ")
 marks=int(input("marks"))
 #grading system
 if marks>=90:
     Grade="A"
 elif marks>=80:
     Grade="B"
 elif marks>=70:
     Grade="C"
 elif marks>=60: 
     Grade="D"
 elif marks>=50:
     Grade="p"
 else:
     Grade="fail"
     #report generation
 print("="*20)
 print("GRADE REPORT")
 print("="*20)
 print(name)
 print(marks)
 print("="*20)
 