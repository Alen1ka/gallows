import random
WORDS = ("woman", "student", "teacher", "president", "motherbook", "computer", "place", "picture", "bottle", "table", "chair", "rabbit", "elephant", "chicken", "horse")
Word = random.choice(WORDS)
d=len(Word)
w=d
field = ('-')
x=0
while d>1: 
  z=('-')
  field = field + z
  d = d - 1
  x = x + 1
o=0
v=[]
a = list(Word)
b = list(field)
print('\n |\n |\n |\n |\n |\n |\n |\n |\n------------------\n')
while True:
  m=0
  n=0
  if o==1:
    print('\n |--------\n |\n |\n |\n |\n |\n |\n |\n------------------\n')

  elif o==2:
    print('\n |--------\n |     |\n |     |\n |\n |\n |\n |\n |\n------------------\n')

  elif o==3:
    print('\n |--------\n |     |\n |     |\n |     O\n |\n |\n |\n |\n------------------\n')

  elif o==4:
    print('\n |--------\n |     |\n |     |\n |     O\n |     |\n |\n |\n \n------------------\n')

  elif o==5:
    print('\n |--------\n |     |\n |     |\n |     O\n |    /|\n |\n |\n \n------------------\n')

  elif o==6:
    print('\n |--------\n |     |\n |     |\n |     O\n |    /|\ \n |\n |\n \n------------------\n')

  elif o==7:
    print('\n |--------\n |     |\n |     |\n |     O\n |    /|\ \n |    /\n |\n \n------------------\n')

  print ("\nThe word is made up: ")
  for p in b:
    print(p,end = '')
  letter = input("\nEnter letter ")
  v.append(letter)
  import os
  os.system('clear')
  if v.count(letter)==2:
    v.remove(letter)
    print('\nYou cannot enter a character more than once; try again.')
    n=n+1

  if n==0:
    q = -1
    z = 0
    for i in Word:
      q=q+1
      if i == letter:
        del b[q]
        b.insert(q, a[q])
        if z==0:
          print('\nYou opened the letter', i)
        z = z + 1
        w=w-1
        m=m+1

  print('\nYou have already entered the letters:', v)

  if w == 0:
    import os
    os.system('clear')
    print('\nYou win')
    print('\nThe hidden word:', Word)
    break
        
  if m==0:
    o=o+1
    import os
    os.system('clear')
    print('\nThere is no letter in the string.')
    print('\nYou have already entered the letters:', v)
    if o==8:
      import os
      os.system('clear')
      print('\nThere is no letter in the string.\n |--------\n |     |\n |     |\n |     O\n |    /|\ \n |    / \ \n |\n |\n------------------\nSorry. You were hanged.')
      print('\nThe hidden word:', Word)
      break
