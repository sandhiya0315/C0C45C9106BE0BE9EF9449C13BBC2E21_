class Students:
 def init_(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
 def sort_Students(students_list):
    sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=true)
    return sorted_students
 Students=[
     Student("Hari","A123",7.8),
     Student("Srikanth","A124",8.9),
     Student("Saumya","A125",9.1),
     Student("Mahidhar","A126",9.9),
     ]
 sorted_students=sort_students(students)
 for students in sorted_students:
     print("Name:{},Roll Number:{}, CGPA:{}",format(student.name,student.roll_number,students.Cgpa))
       
