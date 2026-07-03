name=input("Entere your name")
marks=int(input("Enter your marks"))
if marks>=90:
 print("a grade")
elif marks<=50:
    print("pass") 
else:
    print(fail)

#report generation
print("="*20)
print("GRADE REPORT")
print("="*20)
print("Name:", name)
print("Marks:", marks)
print("=" * 20)

