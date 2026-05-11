"""
Student Marks Calculator
Author: [Your Name]
Description: A professional Python script to calculate grades based on user input.
"""

def calculate_grade(average):
    """
    Determines the letter grade based on the average percentage.
    Using a standard university grading scale.
    """
    if average >= 80:
        return "A (Distinction)"
    elif average >= 70:
        return "B (Credit)"
    elif average >= 60:
        return "C (Pass)"
    elif average >= 50:
        return "D (Narrow Pass)"
    else:
        return "F (Fail)"

def main():
    """
    Main execution function to handle user input and display results.
    """
    print("-" * 30)
    print(" STUDENT MARKS CALCULATOR ")
    print("-" * 30)

    try:
        # Basic student information
        student_name = input("Enter student name: ")
        num_subjects = int(input("Enter the number of subjects: "))
        
        marks = {}

        # Loop to collect marks for each subject
        for i in range(1, num_subjects + 1):
            subject_name = input(f"Enter name for subject {i}: ")
            score = float(input(f"Enter marks for {subject_name} (out of 100): "))
            
            # Simple validation to ensure marks are within 0-100
            if 0 <= score <= 100:
                marks[subject_name] = score
            else:
                print("Invalid input! Marks should be between 0 and 100.")
                return

        # Perform calculations
        total_marks = sum(marks.values())
        average_percentage = total_marks / num_subjects
        final_grade = calculate_grade(average_percentage)

        # Display the Final Report
        print("\n" + "="*30)
        print(f" OFFICIAL REPORT: {student_name.upper()} ")
        print("="*30)
        
        for subject, score in marks.items():
            print(f"{subject:15}: {score}")

        print("-" * 30)
        print(f"TOTAL MARKS:    {total_marks} / {num_subjects * 100}")
        print(f"AVERAGE:        {average_percentage:.2f}%")
        print(f"FINAL GRADE:    {final_grade}")
        print("="*30)

    except ValueError:
        print("Error: Please enter numerical values for marks and number of subjects.")

if __name__ == "__main__":
    main()
