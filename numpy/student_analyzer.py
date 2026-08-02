import numpy as np
#Student Performance Analyzer
student_data=np.array([
                       #ID,Math,Phy,Chem matks out of 100 for each subject
                       [101 ,78,85,90],
                       [102 ,45,55,60],
                       [103 ,88 ,91,84],
                       [104 ,35,40,50],
                       [105 ,95,99,98],
                       [106 ,67,72,70],
                       [107 ,81,76,88],
                       [108 ,52,48,60],
                       [109 ,90,94,93],
                       [110 ,39,45,41]])
original_data=student_data.copy()

def View_Students():
       students= student_data[:,0:]
       print("Students data :",students)
       
       
def Subject_Average():
      math_average= np.mean(student_data[:,1],axis=0)
      print("Average of math is:",math_average)
      phy_average=np.mean(student_data[:,2],axis=0)
      print("Average of phy is:",phy_average)
      chem_average=np.mean(student_data[:,3],axis=0)  
      print("Average of chem is:",chem_average)
      
      
def Total_Marks():      
       total_marks=np.sum(student_data[:, 1:],axis=1)
       id=101
       for marks in total_marks:
          print(f"Student {id} total marks are:",marks)
          id+=1
          
          
def Average_Marks():
       average_marks=np.mean(student_data[:,1:],axis=1)
       id=101
       for marks in average_marks:
          print(f"Student {id} average is:",marks)
          id+=1
          
          
def Topper():
        total_marks=np.sum(student_data[:, 1:],axis=1)
        topper_marks=np.max(total_marks)
        topper=np.argmax(total_marks)
        print("Topper is:",student_data[topper],"with total marks",topper_marks )
        
        
def LowestScorer():
        total_marks=np.sum(student_data[:, 1:],axis=1)
        lowest_marks=np.min(total_marks)
        lowestScorer=np.argmin(total_marks)
        print("Lowest Scorer is:",student_data[lowestScorer],"with total marks :",lowest_marks)  
       
       
def Morethan80():
        math_marks=student_data[student_data[:,1]>80] 
        print("Students who have marks above 80 in maths",math_marks)
        
        
def Failed_Students():
    minimum_marks = 150
    failed = student_data[np.sum(student_data[:, 1:], axis=1) < minimum_marks]
    total_marks=np.sum(failed[:,1:],axis=1)
    if len(failed) == 0:
        print("No failed students")
    else:
         for i in  range(len(failed)):
          print("Failed student IDs:",failed[i,0])
          print("Total marks",total_marks[i])
           
           
def Grace_marks():
         grace_marks=5
         user_input=input("""In which subject u want to add grace marks
        (c for chem,p for physics,m for maths)""").lower()
         if user_input=="c":
             student_data[:,3]=student_data[:,3]+grace_marks
             print("grace marks successfully added in chemistry")
         elif user_input=="p":
             student_data[:,2]=student_data[:,2]+grace_marks
             print("grace marks successfully added in phy")
         elif user_input=="m":
             student_data[:,1]=student_data[:,1]+grace_marks
             print("grace marks successfully added in math")   
         else:
            print("Invalid choice!")
            
                
def Save_report():
    
    save=np.save('Student_Report.npy',student_data)
    print("report successfully saved")
    
    
def Load_Report():
    try:
      load=np.load('Student_Report.npy')
      print("Loaded successfully",load)
    except FileNotFoundError:
        print("No such file exists")
        
        
def Reset_dataset():
     global student_data
     student_data=original_data.copy()
     print("Reset successfully")
     students= student_data[:,0:] 
     print("Students data :",students)
     
     
def Exit():
            print("You terminated from the program")
                
while True:
   user_choice=int(input("""===== STUDENT PERFORMANCE ANALYZER =====
1.View All Students
2.Subject Averages
3.Student Total Marks
4.Student Average Marks
5.Find Topper
6.Find Lowest Scorer
7.Find Students Above 80 in Math
8.Find Failed Students
9.Add Grace Marks
10.Save Report
11.Load Report
12.Reset dataset
13.Exit
Enter your choice:
"""
))   
   if user_choice==1:
       View_Students()    
   elif user_choice==2:
      Subject_Average()
   elif user_choice==3:
       Total_Marks()
   elif user_choice==4:
       Average_Marks() 
   elif user_choice==5:
       Topper()                 
   elif user_choice==6:
       LowestScorer()
   elif user_choice==7:
       Morethan80()  
   elif user_choice==8:
       Failed_Students()  
   elif user_choice==9:
       Grace_marks()  
   elif user_choice==10:
       Save_report()    
   elif user_choice==11:
       Load_Report()      
   elif user_choice==12:
       Reset_dataset()         
   elif user_choice==13:
       Exit()
       break
   else:
       print("Invalid choice")
       break