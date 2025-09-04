from function import collage
objcollage = collage()
cdata = objcollage.read()
teacherdata = objcollage.t_data_read()
sets = set()
for i in cdata:
    sets.add(i["department"])
dep = set()
for i in cdata:
    dep.add(i["department"])
print("    WELCOME")
print("===============")
again =True
while again: #only For login
    user = input("Admin or Teacher : ").lower()
    password = input("Enter the password : ").lower()

    if (user == "admin" and password == "admin") or (user == "teacher" and password == "teacher"):
        print(f"Login successful as {user.capitalize()} ")

        if user == "admin":#only for admin
            while True:
                adminchoice = objcollage.admin()  

                if adminchoice == 1:
                    objcollage.view_all_student_data()

                elif adminchoice == 2:
                    print("=================================================")
                    for j in list(sets):
                        print(j)
                    print("=================================================")
                    department = input("Enter the department you are looking for from the above options without space in between: ")
                    objcollage.department_wise(department.lower())

                elif adminchoice == 3:
                    department = input("Enter the department of the student without space in between: ")
                    rollno = input("Enter the rollno of the student: ")
                    objcollage.individual_view(department.lower(), rollno)

                elif adminchoice == 4:
                    objcollage.department_report(dep)

                elif adminchoice == 5:
                    tid = input("Enter the teacher id : ")
                    in_name = input("Enter the name of the teacher : ") 
                    in_age = int(input("Enter the age : "))
                    in_phn_number = int(input("Enter the phone number : "))
                    objcollage.add_teacher(tid, in_name, in_age, in_phn_number)

                elif adminchoice == 6:
                    with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/Teachers_details.txt", "r") as r_file:
                        print(r_file.read())
                    r_id = input("Enter the teacher id to be removed : ")
                    objcollage.remove_id(r_id,teacherdata)
                elif adminchoice == 7:
                    objcollage.view_teacher()
                elif adminchoice == 8:
                    print("\nYou Exited Admin Menu")
                    break 
                else:
                    print("You Entered the wrong number")
            break 
#=================================================================================================================================================
        elif user == "teacher":
            while True:   #only for teacher
                teacherchoice = objcollage.teacher_choice()
                if teacherchoice == 1:
                    print("=================================================")
                    for j in list(sets):
                        print(j)
                    print("=================================================")
                    t_class = input("Enter your class :")
                    objcollage.teacher_view(t_class)
                elif teacherchoice == 2:
                    department = input("Enter the department of the student without space in between :")
                    rollno = input("Enter the roll No of the student :")
                    objcollage.teacher_individual_view(department.lower(),rollno)
                elif teacherchoice == 3:
                    department = input("Enter the department of the student without space in between: ")
                    rollno = input("Enter the rollno of the student: ")
                    objcollage.teacher_update_mark(department.lower(),rollno)
                elif teacherchoice ==4:
                    avgmark = int(input("Enter the average mark :"))
                    objcollage.teacher_view_above_avg(avgmark)
                elif teacherchoice == 5:
                    t_name = input("Enter the name:")
                    t_department = input("Enter the department without space in between: ")
                    t_roll_no = input("Enter the roll no: ")
                    t_maths = input("Enter the mark of maths: ")
                    t_physics = input("Enter the mark of physics: ")
                    t_programming = input("Enter the mark of programming: ")
                    objcollage.add_student(t_name,t_department,t_roll_no,t_maths,t_physics,t_programming)
                elif teacherchoice == 6:
                    r_department = input("Enter the department of the student without space in between :").lower()
                    r_rollno= input("Enter the roll no of the student :")
                    objcollage.teacher_student_removal(r_department,r_rollno)
                elif teacherchoice == 7:
                    print("=================================================")
                    for j in list(sets):
                        print(j)
                    print("=================================================")
                    g_department = input("Enter the department name without space in between :").lower()
                    objcollage.teacher_view_grade(g_department)
                elif teacherchoice == 8:
                    print("Exited!!")
                    break
                else:
                    print("You Entered the wrong number")
            break
 
    else:  
        print("Wrong username or password!")
        choice = input("Do you want to try again? (y/n): ").lower()
        if choice != "y":
            again = False
            print("Login Exited")
            print("\n_______________ THANK YOU !! _______________")
    




