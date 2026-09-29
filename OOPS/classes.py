class student:
    institute_name="Linkcode"
#without object creation
print(student.institute_name)
#with object creation
s = student()
#prints memory address
print(s)   
print(s.institute_name)
#can create numerous objects
s1= student()
print(s1.institute_name)



