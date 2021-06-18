
def arithmetic_arranger(problems, show = False):
  firstAnswer = ""
  secondAnswer = ""
  answer = ""
  sumUp = ""
  operator = ""
  dashlines = ""
  sum = ""
  
  if(len(problems) > 5):
    return "Error: Too many problems."

  for problem in problems:
    # Spliting strings and extracting useful information
    firstNumber = problem.split()[0]
    operator = problem.split()[1]
    secondNumber = problem.split()[2]

    # Checking number length
    if (len(firstNumber) > 4 or len(secondNumber) > 4):
      return "Error: Numbers cannot be more than four digits."

    # checking validity of input
    if not firstNumber.isnumeric() or not secondNumber.isnumeric():
      return "Error: Numbers must only contain digits."

    # checking correct operators
    
    if (operator == '+' or operator == '-'):
      if operator == "+": 
        sum = str(int(firstNumber) + int(secondNumber))
      if operator == "-":
        sum = str(int(firstNumber) - int(secondNumber))
    else: 
      return "Error: Operator must be '+' or '-'."

    length = max(len(firstNumber) , len(secondNumber)) + 2
    firstLine = str(firstNumber).rjust(length)
    secondLine = operator + str(secondNumber.rjust(length - 1))
    sltn = str(sum.rjust(length))
    
  # For formatting code output 
    dashLine = ""
    for dash in range(length):
      dashLine += "-"

    if problem != problems[-1]: 
      firstAnswer += firstLine + '    '
      secondAnswer += secondLine + '    '
      dashlines += dashLine + '    '
      sumUp += sltn + '    '
    else: 
      firstAnswer += firstLine
      secondAnswer += secondLine 
      dashlines += dashLine 
      sumUp += sltn  
      
# output
  if show: 
    answer = firstAnswer + "\n" + secondAnswer + "\n" + dashlines + "\n" + sumUp
  else:
    answer = firstAnswer + "\n" + secondAnswer + "\n" + dashlines    
  return answer
          