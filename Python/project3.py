
class Student:
    def __init__(self,StudentID,name,age,marks):
        self.StudentID=StudentID
        self.name=name
        self.age=age
        self.marks=marks


students=[]    
 
def Add_Student():
    print("=================")
    studentID=input("Enter StudentID:")
    
    name=input("Enter Student name:")
    age=input("Enter age of Student:")
    marks=input("Enter marks of Student:")
    is_found = False
    for stu in students:
        if stu.StudentID==studentID:
            is_found = True
            break
    
    if is_found:
        print('Student exists already. Try again')
        Add_Student()
    else:
        student=Student(studentID,name,age,marks)
        students.append(student)
        print("Student added!")
        print("==================")
        
             
   
def View_Student():
    if students ==[]:
        print("NO students found")
    else:    
      for stu in students:
          print("=================")
          print("Student name is:",stu.name)
          print("Student id is:",stu.StudentID)
          print("Student age is:",stu.age)
          print("Student marks are:",stu.marks)
          print("=================")
          
         

def Search_Student(ID):
       for stu in students:
           if stu.StudentID==ID:
                print("Student name is:",stu.name)
                print("Student id is:",stu.StudentID)
                print("Student age is:",stu.age)
                print("Student marks are:",stu.marks)
                print("\n")
                break
       else:
           print("No student with such ID exists")
           
def Update_Student(ID):
    for stu in students:
        if stu.StudentID == ID:

            while True:
                studentID = input("Enter new Student ID: ")

                duplicate = False

                for other_stu in students:
                    if other_stu != stu and other_stu.StudentID == studentID:
                        duplicate = True
                        print("This Student ID already exists. Try again.")
                        break

                if not duplicate:
                    break

            stu.StudentID = studentID

            name = input("Enter Student name: ")
            stu.name = name

            age = input("Enter age of Student: ")
            stu.age = age

            marks = input("Enter marks of Student: ")
            stu.marks = marks

            print("Student updated successfully")
            return

    print("No student with such ID exists")
    
def Delete_Student(ID):
    for stu in students:
        if stu.StudentID==ID:
            students.remove(stu)
            print("Student deleted successfully")
            break
    else:
           print("No student with such ID exists")      
                                      
                    
    
                        
while True: 
  userChoice=input("""====Student Management System===
Select 1/2/3/4/5/6 for
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your Choice:
""")    
  if userChoice=="1":
      Add_Student()
  elif userChoice=="2":
      View_Student()
  elif userChoice=="3":
      ID=input("Enter Student id you want to search:")
      Search_Student(ID)    
  elif userChoice=="4":
      ID=input("Enter Student id you want to update the student:")
      Update_Student(ID)     
  elif userChoice=="5":
      ID=input("Enter Student id ,you want to delete the student:")
      Delete_Student(ID)    
  elif userChoice=="6":
      print("You exit from the managemnet program")
      break      
  else :
      print("No such options exist!===ERROR===")
      break    
       
    
        
        