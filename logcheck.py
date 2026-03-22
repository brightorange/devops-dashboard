def check_log():
  filename = input("Enter file name: ")
  try: 
    with open(filename, "r") as file:
      for line in file:
        if "ERROR" in line:
          print(line, '\n')
  except FileNotFoundError:
    print(f"Error: File '{filename}' does not exist.")
