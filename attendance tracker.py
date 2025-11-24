import os

ATTENDANCE_FILE = "attendance.txt"

def mark_attendance():
    name = input("Enter student name to mark present: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    with open(ATTENDANCE_FILE, "a") as file:
        file.write(f"{name},{date}\n")
    print(f"Attendance marked for {name} on {date}.\n")

def view_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records found.\n")
        return
    name = input("Enter student name to view attendance: ").strip()
    with open(ATTENDANCE_FILE, "r") as file:
        records = file.readlines()
    dates_present = [line.split(",")[1].strip() for line in records if line.startswith(name + ",")]
    if dates_present:
        print(f"{name} was present on these dates:")
        for d in dates_present:
            print(f" - {d}")
        print(f"Total days present: {len(dates_present)}\n")
    else:
        print(f"No attendance records found for {name}\n")

def main():
    while True:
        print("Student Attendance Tracker")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
