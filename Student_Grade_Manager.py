import json
import os

marks = {}
subjects = []

Data_file = "students.json"

def load_data():
    global marks, subjects
    if os.path.exists(Data_file):
        with open(Data_file, "r") as f:
            data = json.load(f)
            marks = data.get("marks" , {})
            subjects = data.get("subjects", [])
    else:
        marks = {}
        subjects = []

def save_data():
    with open(Data_file, "w") as f:
        json.dump({"marks": marks, "subjects": subjects} , f, indent=1)

def setup_subjects():
    if not subjects:
        subject_count = int(input("Enter number of subjects : "))
        for i in range(subject_count):
            subjects.append(input(f"Enter name of subject {i+1} : "))
        save_data()    

def add_student():
    roll = input("Enter roll number : ")
    if str(roll) in marks:
        print("Student already exists.")
    else:
        marks[str(roll)] = {}
        for subject in subjects:
            marks[str(roll)][subject] = int(input(f"Enter marks for {subject} : "))
        save_data()    
        print("Student added successfully!\n")

def del_student():
    roll = input("Enter roll number to delete : ")
    if roll in marks:
        del marks[roll]
        save_data()
        print("Student deleted successfully!\n")
    else:
        print("Student Not Found!\n")

def update_student():
    roll = input("Enter roll number to update : ")
    if roll not in marks:
        print("Student Not Found!")
    else:
        print("Current marks :" , marks[roll])
        for subject in subjects:
            new_marks = input(f"Enter new marks for {subject} (press Enter to skip) : ")
            if new_marks.strip() != "":
                marks[roll][subject] = int(new_marks)
        save_data()        
        print("Marks Updated Successfully!\n")

def view_student():
    if not marks:
        print(" No Student Available!\n")
        return
    print("----STUDENT RECORDS----")
    for roll, sub_marks in marks.items():
        print(f"Roll number : {roll}")
        total = sum(sub_marks.values())
        avg = total / len(subjects)
        for subject, mark in sub_marks.items():
            print(f"   {subject} : " , mark)
        print(f"   Total: {total}, Average: {avg:.2f}\n")

def reset_subjects():
    global subjects
    subject_count = int(input("Enter new number of subjects : "))
    subjects = []
    for i in range(subject_count):
        subjects.append(input(f"Enter name of subject {i+1} : "))
    save_data()
    print("Subjects reset successfully!\n")            

load_data()
setup_subjects()

while True:
    print("----- Student Grade Manager -----")
    print("1. Add Student")
    print("2. Delete Student Marks")
    print("3. Update Student")
    print("4. View All Students")
    print("5. Reset Subjects")
    print("6. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        add_student()
    elif choice == 2:
        del_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        view_student()
    elif choice == 5:
        reset_subjects()            
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")                    
