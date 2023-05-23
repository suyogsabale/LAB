def add_emp(emps):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    skills = {}
    total_score=0
    num_skills = int(input("Enter the number of skills: "))
    for i in range(num_skills):
        skill_name = input(f"Enter skill #{i + 1} name: ")
        skill_rating = int(input(f"Enter skill #{i + 1} rating (0-100): "))
        skills[skill_name] = skill_rating
        total_score +=skill_rating
    score=total_score/num_skills
    if score >=90:
        grade="A"
    elif score >=80:
        grade="B"
    elif score >=70:
        grade="C"
    elif score >=60:
        grade="D"
    else:
        grade="F"
    emps.append({"Emp_id":emp_id,"Name":name,"Skills":skills,"Score":score,"Grade":grade})
    print("emp added successfully!")

def view_emps(emps):
        if not emps:
            print("No employees available.")
            return
        else:
            print("Employee Performance:")
            for emp in emps:
                print("Employee ID:",emp["Emp_id"])
                print("Name:",emp["Name"])
                print("Skills: ",emp["Skills"])
                print("Performance Score:",emp["Score"])
                print("Grade:",emp["Grade"])
                print("-------------------------")
def main():
    emps=[]
    while True:
        print("\n--- Employee Performance Evaluation System ---")
        print("1. Add an employee")
        print("2. Evaluate employee performance and display")
        print("3. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_emp(emps)
        elif choice == "2":
            view_emps(emps)
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()