
'''This project is a simple student management system implemented in Python. 
It maintains a list of students, where each student’s details include their name, ID, section, and marks in five subjects. 
The program calculates the total marks and percentage for each student based on their subject scores.
 Users can add new students by entering their details, which are then appended to the existing student list.
It also allows viewing all students along with their computed total marks and percentages.
There is a search functionality that lets users find a student by their unique ID quickly. 
The system ensures that marks are always up to date by recalculating totals and percentages whenever data is accessed or modified.
This project can be used to keep track of academic performance in a simple and efficient manner.
It is a command-line tool designed for ease of use, making it accessible for beginners. 
Overall, this project serves as a basic yet functional example of managing and processing student data programmatically.'''

students = [
    {"Name":"Aarav Sharma", "ID":"S001", "Section":"D", "Sub1":78, "Sub2":7,  "Sub3":94, "Sub4":99, "Sub5":91 },
    {"Name":"Rohan Mehta", "ID":"S002", "Section":"C", "Sub1":50, "Sub2":90, "Sub3":20, "Sub4":14, "Sub5":6 },
    {"Name":"Karan Singh", "ID":"S003", "Section":"C", "Sub1":63, "Sub2":48, "Sub3":95, "Sub4":33, "Sub5":90 },
    {"Name":"Anjali Patel", "ID":"S004", "Section":"A", "Sub1":97, "Sub2":32, "Sub3":10, "Sub4":47, "Sub5":57 },
    {"Name":"Neha Gupta", "ID":"S005", "Section":"C", "Sub1":40, "Sub2":100,"Sub3":67, "Sub4":28, "Sub5":37 },
    {"Name":"Aditya Nair", "ID":"S006", "Section":"D", "Sub1":30, "Sub2":36, "Sub3":96, "Sub4":42, "Sub5":60 },
    {"Name":"Priya Sharma", "ID":"S007", "Section":"B", "Sub1":79, "Sub2":82, "Sub3":15, "Sub4":23, "Sub5":99 },
    {"Name":"Rahul Verma", "ID":"S008", "Section":"B", "Sub1":29, "Sub2":100,"Sub3":66, "Sub4":51, "Sub5":83 },
    {"Name":"Sonal Iyer", "ID":"S009", "Section":"C", "Sub1":51, "Sub2":4,  "Sub3":35, "Sub4":1,  "Sub5":46 },
    {"Name":"Vikas Rao", "ID":"S010", "Section":"A", "Sub1":42, "Sub2":91, "Sub3":63, "Sub4":97, "Sub5":25 },
    {"Name":"Divya Reddy", "ID":"S011", "Section":"B", "Sub1":73, "Sub2":5,  "Sub3":6,  "Sub4":66, "Sub5":64 },
    {"Name":"Suresh Kumar", "ID":"S012", "Section":"D", "Sub1":28, "Sub2":81, "Sub3":33, "Sub4":76, "Sub5":54 },
    {"Name":"Anita Desai", "ID":"S013", "Section":"B", "Sub1":60, "Sub2":94, "Sub3":1,  "Sub4":40, "Sub5":79 },
    {"Name":"Manish Joshi", "ID":"S014", "Section":"C", "Sub1":39, "Sub2":43, "Sub3":97, "Sub4":77, "Sub5":97 },
    {"Name":"Neelam Singh", "ID":"S015", "Section":"C", "Sub1":74, "Sub2":7,  "Sub3":71, "Sub4":7,  "Sub5":68 },
    {"Name":"Rakesh Sharma","ID":"S016", "Section":"B", "Sub1":59, "Sub2":37, "Sub3":16, "Sub4":26, "Sub5":48 },
    {"Name":"Pooja Mishra", "ID":"S017", "Section":"A", "Sub1":62, "Sub2":84, "Sub3":70, "Sub4":96, "Sub5":28 },
    {"Name":"Amit Verma", "ID":"S018", "Section":"B", "Sub1":2,  "Sub2":51, "Sub3":56, "Sub4":71, "Sub5":37 },
    {"Name":"Deepak Jain", "ID":"S019", "Section":"B", "Sub1":89, "Sub2":26, "Sub3":51, "Sub4":35, "Sub5":7, },
    {"Name":"Sheetal Reddy", "ID":"S020", "Section":"C", "Sub1":52, "Sub2":99, "Sub3":68, "Sub4":19, "Sub5":69 },
    {"Name":"Ravi Gupta", "ID":"S021", "Section":"D", "Sub1":94, "Sub2":97, "Sub3":10, "Sub4":16, "Sub5":20 },
    {"Name":"Kavita Shah", "ID":"S022", "Section":"B", "Sub1":8,  "Sub2":10, "Sub3":77, "Sub4":35, "Sub5":39 },
    {"Name":"Harsh Malhotra","ID":"S023", "Section":"C", "Sub1":24, "Sub2":81, "Sub3":62, "Sub4":29, "Sub5":97 },
    {"Name":"Mira Kapoor", "ID":"S024", "Section":"C", "Sub1":13, "Sub2":69, "Sub3":88, "Sub4":75, "Sub5":51 },
    {"Name":"Nitin Deshmukh","ID":"S025", "Section":"D", "Sub1":88, "Sub2":28, "Sub3":36, "Sub4":13, "Sub5":47 },
    {"Name":"Sonia Rani", "ID":"S026", "Section":"C", "Sub1":27, "Sub2":14, "Sub3":53, "Sub4":54, "Sub5":65 },
    {"Name":"Vijay Bhat", "ID":"S027", "Section":"A", "Sub1":26, "Sub2":0,  "Sub3":10, "Sub4":62, "Sub5":37 },
    {"Name":"Anju Singh", "ID":"S028", "Section":"C", "Sub1":36, "Sub2":37, "Sub3":61, "Sub4":31, "Sub5":93 },
    {"Name":"Sanjay Thakur", "ID":"S029", "Section":"D", "Sub1":81, "Sub2":92, "Sub3":77, "Sub4":87, "Sub5":81} ,
    {"Name":"Nisha Yadav", "ID":"S030", "Section":"C", "Sub1":12, "Sub2":38, "Sub3":63, "Sub4":35, "Sub5":95 },
    {"Name":"Raghav Desai", "ID":"S031", "Section":"C", "Sub1":100,"Sub2":82, "Sub3":44, "Sub4":95, "Sub5":36 },
    {"Name":"Pallavi Nair", "ID":"S032", "Section":"D", "Sub1":66, "Sub2":19, "Sub3":57, "Sub4":16, "Sub5":29 },
    {"Name":"Suresh Kumar","ID":"S033", "Section":"B", "Sub1":3,  "Sub2":18, "Sub3":68, "Sub4":10, "Sub5":82 },
    {"Name":"Meena Iyer", "ID":"S034", "Section":"B", "Sub1":98, "Sub2":86, "Sub3":10, "Sub4":60, "Sub5":54 },
    {"Name":"Arjun Joshi", "ID":"S035", "Section":"D", "Sub1":27, "Sub2":83, "Sub3":80, "Sub4":91, "Sub5":72} ,
    {"Name":"Radha Sharma","ID":"S036", "Section":"A", "Sub1":77, "Sub2":90, "Sub3":99, "Sub4":90, "Sub5":13 },
    {"Name":"Manoj Verma", "ID":"S037", "Section":"A", "Sub1":51, "Sub2":24, "Sub3":99, "Sub4":87, "Sub5":36 },
    {"Name":"Bhavna Singh","ID":"S038", "Section":"D", "Sub1":93, "Sub2":90, "Sub3":75, "Sub4":98, "Sub5":24 },
    {"Name":"Kiran Patel", "ID":"S039", "Section":"C", "Sub1":27, "Sub2":17, "Sub3":64, "Sub4":26, "Sub5":65 },
    {"Name":"Laxmi Reddy", "ID":"S040", "Section":"C", "Sub1":92, "Sub2":35, "Sub3":81, "Sub4":32, "Sub5":5, },
    {"Name":"Rahul Gupta","ID":"S041", "Section":"A", "Sub1":4,  "Sub2":25, "Sub3":47, "Sub4":21, "Sub5":44 },
    {"Name":"Neeta Sharma","ID":"S042", "Section":"B", "Sub1":22, "Sub2":85, "Sub3":4,  "Sub4":56, "Sub5":43 },
    {"Name":"Deepak Kumar","ID":"S043", "Section":"B", "Sub1":58, "Sub2":88, "Sub3":38, "Sub4":41, "Sub5":33 },
    {"Name":"Sonal Joshi","ID":"S044", "Section":"D", "Sub1":74, "Sub2":65, "Sub3":22, "Sub4":38, "Sub5":66 },
    {"Name":"Anil Nair", "ID":"S045", "Section":"D", "Sub1":31, "Sub2":78, "Sub3":93, "Sub4":34, "Sub5":89 },
    {"Name":"Tina Rani","ID":"S046", "Section":"A", "Sub1":53, "Sub2":6,  "Sub3":96, "Sub4":54, "Sub5":89 },
    {"Name":"Rajiv Malhotra","ID":"S047", "Section":"A", "Sub1":73, "Sub2":40, "Sub3":17, "Sub4":80, "Sub5":84 },
    {"Name":"Anusha Desai","ID":"S048", "Section":"C", "Sub1":95, "Sub2":4,  "Sub3":76, "Sub4":44, "Sub5":19 },
    {"Name":"Kamal Shah", "ID":"S049", "Section":"C", "Sub1":13, "Sub2":67, "Sub3":26, "Sub4":95, "Sub5":99 },
    {"Name":"Ritika Bhat","ID":"S050", "Section":"C", "Sub1":18, "Sub2":28, "Sub3":39, "Sub4":79, "Sub5":41 },
    {"Name":"Sanjay Mehta","ID":"S051", "Section":"C", "Sub1":50, "Sub2":57, "Sub3":19, "Sub4":90, "Sub5":50 },
    {"Name":"Megha Iyer","ID":"S052", "Section":"B", "Sub1":15, "Sub2":23, "Sub3":94, "Sub4":19, "Sub5":76 },
    {"Name":"Rohit Verma","ID":"S053", "Section":"A", "Sub1":81, "Sub2":83, "Sub3":10, "Sub4":87, "Sub5":76 },
    {"Name":"Sneha Joshi","ID":"S054", "Section":"D", "Sub1":57, "Sub2":65, "Sub3":50, "Sub4":31, "Sub5":31 },
    {"Name":"Vivek Nair","ID":"S055", "Section":"C", "Sub1":19, "Sub2":23, "Sub3":74, "Sub4":73, "Sub5":41 },
    {"Name":"Neelam Singh","ID":"S056", "Section":"C", "Sub1":16, "Sub2":27, "Sub3":70, "Sub4":57, "Sub5":31 },
    {"Name":"Amit Desai","ID":"S057", "Section":"A", "Sub1":81, "Sub2":39, "Sub3":26, "Sub4":36, "Sub5":68 },
    {"Name":"Kajal Sharma","ID":"S058", "Section":"A", "Sub1":83, "Sub2":24, "Sub3":23, "Sub4":41, "Sub5":85 },
    {"Name":"Vikram Gupta","ID":"S059", "Section":"B", "Sub1":94, "Sub2":43, "Sub3":53, "Sub4":80, "Sub5":20 },
    {"Name":"Ritu Malhotra","ID":"S060", "Section":"A", "Sub1":94, "Sub2":27, "Sub3":50, "Sub4":41, "Sub5":20 },
    {"Name":"Harsh Jain", "ID":"S061", "Section":"A", "Sub1":11, "Sub2":54, "Sub3":82, "Sub4":33, "Sub5":81 },
    {"Name":"Neha Kapoor","ID":"S062", "Section":"C", "Sub1":21, "Sub2":83, "Sub3":44, "Sub4":65, "Sub5":55 },
    {"Name":"Ramesh Kumar","ID":"S063", "Section":"A", "Sub1":58, "Sub2":17, "Sub3":18, "Sub4":64, "Sub5":51 },
    {"Name":"Suman Reddy","ID":"S064", "Section":"C", "Sub1":29, "Sub2":21, "Sub3":26, "Sub4":37, "Sub5":10,},
    {"Name":"Aakash Verma","ID":"S065", "Section":"D", "Sub1":54, "Sub2":17, "Sub3":49, "Sub4":81, "Sub5":89 },
    {"Name":"Sheetal Sharma","ID":"S066", "Section":"C", "Sub1":79, "Sub2":51, "Sub3":5,  "Sub4":89, "Sub5":90 },
    {"Name":"Vijay Singh","ID":"S067", "Section":"D", "Sub1":81, "Sub2":77, "Sub3":40, "Sub4":44, "Sub5":40 },
    {"Name":"Alok Jain", "ID":"S068", "Section":"B", "Sub1":69, "Sub2":28, "Sub3":10, "Sub4":27, "Sub5":74 },
    {"Name":"Kiran Patel","ID":"S069", "Section":"B", "Sub1":41, "Sub2":89, "Sub3":14, "Sub4":28, "Sub5":71 },
    {"Name":"Rajesh Gupta","ID":"S070", "Section":"A", "Sub1":72, "Sub2":97, "Sub3":11, "Sub4":41, "Sub5":51 },
    {"Name":"Anjali Rani","ID":"S071", "Section":"B", "Sub1":68, "Sub2":15, "Sub3":39, "Sub4":18, "Sub5":90 },
    {"Name":"Amit Mehta","ID":"S072", "Section":"D", "Sub1":20, "Sub2":88, "Sub3":84, "Sub4":41, "Sub5":68 },
    {"Name":"Sunita Deshmukh","ID":"S073", "Section":"C", "Sub1":81, "Sub2":88, "Sub3":5,  "Sub4":22, "Sub5":30 },
    {"Name":"Sanjay Sharma","ID":"S074", "Section":"D", "Sub1":92, "Sub2":71, "Sub3":61, "Sub4":87, "Sub5":81 },
    {"Name":"Pooja Singh","ID":"S075", "Section":"B", "Sub1":50, "Sub2":24, "Sub3":20, "Sub4":43, "Sub5":96 },
    {"Name":"Rohit Patel","ID":"S076", "Section":"A", "Sub1":71, "Sub2":96, "Sub3":36, "Sub4":60, "Sub5":36 },
    {"Name":"Meena Rani","ID":"S077", "Section":"D", "Sub1":67, "Sub2":90, "Sub3":41, "Sub4":35, "Sub5":58 },
    {"Name":"Vikas Kumar","ID":"S078", "Section":"C", "Sub1":21, "Sub2":38, "Sub3":67, "Sub4":39, "Sub5":76 },
    {"Name":"Radha Sharma","ID":"S079", "Section":"B", "Sub1":34, "Sub2":81, "Sub3":19, "Sub4":37, "Sub5":54 },
    {"Name":"Kamal Verma","ID":"S080", "Section":"C", "Sub1":39, "Sub2":16, "Sub3":26, "Sub4":18, "Sub5":47 },
    {"Name":"Priya Joshi","ID":"S081", "Section":"B", "Sub1":79, "Sub2":32, "Sub3":96, "Sub4":54, "Sub5":89 },
    {"Name":"Manoj Shah","ID":"S082", "Section":"A", "Sub1":50, "Sub2":36, "Sub3":70, "Sub4":99, "Sub5":31 },
    {"Name":"Asha Singh","ID":"S083", "Section":"D", "Sub1":47, "Sub2":64, "Sub3":81, "Sub4":87, "Sub5":54 },
    {"Name":"Raju Malhotra","ID":"S084", "Section":"B", "Sub1":78, "Sub2":53, "Sub3":18, "Sub4":33, "Sub5":45 },
    {"Name":"Sita Nair","ID":"S085", "Section":"D", "Sub1":17, "Sub2":75, "Sub3":26, "Sub4":10, "Sub5":54 },
    {"Name":"Vimal Reddy","ID":"S086", "Section":"D", "Sub1":80, "Sub2":81, "Sub3":50, "Sub4":99, "Sub5":31 },
    {"Name":"Kiran Kumar","ID":"S087", "Section":"D", "Sub1":36, "Sub2":19, "Sub3":67, "Sub4":67, "Sub5":86 },
    {"Name":"Suman Joshi","ID":"S088", "Section":"C", "Sub1":88, "Sub2":77, "Sub3":56, "Sub4":65, "Sub5":49 },
    {"Name":"Nitin Shah","ID":"S089", "Section":"B", "Sub1":66, "Sub2":82, "Sub3":37, "Sub4":33, "Sub5":54 },
    {"Name":"Sneha Patel","ID":"S090", "Section":"A", "Sub1":59, "Sub2":70, "Sub3":26, "Sub4":45, "Sub5":83 },
    {"Name":"Rakesh Singh","ID":"S091", "Section":"D", "Sub1":45, "Sub2":80, "Sub3":32, "Sub4":91, "Sub5":78 },
    {"Name":"Preeti Rani","ID":"S092", "Section":"B", "Sub1":58, "Sub2":77, "Sub3":40, "Sub4":53, "Sub5":90 },
    {"Name":"Vivek Verma","ID":"S093", "Section":"C", "Sub1":89, "Sub2":90, "Sub3":74, "Sub4":88, "Sub5":91 },
    {"Name":"Meena Gupta","ID":"S094", "Section":"B", "Sub1":55, "Sub2":44, "Sub3":67, "Sub4":66, "Sub5":54 },
    {"Name":"Rohit Malhotra","ID":"S095", "Section":"C", "Sub1":82, "Sub2":89, "Sub3":72, "Sub4":58, "Sub5":51 },
    {"Name":"Aarav Sharma", "ID":"S096", "Section":"C", "Sub1":81, "Sub2":64, "Sub3":47, "Sub4":87, "Sub5":54 },
    {"Name":"Rohan Mehta", "ID":"S097", "Section":"B", "Sub1":78, "Sub2":53, "Sub3":18, "Sub4":33, "Sub5":45 },
    {"Name":"Karan Singh", "ID":"S098", "Section":"D", "Sub1":17, "Sub2":75, "Sub3":26, "Sub4":10, "Sub5":54 },
    {"Name":"Anjali Patel","ID":"S099", "Section":"D", "Sub1":80, "Sub2":81, "Sub3":50, "Sub4":99, "Sub5":31 },
    {"Name":"Neha Gupta",  "ID":"S100", "Section":"D", "Sub1":36, "Sub2":19, "Sub3":67, "Sub4":67, "Sub5":86 }
]


def calculate_marks():
    for s in students:
        s['Total'] = s['Sub1'] + s['Sub2'] + s['Sub3'] + s['Sub4'] + s['Sub5']
        s['Percentage'] = (s['Total'] / 500) * 100 



def add_student():
    print("\nEnter new student details:")
    name = input("Name: ")
    student_id = input("ID: ")
    section = input("Section: ")
    sub1 = int(input("Sub1 marks: "))
    sub2 = int(input("Sub2 marks: "))
    sub3 = int(input("Sub3 marks: "))
    sub4 = int(input("Sub4 marks: "))
    sub5 = int(input("Sub5 marks: "))
    
    new_student = {
        "Name": name,
        "ID": student_id,
        "Section": section,
        "Sub1": sub1,
        "Sub2": sub2,
        "Sub3": sub3,
        "Sub4": sub4,
        "Sub5": sub5
    }
    
    students.append(new_student)
    calculate_marks()
    print(f"Student {name}, ID: {student_id}, Section: {section}, "
          f"Sub1: {sub1}, Sub2: {sub2}, Sub3: {sub3}, Sub4: {sub4}, Sub5: {sub5}, "
          f"Total: {new_student['Total']}, Percentage: {new_student['Percentage']}% added successfully!\n")


def view_students():
    calculate_marks()
    print("\nAll Students:")
    for s in students:
        print(f"Name: {s['Name']}, ID: {s['ID']}, Section: {s['Section']}, "
              f"Subs: [{s['Sub1']}, {s['Sub2']}, {s['Sub3']}, {s['Sub4']}, {s['Sub5']}], "
              f"Total: {s['Total']}, Percentage: {s['Percentage']}%")


def search_student():
    calculate_marks()    
    key = input("Enter studentID to search: ")
    for s in students:
        if s.get('ID') == key:
            calculate_marks()
            print(f"Name: {s['Name']}, ID: {s['ID']}, Section: {s['Section']}, "
                  f"Subs: [{s['Sub1']}, {s['Sub2']}, {s['Sub3']}, {s['Sub4']}, {s['Sub5']}], "
                  f"Total: {s['Total']}, Percentage: {s['Percentage']:.2f}%")
            
            

def update_student():
    student_id = input("Enter student ID: ")
    for s in students:
        if s['ID'] == student_id:
            print("What do you want to update?")
            print("1. Name")
            print("2. Marks")
            print("3. Section")
            print("4. ID")
            choice = input("Choose option (1-4): ")
            if choice == '1':
                new_name = input("Enter new name: ")
                if new_name:
                    s['Name'] = new_name
            elif choice == '2':
                print("Enter new marks (press Enter to keep current marks):")
                
                s['Sub1'] = int(input(f"Sub1 ({s['Sub1']}): ") or s['Sub1'])
                s['Sub2'] = int(input(f"Sub2 ({s['Sub2']}): ") or s['Sub2'])
                s['Sub3'] = int(input(f"Sub3 ({s['Sub3']}): ") or s['Sub3'])
                s['Sub4'] = int(input(f"Sub4 ({s['Sub4']}): ") or s['Sub4'])
                s['Sub5'] = int(input(f"Sub5 ({s['Sub5']}): ") or s['Sub5'])
                
                s['Total'] = s['Sub1'] + s['Sub2'] + s['Sub3'] + s['Sub4'] + s['Sub5']
                s['Percentage'] = (s['Total'] / 500) * 100
            elif choice == '3':
                new_section = input("Enter new section: ")
                if new_section:
                    s['Section'] = new_section
            elif choice == '4':
                new_id = input("Enter new ID: ")
                if new_id:
                    s['ID'] = new_id
def delete_student():       
    student_id = input("Enter student ID to delete: ")
    for i, s in enumerate(students):
        if s['ID'] == student_id:
            del students[i]
            print("Student deleted successfully.")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")  
        

    
