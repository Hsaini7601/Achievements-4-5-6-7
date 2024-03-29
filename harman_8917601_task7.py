def main():
    
    # Welcome message and user information input
    print("Welcome to the Course Registration System!")
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    student_number = input("Enter your student number: ").strip()

    # Courses with codes
    courses = {
        "PROG1783": "Introduction to Programming",
        "INFO8025": "Network Infrastructure",
        "PROG2267": "IT Web Foundation",
        "MATH3012": "Computer Ops and troubleshooting"
    }

    # show available courses
    print("\nAvailable Courses:")
    for code, name in courses.items():
        print(f"{code}: {name}")

    # User input for course registration
    course_codes_input = input("\nPut the desired course codes here (separated by commas): ").strip()
    selected_courses = course_codes_input.split(",")

    #  student information and choosen courses
    print("\nStudent Information:")
    print(f"Name: {first_name} {last_name}")
    print(f"Student Number: {student_number}")

    print("\nRegistered Courses:")
    for code in selected_courses:
        if code.strip() in courses:
            print(f"{courses[code.strip()]} ({code.strip()})")

if __name__ == "__main__":
    main()
