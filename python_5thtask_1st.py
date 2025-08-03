# student_marks_dictionary.py

# Step 1: Create dictionary
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}

# Step 2: Ask user for a student's name
student_name = input("Enter the student's name to get their marks: ")

# Step 3: Retrieve and display marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
