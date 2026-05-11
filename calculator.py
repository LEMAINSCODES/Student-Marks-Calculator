def calculate_grade(average):
    if average >= 80: return "A (Distinction)"
    elif average >= 70: return "B"
    elif average >= 60: return "C"
    elif average >= 50: return "D"
    else: return "F (Fail)"

def main():
    print("--- Student Marks Calculator ---")
    
    # Input student details
    student_name = input("Enter Student Name: ")
    num_subjects = int(input("How many subjects? "))
    
    marks = {}
    
    # Collect marks
    for i in range(num_subjects):
        subject = input(f"Enter name of subject {i+1}: ")
        score = float(input(f"Enter marks for {subject} (out of 100): "))
        marks[subject] = score

    # Logic
    total_marks = sum(marks.values())
    average_percentage = total_marks / num_subjects
    grade = calculate_grade(average_percentage)

    # Output Result
    print("\n" + "="*30)
    print(f"REPORT CARD: {student_name}")
    print("="*30)
    for sub, score in marks.items():
        print(f"{sub}: {score}")
    print("-" * 30)
    print(f"Total Marks: {total_marks} / {num_subjects * 100}")
    print(f"Average: {average_percentage:.2f}%")
    print(f"Final Grade: {grade}")
    print("="*30)

if __name__ == "__main__":
    main()
