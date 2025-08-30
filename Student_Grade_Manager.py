marks = {}

subject_count = int(input("Enter number of subjects : "))
subjects = []

for subject in range(subject_count):
    subjects.append(input(f"Enter name of subject {subject+1} : "))
   
def add_student():
    roll = int(input("Enter roll number : "))
    if roll in marks:
        print("Student already exists.")
    else:
        marks[roll] = {}
        for subject in subjects:
            marks[roll][subject] = int(input(f"Enter marks for {subject} : "))
        print("Student added successfully!\n")

def del_student():
    roll = int(input("Enter roll number to delete : "))
    if roll in marks:
        del marks[roll]
        print("Student deleted successfully!\n")
    else:
        print("Student Not Found!\n")

def update_student():
    roll = int(input("Enter roll number to update : "))
    if roll not in marks:
        print("Student Not Found!")
    else:
        print("Current marks :" , marks[roll])
        for subject in subjects:
            new_marks = input(f"Enter new marks for {subject} (press Enter to skip) : ")
            if new_marks.strip() != "":
                marks[roll][subject] = int(new_marks)
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


while True:
    print("----- Student Grade Manager -----")
    print("1. Add Student")
    print("2. Delete Student Marks")
    print("3. Update Student")
    print("4. View All Students")
    print("5. Exit")

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
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")                    