import os
import json

filename = "students.json"

# --- 1. LOAD DATA USING OS ---
# Check if file exists before trying to read it
if os.path.exists(filename):
    with open(filename, "r") as f:
        students = json.load(f)
else:
    students = []

# --- 2. MAIN LOOP ---
while True:
    print("\n--- MENU ---")
    print("[1] Add  [2] List  [3] Search  [4] Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        
        while True:
            age = input("Age: ")
            if age.isdigit() and int(age) > 0:
                break 
            print("Invalid age! Please enter a number greater than 0.")
            
        course = input("Course: ")
        
        student = {
            "name": name,
            "age":  age,
            "course": course
        }
        students.append(student)
        
        with open(filename, "w") as f:
            json.dump(students, f, indent=2)
        print("Saved!")

    elif choice == "2":
        print("\n--- Student Records ---")
        print("_______________________________________") 
        for s in students:
            print(f"{s['name']}  Age: {s['age']}  Course: {s['course']}")
        print("_______________________________________")

    elif choice == "3":
        query = input("Search Name: ").lower()
        found = False
        for s in students:
            if query in s['name'].lower():
                print("_______________________________________")
                print(f"Found!\nName {s['name']} \nAge: {s['age']} \nCourse: {s['course']}")
                print("_______________________________________")
                found = True
                
        if not found:
            print("No student found.")

    elif choice == "4":
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice! (1-4 only)")