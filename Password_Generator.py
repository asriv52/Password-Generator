import random


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main
special = ['!', '@', '#', '$','%', '&', '*']

uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
special1= special[random.randint(1,7)]
special2= special[random.randint(1,7)]

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + special1 + special2
password = shuffle(password)

#Ouput
print(password)
