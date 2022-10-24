def arithmetic_arranger(problems, solution=False):
  #first error condition
  if len(problems) > 5:
    return "Error: Too many problems."
    
  first,second,third, fourth = "", "", "" , ""
  for p in problems:
    ele = p.split()
    #thrid, fourth error condtion
    if ele[0].isdigit() == False:
      return "Error: Numbers must only contain digits." 
    if len(ele[0]) > 4:
      return "Error: Numbers cannot be more than four digits."
    l = ele[0]
    
    #second error condition
    if ele[1] != "+" and ele[1] != "-":
      return "Error: Operator must be '+' or '-'."
    op = ele[1]
    
    #thrid ,fourth error condtion
    if ele[2].isdigit() == False:
      return "Error: Numbers must only contain digits."
    if len(ele[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    r = ele[2]
  
    space_len = max(len(l), len(r)) + 2
    four_space = " " * 4
    
    #fourth line
    if solution == True:
      if op == "+":
        answer = str(int(l) + int(r))
      else:
        answer = str(int(l) - int(r))

      if p == problems[-1]:
        fourth += (space_len - len(answer)) * " " + answer
      else:
        fourth += (space_len - len(answer)) * " " + answer + four_space
        
    #set up first line , second line , third
    if p == problems[-1]: #check if 
      first += (space_len - len(l)) * " " + l
      second += op + ((space_len - len(r) - 1) * " ") + r
      third += space_len * "-"
    else:
      first += (space_len - len(l)) * " " + l + four_space
      second += op + ((space_len - len(r) - 1) * " ") + r + four_space
      third += (space_len * "-") + four_space

  if solution == True:
    arranged_problems = first + "\n" + second + "\n" + third + "\n" + fourth
  else:
    arranged_problems = first + "\n" + second + "\n" + third
   
  return arranged_problems
