import random

def tweet() :
  yell = (random.uniform(0.0, 1.0) < .25)
  
  if (yell):
    lines = open('words.txt').read().splitlines()
  else:
    lines = open('allwords.txt').read().splitlines()
  
  def f(x):
    return {
      0: ".",
      1: "!",
      2: "?",
      3: ",",
      4: ",",
      5: ",",
      6: ":",
    }[x] 

  def format(x, yell):
    t = x[0].upper() + x[1:]
    if (yell):
       t = t.upper()
    return t

  myline = ""
  numWords = range(random.randint(2,5)*random.randint(3,4))
  for i in numWords:
    myline += random.choice(lines)
    if (i != max(numWords)):
      if (not yell and random.uniform(0.0, 1.0) < .1): 
        myline += f(random.randint(3,6))
      myline += " "	

  myline = format(myline, yell)
  myline += f(random.randint(0,2))

  return myline
