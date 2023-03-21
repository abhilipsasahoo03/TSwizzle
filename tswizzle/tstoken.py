import os

def translateCode(line):
  try:
     nline=line
     if "AND I'LL SHOW YOU EVERY VERSION OF " in nline:
          nline = nline.replace("AND I'LL SHOW YOU EVERY VERSION OF ", 'print(')
          nline = nline.replace(" TONIGHT", ')')
     if "GOODBYE GOODBYE GOODBYE" in nline:
          nline = nline.replace("GOODBYE GOODBYE GOODBYE", "pass")
     if 'ARE WE IN THE CLEAR YET?' in line:
          nline = nline.replace("ARE WE IN THE CLEAR YET?","os.system('cls')")
     if line.find('SPEAK NOW OR FOREVER HOLD YOUR ') == 0:
          nline = line.replace('SPEAK NOW OR FOREVER HOLD YOUR ', '')
          nline = assignInputType(nline)
     if line.find('COUNTER ALL YOUR QUICK REMARKS ~> ') == 0:
          nline = line.replace('COUNTER ALL YOUR QUICK REMARKS ~>', '#')
     if line.find("IF YOU'VE GOT A (") == 0:
          nline = checkCondition(nline)
     return nline
  except ValueError:
      print("WRONG LYRIC.")
  except NameError:
      print("ERROR HAS OCCURED.")

def assignInputType(code):
    if code.find('NUMBER ON ME ')==0:
        code = code.replace('NUMBER ON ME ', '', 1)
        code = code + " = [int(x) for x in input('Enter input: ').split()]"
    if code.find('INVISIBLE STRING TYING YOU TO ME ')==0:
        code = code.replace('INVISIBLE STRING TYING YOU TO ME ', '', 1)
        code = code + " = [str(x) for x in input('Enter input: ').split()]"
    return code
    
def checkCondition(line):
      nline=""
      nline = line.replace("IF YOU'VE GOT A", "if")
      if "I'M JEALOUS OF " in nline:
          nline = nline.replace(" I'M JEALOUS OF ", ": ")
      else:
          print("MISSING STATEMENT UNDER IF CONDITION.")
      if "BUT IF YOU'RE SINGLE (" in line:
          nline = nline.replace(" BUT IF YOU'RE SINGLE ", "\nelif")
          if "THAT'S HONESTLY WORSE" in line:
              nline = nline.replace(" THAT'S HONESTLY WORSE ", ": ")
          else:
              print("MISSING STATEMENT UNDER ELIF CONDITION.")
      if "CAUSE YOU'RE SO GORGEOUS IT ACTUALLY " in line:
          nline = nline.replace(" CAUSE YOU'RE SO GORGEOUS IT ACTUALLY ", "\nelse: ")
      newline = translateCode(nline)
      return newline
