#MAKING STUDENT MANAGEMENT SYSTEM
#storing students data in dictionary
students={}
#now creating feature fucntions 
######
#ADDING STUDENTS FUNCTION
def addingstudents(students):
    n=input( " Enter students name")
    c=input( " Enter students class")
    r=input( " Enter students roll no")
    a=input( " Enter address of student")
    if r in students:
       print("Roll no already exists")
       return
    else:
     students[r]={
          "Name":n,
          "Class":c,
          "Roll No":r,
          "Address":a
     }
#CREATING VIEW STUDENTS FUNCTION
#####
def viewstudent(students):
   for keys,values in  students.items():
       print(keys,values)

#creating a function to seach students via roll no
def searchstudent(students):
      r=input("Enter roll no of student you want to search")
      if r in students:
        print(students[r])
      else:
         print(f"Roll no {r}does not exist")

#creating a function for deleting a student
def deletingstudent(students):
   r=input("Enter roll no of student ")
   if r in students:
      del students[r]
   else:
      print(f"Roll no {r }is not avaliable")
#making update students functions
#update name 
def updatename(students,r):
   if r in students:
      students[r]["name"]=input("enter new name of student")
   else:
      print(f"Roll no {r}does not exist")
 #update class
def updateclass(students,r):
   if r in students:
      students[r]["Class"]=input("Enter new class of student")
   else:
      print(f"Roll no {r}does not exist")
#update adress 
def updateadress(students,r):
   if r in students:
      students[r]["Address"]=input("Enter new adress of the student")
   else:
      print(f"Roll no {r}does not exist")
#changing roll no of student
def changerollno(students,r):
   if r in students:
      newrollno=input("Enter new roll no")
      students[newrollno]=students[r]
      students[newrollno]["Rollno"]=newrollno
      del students[r]

   else:
      print(f"roll no {r }not found")
#making menu for updation
def updationmenu(students,updatename,updateclass,updateadress,changerollno):
 while True:
   print("UPDATE MENU")
   print("1 update name")
   print("2 update class")
   print("3 update roll no")
   print("4 update address")
   print("5 exit")
   #now
   choice=input("enter choice")
   r=input("Enter roll no of student")
   if choice=="1":
      updatename(students,r)
   elif choice=="2":
      updateclass(students,r)
   elif choice=="3":
      changerollno(students,r)
   elif choice=="4":
      updateadress(students,r)
   elif choice=="5":
      break
   else: print("invalid choice")
#count student function
def countingstudents(students):
 count=0
 for keys,values in students.items():
   count=count+1
#now creating menu for students managemtent system
while True:
   print("1 Add students")
   print("2 View students")
   print("3 Search students")
   print("4 Update students")
   print("5 Delete students")
   print("6 Count students")
   print("7 Exit")
   try:
      choice=input("enter choice")
   except ValueError:
      print("Enter a number")
   if choice=="1":
      addingstudents(students)
   elif choice=="2":
      viewstudent(students)
   elif choice=="3":
      searchstudent(students)
   elif choice=="4":
      updationmenu(students)
   elif choice=="5":
      deletingstudent(students)
   elif choice=="6":
      countingstudents(students)
   elif choice=="7":
      break
   else:
      print("invalid choice")