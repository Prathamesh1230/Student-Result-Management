from student import *
from utils import *

def menu():
    while True:
        print("\n📘 Student Result Management")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            roll = int(input("Roll No: "))
            name = input("Name: ")
            s1 = int(input("Subject 1 Marks: "))
            s2 = int(input("Subject 2 Marks: "))
            s3 = int(input("Subject 3 Marks: "))
            add_student(roll, name, s1, s2, s3)
            print("✅ Student added successfully.")

        elif choice == '2':
            students = view_students()
            for s in students:
                total = calculate_total(s[2], s[3], s[4])
                percent = calculate_percentage(s[2], s[3], s[4])
                print(f"Roll: {s[0]}, Name: {s[1]}, Total: {total}, Percentage: {percent}%")

        elif choice == '3':
            roll = int(input("Enter Roll No to search: "))
            s = search_student(roll)
            if s:
                total = calculate_total(s[2], s[3], s[4])
                percent = calculate_percentage(s[2], s[3], s[4])
                print(f"Roll: {s[0]}, Name: {s[1]}, Total: {total}, Percentage: {percent}%")
            else:
                print("❌ Student not found.")

        elif choice == '4':
            roll = int(input("Enter Roll No to update: "))
            name = input("New Name: ")
            s1 = int(input("New Subject 1 Marks: "))
            s2 = int(input("New Subject 2 Marks: "))
            s3 = int(input("New Subject 3 Marks: "))
            update_student(roll, name, s1, s2, s3)
            print("✅ Record updated.")

        elif choice == '5':
            roll = int(input("Enter Roll No to delete: "))
            delete_student(roll)
            print("🗑️ Record deleted.")

        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice.")
