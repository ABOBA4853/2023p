from students import Student
#1
'''
students = Student("Dima", 11, "S2019")
print("Call atributtes:")
print(f"Name: {student.Name}\n"
      f"Age: {student.Age}\n"
      f"Groupe: {student.Group}")
print("Call method ShowStudentInfo:")
student.ShowStudentInfo()
'''
dimaS = Student ("Dima", 11, "S2019")
antonS = Student ("Anton", 13, "S2019")
pipaS = Student ("Pipa", 15, "S2019")
bibaF = Student ("Biba", 12, "S2019")
timaL = Student ("Tima", 11, "S2019")
students = list()
students.append(dimaS)
students.append(antonS)
students.append(pipaS)
students.append(bibaF)
students.append(timaL)
for student in students:
        student.ShowStudentInfo()
