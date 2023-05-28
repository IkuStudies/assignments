#this was a huge pain in the ass, took me days to finally get.  it formats strings of arithmetic to print veritcally.  pretty pointless but good info to learn rstrip and more logic

import re

def arithmetic_arranger(problems, solution=False):
  #check: if more than 5 return error: Too many problems.
  if len(problems)>5:
    return "Error: Too many problems."

  arranged_problems=""
  l1=""
  l2=""
  sumx=""
  lines=""
 
  #input arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
  #output:(n1_list)  32         1      9999      523\n+  (n2_list)8    - 3801    + 9999    -  49\n(line_list)----    ------    ------    -----\n  40     -3800     19998      474
  for problem in problems:
    spl=problem.split()
    n1=spl[0]
    op=spl[1]
    n2=spl[2]
    #check numbers <= 4
    if len(n1)>4 or len(n2)>4:
      return "Error: Numbers cannot be more than four digits."
    #check operator = + or - 
    if op not in ('+', '-'):
      return "Error: Operator must be '+' or '-'."
    #check if numbers are digits
    if not n1.isdigit() or not n2.isdigit():
      return "Error: Numbers must only contain digits."
    #checks complete 
    
    #get number of dashes, append lists
    if len(n1) >= len(n2):
      line_length = len(n1)+2
    else:
      line_length = len(n2)+2
    
    # get sum, append list
    if op == '+':
      sum = int(n1) + int(n2)
    elif op == '-':
      sum = int(n1) - int(n2)

    # set length of sum and top, bottom and line values
    length = max(len(n1), len(n2)) + 2
    top = str(n1).rjust(length)
    bottom = op + str(n2).rjust(length - 1)
    line = ''
    result = str(sum).rjust(length)
    for s in range(length):
      line += '-'
    # add to the overall string
    l1 += top + '    '
    l2 += bottom + '    '
    lines += line + '    '
    sumx += result + '    '
    #l1= l1.rstrip()
    #l2= l2.rstrip()
    #lines= lines.rstrip()
    #sumx= sumx.rstrip()
    if solution == True:
      arranged_problems = l1.rstrip() + '\n' + l2.rstrip() + '\n' + lines.rstrip() + '\n' + sumx.rstrip()
    else:
      arranged_problems = l1.rstrip() + '\n' + l2.rstrip() + '\n' + lines.rstrip()


  return arranged_problems
