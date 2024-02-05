class StudentRecord:
    def __init__(self, locker_number, surname, first_name, student_id):
        self.locker_number = locker_number
        self.surname = surname
        self.first_name = first_name
        self.student_id = student_id

    def update(self, locker_number, surname, first_name, student_id):
        self.locker_number = locker_number
        self.surname = surname
        self.first_name = first_name
        self.student_id = student_id

def main_screen():
    print("Welcome to the Locker Information System")
    print("\nWhat would you like to do?")
    print("1. Input student information")
    print("2. Update information")
    print("3. Display current record")
    print("4. Search for a student")
    print("5. Quit")
    print()

def info_input(student_records):
    num_records = int(input("\nHow many data you want to enter? "))
    for i in range(num_records):
        print(f"\nRecord #{i + 1}")
        locker_number = int(input("Locker Number: "))
        surname = input("Surname: ")
        first_name = input("First Name: ")
        student_id = input("Student ID: ")
        student_records.append(StudentRecord(locker_number, surname, first_name, student_id))
    save_to_file(student_records)

def info_update(student_records):
    search_param = input("\nEnter search parameter: ")
    found_record = next((record for record in student_records if
                         record.surname.lower() == search_param.lower() or
                         record.first_name.lower() == search_param.lower() or
                         record.student_id == search_param or
                         str(record.locker_number) == search_param), None)
    if found_record:
        display_record_header()
        display_record(found_record)

        if input("\nDo you want to update this record? (y/n): ").strip().upper() == "Y":
            new_locker_number = int(input("New Locker Number: "))
            new_surname = input("New Surname: ")
            new_first_name = input("New First Name: ")
            new_student_id = input("New Student ID: ")
            found_record.update(new_locker_number, new_surname, new_first_name, new_student_id)
            save_to_file(student_records)
            print("\nRecord updated successfully!")
        else:
            print("\nReturning to the main screen...")
    else:
        print("\nRecord not found.")

def record_display(student_records):
    display_record_header()
    for record in student_records:
        display_record(record)

def search(student_records):
    search_param = input("\nEnter search parameter: ")
    found_record = next((record for record in student_records if
                         record.surname.lower() == search_param.lower() or
                         record.first_name.lower() == search_param.lower() or
                         record.student_id == search_param or
                         str(record.locker_number) == search_param), None)
    if found_record:
        display_record_header()
        display_record(found_record)
        if input("\nSearch again? (y/n): ").strip().upper() == "N":
            print("\nReturning to the main screen...")
    else:
        print("\nRecord not found.")

def quit_program(student_records):
    if input("\nAre you sure you want to quit? (Y/N): ").strip().upper() == "Y":
        save_to_file(student_records)
        print("\nQuitting...")
        exit()
    else:
        print("\nReturning to the main screen...")

def save_to_file(student_records):
    try:
        with open("data.txt", "w") as writer:
            writer.write(str(len(student_records)) + "\n")
            for record in student_records:
                writer.write(f"{record.locker_number};{record.surname};{record.first_name};{record.student_id}\n")
    except IOError as ex:
        print(f"Error saving to file: {ex}")

def load_from_file():
    student_records = []
    try:
        with open("data.txt", "r") as reader:
            num_records = int(reader.readline())
            for _ in range(num_records):
                data = reader.readline().strip().split(';')
                locker_number = int(data[0])
                surname = data[1]
                first_name = data[2]
                student_id = data[3]
                student_records.append(StudentRecord(locker_number, surname, first_name, student_id))
    except IOError as ex:
        print(f"Error loading from file: {ex}")
    return student_records

def display_record_header():
    print("Locker\tSurname\t\tFirst Name\tStudent ID")

def display_record(record):
    print(f"{record.locker_number}\t{record.surname}\t\t{record.first_name}\t{record.student_id}")

def main():
    student_records = load_from_file()
    while True:
        main_screen()
        selection = input().strip()
        if selection == "1":
            info_input(student_records)
        elif selection == "2":
            info_update(student_records)
        elif selection == "3":
            record_display(student_records)
        elif selection == "4":
            search(student_records)
        elif selection == "5":
            quit_program(student_records)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
