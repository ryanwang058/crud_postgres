import crud as c

def main():
  table = "students"
  crud = c.CRUD(table)

  option = input("Enter option (1 for READ, 2 for ADD, 3 for UPDATE, 4 for DELETE, q to Quit): ")
  while (option != 'q'):
    if option == '1':
      print("READ")
      crud.getAllStudents()
    elif option == '2':
      print("ADD")
      crud.addStudent('Joseph', 'Stone', 'jo.st@example.com', '2023-09-03')
    elif option == '3':
      print("UPDATE")
      crud.updateStudentEmail(4, 'new.jo.st@example.com')
    elif option == '4':
      print("DELETE")
      crud.deleteStudent(4)
    else:
      print("Wrong input. 1 for READ, 2 for ADD, 3 for UPDATE, 4 for DELETE")
    print("----------------")
    option = input("Enter option (1 for READ, 2 for ADD, 3 for UPDATE, 4 for DELETE, q to Quit): ")

if __name__ == "__main__":
  main()