History_file = "history.txt"

def show_history():
  try:
    file = open(History_file, "r")
    lines = file.readlines()
    if len(lines) == 0:
      print("No Record found!")
    else:
      for line in reversed(lines):
        print(line.strip())
    file.close()
  except FileNotFoundError:
    print("No Record found!")


def clear_history():
  file = open(History_file, "w")
  file.close()
  print("History cleared!")


def save_to_history(equation, result):
  file = open(History_file, "a")
  file.write(f"{equation} = {str(result)} \n")
  file.close()


def calculation(User_input):
  separate = User_input.split()
  if len(separate) != 3:
    print(
        "Invalid input! Please enter valid format:number operator number(space mandatory, eg.1 + 1): "
    )
    return

  num1 = float(separate[0])
  num2 = float(separate[2])
  operator = separate[1]
  match operator:
    case "+":
      result = num1 + num2
    case "-":
      result = num1 - num2
    case "*":
      result = num1 * num2
    case "/":
      if num2 == 0:
        print("Invalid! Any number cannot be divide by zero. ")
        return
      else:
        result = num1 / num2
    case _:
      print("Invalid Operator! use valid operator(+, -, *, /): ")
      return
  if int(result) == result:
    result = int(result)
  print(f"Result: {result}")
  save_to_history(User_input, result)


def main():
  print("----Simple Calculator----\n")
  while True:
    User_input = input(
        "Enter Calculation(eg. 1+1) or other commands(exit, show_history, clear_history): "
    )
    if User_input == "exit":
      print("GoodBye")
      break
    elif User_input == "clear_history":
      clear_history()
    elif User_input == "show_history":
      show_history()
    else:
      calculation(User_input)


main()
