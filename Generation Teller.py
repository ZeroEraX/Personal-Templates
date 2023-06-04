##### Find Out Which Generation You Are #####
import sys

Bday = int(input('What year were you born in: '))
print()
if Bday >= 1925 and Bday <= 1946:
  print('You are a Traditionalist')
  print()
elif Bday >= 1947 and Bday <= 1964:
  print('Baby Boomer Baby yeahhh')
  print()
elif Bday >= 1965 and Bday <= 1981:
  print('X Gen huh')
  print()
elif Bday >= 1982 and Bday <= 1995:
  print('''Of course you're a millenial''')
  print()
elif Bday >= 1996 and Bday <= 2015:
  print('''You're in last place Gen Z''')
  print()
else:
  print('Hmmmmm Youre either too old, or too young, goodbye.')
  print()
sys.exit()
