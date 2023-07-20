import logging

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample list of dictionaries containing student information
students = [
    {"name": "Alice", "age": 21, "marks": 85},
    {"name": "Bob", "age": 22, "marks": 76},
    {"name": "Charlie", "age": 20, "marks": 92},
    {"name": "David", "age": 19, "marks": 88},
    {"name": "Eve", "age": 21, "marks": 82},
    {"name": "Frank", "age": 20, "marks": 78},
]

def main():
    # Challenge 1: Sort the list of dictionaries by "marks" in descending order and then by "name" in ascending order
    sorted_students = sorted(students, key=lambda x: (-x["marks"], x["name"]))
    logging.info("Challenge 1 - Sorted Students:")
    for student in sorted_students:
        logging.info(student)

    # Challenge 2: Find the student(s) with the highest marks
    highest_marks = sorted_students[0]["marks"]
    top_students = [student["name"] for student in sorted_students if student["marks"] == highest_marks]
    logging.info("Challenge 2 - Student(s) with Highest Marks: %s", top_students)

    # Challenge 3: Calculate the average age of students
    total_age = sum(student["age"] for student in students)
    average_age = total_age / len(students)
    logging.info("Challenge 3 - Average Age of Students: %s", average_age)

    # Challenge 4: Create a dictionary with "name" as key and "age" as value
    name_age_dict = {student["name"]: student["age"] for student in students}
    logging.info("Challenge 4 - Name-Age Dictionary:")
    logging.info(name_age_dict)

if __name__ == "__main__":
    main()
