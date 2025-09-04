class collage:
    def __init__(self):
        self.c_data = self.read()

    def read(self):
        c_data = []
        try :
            file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/data.txt","r")
            for i in file:
                if len(i.strip().split(","))>5:
                    name,department,rollno,maths,physics,programming = i.strip().split(",")
                    c_data.append({
                        "name":name,"department":department,"rollno":rollno,"maths":maths,"physics":physics,"programming":programming
                                })
            file.close()
            return c_data
        except FileNotFoundError:
            print("||The File Not Found||") 

    def admin(self):
        admin_choice = int(input("Admin Menu:\n1. View All Student Data\n2. View Department-wise\n3. View Individual-wise\n4. Department Performance Report \n5. Add New Teacher\n6. Remove Teacher\n7. View Teacher list \n8. EXIT  \nEnter your choice (1-8): "))
        return admin_choice
    
    def view_all_student_data(self):
        num = 0
        W_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/All_student_data.txt","w")
        for i in self.c_data:
            num +=1
            W_file.write(
                "SI NO : " + str(num)+
                ", Name: " + i["name"] +
                ", Department: " + i["department"] +
                ", Roll no: " + i["rollno"] +
                ", Maths: " + i["maths"] +
                ", Physics: " + i["physics"] +
                ", Programming: " + i["programming"] + "\n"
            )
        print("===========================================================================")    
        print("  The students list has been printed in the -All_studnent_data.txt- file")
        print("===========================================================================") 

    def department_wise(self,depart):
        w_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/department_details.txt","w")
        num =0
        found = False
        for i in self.c_data:
            if depart == i["department"].lower():
                  found = True
                  num+=1
                  w_file.write(
                        "SI NO : " + str(num)+
                        ", Name: " + i["name"] +
                        ", Department: " + i["department"] +
                        ", Roll no: " + i["rollno"] +
                        ", Maths: " + i["maths"] +
                        ", Physics: " + i["physics"] +
                        ", Programming: " + i["programming"] + "\n"
                )    
        if found == False:
            print("||| The Department you are looking for not found |||")
        else:
            print("===========================================================================") 
            print(f" The {depart} data has been printed in the -department_details.txt- file ")
            print("===========================================================================") 
        w_file.close()

    def individual_view(self,department,rollno):
        w_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/individual.txt","w")
        found = False
        for i in self.c_data:
            if i["department"].lower() == department and i["rollno"].lower()==rollno:
                found = True
                w_file.write(
                        " Name: " + i["name"] +
                        ", Department: " + i["department"] +
                        ", Roll no: " + i["rollno"] +
                        ", Maths: " + i["maths"] +
                        ", Physics: " + i["physics"] +
                        ", Programming: " + i["programming"] + "\n"
                )
        if found == False:
            print("||| The Student You Are Looking For Not Found |||")
        else:
            print("======================================================================================================") 
            print(f"  The data of roll no : {rollno} from the {department} has been printed in the -individual.txt- file ")
            print("======================================================================================================") 
        w_file.close()
    def department_report(self,dep):
        w_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/Department_report.txt","w")
        dept_dict = {}
        found = False
        for i in list(dep):
            dep_sum = 0
            for j in self.c_data:
                if i ==  j["department"]:
                    found = True
                    dep_sum += int(j["maths"])+int(j["physics"])+int(j["programming"])
            dept_dict[i] = dep_sum
            w_file.write(
                "Department : "+ str(i) +
                ",  Total marks of full students is : "+ str(dep_sum) + "\n"
            )
        w_file.write(
            "==================================================================================\n"
                "The Department which has the highest perfomance is : " + str(max(dept_dict))
        )
        if found == False:
            print("||| The Department You are looking for not Found |||")
        else:
            print("========================================================================") 
            print("     The data has been printed to the -Department_report.txt- file")
            print("========================================================================") 
        w_file.close
    def t_data_read(self):
            r_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/teachers.txt","r")
            teacher_data = []
            for i in r_file:
                if len(i.strip().split(","))>3:
                   t_id,name,age,phnnumber= i.strip().split(",")
                   teacher_data.append({
                    "t_id":t_id,"name":name,"age":age,"phnnumber":phnnumber
                            })    
            r_file.close()
            return teacher_data
    
    def add_teacher(self,tid,in_name,in_age,in_phn_number):
            a_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/Teachers_details.txt","a")
            a_file.write(
            f"Teacher id :{tid}, Name :{in_name}, Age : {in_age}, Ph number : {in_phn_number}\n")
            a_file.close()
            print("===========================================================================================")
            print(f"  The details of the teacher {in_name} has been added to the file -Teachers_details.txt-")
            print("===========================================================================================") 
    def remove_id(self, r_id, teacherdata):
        found = False
        # Filter out the teacher to remove
        new_data = []
        for i in teacherdata:
            if i["t_id"] == r_id:
                found = True
            else:
                new_data.append(i)

        # Write back updated list
        with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/Teachers_details.txt","w") as w_file:
            for j in new_data:
                w_file.write(
                    "Teacher id :" + j["t_id"] +
                    ", Name :" + j["name"] +
                    ", Age : " + j["age"] +
                    ", Ph number : " + j["phnnumber"] + "\n"
                )

        if not found:
            print("||| The Teacher Id does not Match |||")
        else:
            print("=============================================================================================") 
            print(f"  The teacher with the id of {r_id} has been removed from the -Teachers_details.txt- file")
            print("=============================================================================================")

    def view_teacher(self):
        try:
            with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/Teachers_details.txt", "r") as r_file:
                data = r_file.read()

            with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/admin_txt/Teacher_view.txt", "w") as f_out:
                f_out.write(data)
            print("==================================================================")
            print("         Teacher details exported to Teacher_view.txt")
            print("==================================================================")

        except FileNotFoundError:
            print("The input file was not found.")
#================================================================================================================================================================================================================= 
    def teacher_choice(self):
        teacherchoice = int(input(
            "\nTeacher Menu:\n"
            "1. View All Students in Her Class\n"
            "2. Search Student in Her Class\n"
            "3. Update Marks\n"
            "4. View Students Above a Given Average\n"
            "5. Add Student\n"
            "6. Delete Student\n"
            "7. View Students Grade-wise\n"
            "8. EXIT\n"
            "Enter your choice: "
            ))
        return teacherchoice
    def teacher_view(self,t_class):
        w_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/teacher_txt/Teacher_department_details.txt","w")
        num =0
        found = False
        for i in self.c_data:
            if t_class == i["department"].lower():
                  found = True
                  num+=1
                  w_file.write(
                        "SI NO : " + str(num)+
                        ", Name: " + i["name"] +
                        ", Department: " + i["department"] +
                        ", Roll no: " + i["rollno"] +
                        ", Maths: " + i["maths"] +
                        ", Physics: " + i["physics"] +
                        ", Programming: " + i["programming"] + "\n"
                    )  
        if found == False:
            print("||| The Department Not Found |||") 
        else:
            print("===========================================================================") 
            print(f" The {t_class} data has been printed in the -teacher_department_details.txt- file ")
            print("===========================================================================") 
        w_file.close()
    def teacher_individual_view(self,department,rollno):
        w_file = open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/teacher_txt/teacher_individual.txt","w")
        found = False
        for i in self.c_data:
            if i["department"].lower() == department and i["rollno"].lower()==rollno:
                found = True
                w_file.write(
                        " Name: " + i["name"] +
                        ", Department: " + i["department"] +
                        ", Roll no: " + i["rollno"] +
                        ", Maths: " + i["maths"] +
                        ", Physics: " + i["physics"] +
                        ", Programming: " + i["programming"] + "\n"
                )
        if found == False:
            print("||| The Student Not Found |||")
        else:
            print("==========================================================================================") 
            print(f"  The data of roll no : {rollno} from the {department} has been printed in the -teacher_individual.txt- file ")
            print("==========================================================================================") 
        w_file.close()
    def teacher_update_mark(self,u_department,roll_no):
        updated = False
        for i in self.c_data:
            if i["department"].lower() == u_department and i["rollno"].lower()==roll_no:
                print(f"Found student: {i['name']} (Roll No: {i['rollno']})")
                i["maths"] = str(input("Enter new Maths marks: "))
                i["physics"] = str(input("Enter new Physics marks: "))
                i["programming"] = str(input("Enter new Programming marks: "))
                print("================================")
                print("  Marks updated successfully!")
                print("================================")
                updated = True
                break
         
        if updated==True:
            #updated data is passed here
            with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/data.txt", "w") as w_file:
                for s in self.c_data:
                    w_file.write(f"{s['name']},{s['department']},{s['rollno']},{s['maths']},{s['physics']},{s['programming']}\n")
                    #=====================================
        else:
            print("The student not found!!")
    def teacher_view_above_avg(self,avgmark):
       with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/teacher_txt/Teacher_avg_mark.txt", "w") as w_file:
        num = 0
        for i in self.c_data:
            total =int(i["maths"])+int(i["physics"])+int(i["programming"])
            avg = total//3
            if avgmark<avg:
                num +=1
                w_file.write(
                    "SI NO : " +str(num) +
                    ", Name: " + i["name"] +
                    ", Department: " + i["department"] +
                    ", Roll no: " + i["rollno"] +
                    ", Maths: " + i["maths"] +
                    ", Physics: " + i["physics"] +
                    ", Programming: " + i["programming"] +
                    ", Average mark is :" + str(avg) +"\n"
                    
                )
        print("======================================================================")
        print("  The Students list has been added to the -teacher_avg_mark.txt- file")
        print("======================================================================")
    def add_student(self, t_name, t_department, t_roll_no, t_maths, t_physics, t_programming):
    # Write to file
        with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/data.txt", "a") as a_file:
            a_file.write(f"{t_name},{t_department},{t_roll_no},{t_maths},{t_physics},{t_programming}\n")

        # Update memory list
        self.c_data.append({
            "name": t_name,
            "department": t_department,
            "rollno": t_roll_no,
            "maths": str(t_maths),
            "physics": str(t_physics),
            "programming": str(t_programming)
        })

        print("===================================================")
        print(f" Student {t_name} ({t_roll_no}) added successfully!")
        print("===================================================")
    def teacher_student_removal(self,r_departent,r_rollno):
        found = False
        for i in self.c_data:
            if r_departent == i["department"].lower() and r_rollno == i["rollno"]:
                found = True
                print("Student Found",i)
                self.c_data.remove(i)

        with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/data.txt", "w") as w_file:
            for student in self.c_data:
                w_file.write(f"{student['name']},{student['department']},{student['rollno']},{student['maths']},{student['physics']},{student['programming']}\n")
        if found == False:
            print("||| Student Not Found |||")
        else:
            print("===================================================")
            print(f"Student with Roll No {r_rollno} from Department {r_departent} has been deleted successfully!")
            print("===================================================")
        w_file.close()
    def teacher_view_grade(self,g_department):
        with open("C:/Users/LENOVO/Documents/MINI_PRJCT_ORG/teacher_txt/Teacer_grade_view.txt", "w") as w_file:
         num = 0
         found = False
         grade = ""
         for i in self.c_data:
            if g_department == i["department"].lower():
                  found = True
                  total =int(i["maths"])+int(i["physics"])+int(i["programming"])
                  avg = total//3
                  if avg >= 90:
                    grade = "A+"
                  elif avg >= 80:
                    grade = "A"
                  elif avg >= 70:
                    grade = "B"
                  elif avg >= 60:
                    grade = "C"
                  elif avg >= 50:
                    grade = "D"
                  else:
                    grade = "F"
                  num +=1
                  w_file.write(
                    "SI NO : " + str(num)+
                    ", Name: " + i["name"] +
                    ", Department: " + i["department"] +
                    ", Roll no: " + i["rollno"] +
                    ", Maths: " + i["maths"] +
                    ", Physics: " + i["physics"] +
                    ", Programming: " + i["programming"] +
                    ", Average Mark: "+str(avg)+
                    ", Grade =  :" + grade +"\n"
                )
        if found == False:
            print("||| The Department Not Found |||")   
        else:       
            print("===================================================")
            print(f"Grade added list has been added to the -teacher_grade-view.txt- file")
            print("===================================================")
        w_file.close()