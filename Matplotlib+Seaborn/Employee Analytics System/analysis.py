#Employee Analytics System
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#Data loading
def Read_CSV():
    return pd.read_csv("employees.csv")

#inspect data
def inspect_data(updated):
    print(updated.head())
    print(updated.tail())
    print(updated.info())
    print(updated.describe())
    print(updated.shape)
    print(updated.columns)
    print(updated.dtypes)

#Data cleaning
def clean_data(updated):
      #for checking value_counts
      print(updated.duplicated().sum())
      #its optional because in our dataset there are no duplicates
      print(updated.drop_duplicates())
      #for checking null values
      print(updated.isnull().sum())
      #department is missing
      updated["Department"]= updated["Department"].fillna("Unknown")
      updated["Name"]=updated["Name"].str.title()
      updated["Name"]=updated["Name"].str.strip()
      print(updated)
      return updated
      #data types are already fix
      #no need to rename columns 
      
#Basic Analysis
def basic_analysis(updated):
    print("Average salary",updated["Salary"].mean())
    print("Highest salary",updated["Salary"].max())      
    print("Lowest salary",updated["Salary"].min())      
    print("Median salary",updated["Salary"].median()) 
    print("No of Employees",updated["Name"].count())      
    print("Unique departments",updated["Department"].unique())  
    city=updated.groupby("City")
    print("Employees per city")
    print(city["Name"].count())   
         
#Department Analysis
#Groupby
def Dept_Analysis(updated):
    dept=updated.groupby("Department")
    print("Employee count of each department:")
    print(dept["Name"].count())
    print("Average salary of each deapartment") 
    print(dept['Salary'].mean())
    print("Highest salary of each deapartment") 
    print(dept['Salary'].max())
    print("Lowest salary of each deapartment")    
    print(dept['Salary'].min())  
    print("Average experince(Department-wise)")
    print(dept["Experience"].mean())
    print("Highest paid employee in each department:")
    max_salary=dept["Salary"].idxmax()
    print(updated.loc[max_salary])
     
#Advanced Pandas
def advanced_pandas(updated):
     query_operations(updated)
     map_operations(updated)
     updated["Bonus"]=updated["Salary"].apply(bonus_func)
     updated["Experience Level"]=updated["Experience"].apply(Experience_func)
     ranking_report=Rank(updated)
     sorting_report=Sort_values(updated)
     pivot_report= Pivot_table(updated)
     reports={
         "ranking_report":ranking_report,
         "sorting_report":sorting_report,
         "pivot_report":pivot_report
     }
     return reports
def query_operations(updated):
        print(updated.query('Salary>60000')) 
        print(updated.query('Department=="IT"'))      
        print(updated.query('Salary>55000 & Experience>3')) 
        print(updated.query('Department=="HR" & City=="Karachi"'))
        print(updated.query('Performance=="Excellent"'))
        
def   map_operations(updated):
    updated["Performance Score"]=updated["Performance"].map({
        "Excellent":5,
        "Good":4,
        "Average":3,
        "Poor":2
    })
    updated["Department Code"]=updated["Department"].map({
        "IT":101,
        "HR":102,
        "Finance":103,
        "Marketing":104,
        "Sales":105,
         "Unknown" :0       
    })    
def bonus_func(salary):
     if salary>=65000 :
         return salary*1.20
     elif salary>=50000 and  salary<65000:
         return salary*1.10
     else:
         return salary*1.05
def Experience_func(experience):                
    if (experience <=2):
        return ("Junior")
    elif experience<=5:
        return ("Mid")
    else:
       return ("Senior") 
def Rank(updated):
       updated["Salary Rank"]=updated["Salary"].rank(ascending=False)
       dept=updated.groupby("Department")
       updated["Department_Ranking"]=dept["Salary"].rank(ascending=False)
       ranking_report={
           "salary_ranking":updated["Salary Rank"],
           "dept_ranking":updated["Department_Ranking"]
       }
       return ranking_report
def Sort_values(updated):
      highest_salary= updated.sort_values("Salary",ascending=False)
      print(highest_salary)
      highest_experience=updated.sort_values("Experience",ascending=False)
      print(highest_experience)
      dept_salary=updated.sort_values(
          by=["Department","Salary"],
          ascending=[True,False]
      )
      print(dept_salary)
      sorting_report={
          "highest_salary":highest_salary,
          "highest_experience":highest_experience,
          "dept_salary":dept_salary
      }
      return sorting_report
       
def Pivot_table(updated):
    average_salary= updated.pivot_table(
        index="Department",
        values="Salary",
        aggfunc="mean"
    )
    print(average_salary)
    dept_city_salary=updated.pivot_table(
        index="Department",
        values="Salary",
        aggfunc="mean",
        columns="City"
    )
    print(dept_city_salary)
    employee_count=updated.pivot_table(
        index="Department",
        values="Employee_ID",
        aggfunc="count",
    )
    print(employee_count)
    max_salary=updated.pivot_table(
        index="Department",
        values="Salary",
        aggfunc="max",
    )
    print(max_salary)
    pivot_report={
        "dept_city_salary":dept_city_salary,
        "employee_count":employee_count,
        "max_salary":max_salary
    }
    return pivot_report

#Visualization
def Visualization(updated):
     salary_distribution(updated)
     department_employee_count(updated)
     dept_Average_Salary(updated)
     dept_salary(updated)
     experience_vs_salary(updated)
     performance_distribution(updated)
     correlation_analysis(updated)
     department_city_analysis(updated)
     dashboard(updated)  
       
def salary_distribution(updated):
    plt.figure(figsize=(8,5))
    plt.grid()
    sns.histplot(data=updated,x="Salary",alpha=0.3, stat="density")
    sns.kdeplot(data=updated,x="Salary",fill=True) 
    plt.title("Salary Distribution")
    plt.savefig("graphs\\Salary Distribution.png")
    plt.tight_layout()
    plt.close()
def department_employee_count(updated):  
    Employee_Count=updated.groupby("Department")["Name"].count().reset_index(name="Employee count")
    plt.figure(figsize=(8,5)) 
    bar= sns.barplot(data=Employee_Count,x="Department",y="Employee count",hue="Department",legend=True)
    for container in  bar.containers:
        bar.bar_label(container) 
    plt.title("Employee Count")
    plt.savefig("graphs\\Department Count.png")
    plt.tight_layout()  
    plt.close()  
def dept_Average_Salary(updated):
        dept_Salary=updated.groupby("Department")["Salary"].mean().reset_index(name="Average Salary")
        plt.figure(figsize=(8,5)) 
        sns.barplot(data=dept_Salary,x="Department",y="Average Salary",hue="Department",legend=True)
        highest_salary=dept_Salary["Average Salary"].idxmax()
        plt.text(dept_Salary.loc[highest_salary,"Department"],dept_Salary.loc[highest_salary,"Average Salary"],"Highest avg salary")
        plt.title("Average Salary")
        plt.savefig("graphs\\Department Average Salary.png")
        plt.close()  
def  dept_salary(updated):
      plt.figure(figsize=(8,5))
      sns.boxplot(data=updated,x="Department",y="Salary",hue="Department",legend=True)
    
      plt.title("Department salary")
      plt.savefig("graphs\\Department Salary.png")
      plt.tight_layout()
      plt.close()    
def  experience_vs_salary(updated):
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=updated,x="Experience",y="Salary",hue="Performance")
    plt.title("Experinece vs Salary")
    plt.savefig("graphs\\Experience vs Salary .png")
    plt.tight_layout()
    plt.close() 
def performance_distribution(updated):
    plt.figure(figsize=(8,5))
    sns.countplot(data=updated,x="Performance",hue="Performance",legend=True)
    plt.title("Performance distribution")
    plt.savefig("graphs\\Performance distribution.png")
    plt.tight_layout()
    plt.close() 
def correlation_analysis(updated):
    plt.figure(figsize=(15,10))
    corr_matrix=updated.corr(numeric_only=True)
    sns.heatmap(corr_matrix,annot=True) 
    plt.title("Correlation Analysis")
    plt.savefig("graphs\\Correlation Analysis.png")
    plt.tight_layout() 
    plt.close()  
def department_city_analysis(updated):  
    Highest_salary=updated.pivot_table(
        index="Department",
        columns="City",
        values="Salary",
        aggfunc="mean"
        
    )  
    Highest_employee_count=updated.pivot_table(
        index="Department",
        columns="City",
        values="Employee_ID",
        aggfunc="count"
    )
    fig,ax=plt.subplots(1,2,figsize=(15,8))
    sns.heatmap(Highest_salary,annot=True,ax=ax[0])
    ax[0].set_title  ("Highest Salary (dept x city)")
    sns.heatmap(Highest_employee_count,annot=True,ax=ax[1],cmap="viridis")
    ax[1].set_title("Highest Employeee Count(dept x city)")
    plt.savefig("graphs\\salary & employee count.png")
    plt.tight_layout() 
    plt.close()  
    
def dashboard(updated):  
    fig,ax=plt.subplots(nrows=2,ncols=2,figsize=(16,10))  
    sns.histplot(data=updated,x="Salary", stat="density",ax=ax[0,0],color="skyblue")
    sns.kdeplot(data=updated,x="Salary",fill=True,ax=ax[0,0]) 
    ax[0,0].set_title("Salary Distribution")
    Employee_Count=updated.groupby("Department")["Name"].count().reset_index(name="Employee count")
    bar= sns.barplot(data=Employee_Count,x="Department",y="Employee count",hue="Department",legend=True,ax=ax[0,1],palette="Set2")
    for container in  bar.containers:
        bar.bar_label(container) 
    ax[0,1].set_title("Employee Count")
    s=sns.scatterplot(data=updated,x="Experience",y="Salary",hue="Performance",ax=ax[1,0],palette="viridis")
    highest_experience=updated["Experience"].idxmax()
    s.text(updated.loc[highest_experience,"Experience"],updated.loc[highest_experience,"Salary"],"Highest Experience")
    ax[1,0].set_title("Experinece vs Salary")
    corr_matrix=updated.corr(numeric_only=True)
    sns.heatmap(corr_matrix,annot=True,ax=ax[1,1],cmap="coolwarm") 
    ax[1,1].set_title("Correlation Analysis")
    fig.suptitle( "Employee Analytics Dashboard",
    fontsize=12,             
    fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig("graphs\\dashboard.png",dpi=300)
    plt.close()
    
#Export    
def Export(updated,original,reports) :
    with pd.ExcelWriter("Employee_Report.xlsx") as writer:
        original.to_excel(writer,sheet_name="Original information",index=False)  
        updated.to_excel(writer,sheet_name="Updated information",index=False)  
        reports[ "ranking_report"]["dept_ranking"].to_excel(writer,sheet_name="dept_Ranking",index=False)
        reports[ "ranking_report"]["salary_ranking"].to_excel(writer,sheet_name="salary_Ranking",index=False)
        reports["sorting_report"]["highest_salary"].to_excel(writer,sheet_name="Highest salary",index=False)
        reports["sorting_report"][ "highest_experience"].to_excel(writer,sheet_name="Highest Experience",index=False)
        reports["pivot_report"]["dept_city_salary"].to_excel(writer,sheet_name="DepartmentxCity salary")
        reports["pivot_report"][ "employee_count"].to_excel(writer,sheet_name="dept wise no of employees")
        reports["pivot_report"][ "max_salary"].to_excel(writer,sheet_name="dept wise max salary")
        
        
        
        
        
        
        
def main():
    original=Read_CSV()
    updated=original.copy()
    inspect_data(updated) 
    updated=clean_data(updated) 
    basic_analysis(updated)
    Dept_Analysis(updated)
    reports=advanced_pandas(updated)
    Visualization(updated)
    Export(updated,original,reports)
   
    
main()      
    

    


