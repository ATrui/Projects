def arithmetic_arranger(problems, solution=False):

  if len(problems) > 5:
    return "Error: Too many problems."

  operators = ["+", "-"]

  line_1 = ""
  line_2 = ""
  line_3 = ""
  line_4 = ""

  for i, problem in enumerate(problems):
    n1, op, n2 = problem.split(" ")
    # Check for errors
    if op not in operators:
      return "Error: Operator must be '+' or '-'."
    if not (n1.isdigit() and n2.isdigit()):
      return "Error: Numbers must only contain digits."
    if len(n1) > 4 or len(n2) > 4:
      return "Error: Numbers cannot be more than four digits."

    if op == "+":
      result = int(n1) + int(n2)
    else:
      result = int(n1) - int(n2)

    space = max(len(n1), len(n2))

    line_1 = line_1 + n1.rjust(space+2)
    line_2 = line_2 + op + n2.rjust(space+1)
    line_3 = line_3 + "".rjust(space+2, "-")
    line_4 =  line_4 + str(result).rjust(space+2)

    if i < len(problems) - 1:
      line_1 += "    "
      line_2 += "    "
      line_3 += "    "
      line_4 += "    "

  if solution:
    arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
  else:
    arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3

  return arranged_problems