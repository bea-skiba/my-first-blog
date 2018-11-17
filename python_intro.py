print('Hello, Django girls!') #to jest komentarz
if 2 > 2:
    print('To działa!')
else:
    print('bzdura')

name="Beata"
if name=="Ola":
    print("Hey, Ola")
if name=="Ala":
    print("Ala")
else:
    print("hello Beata")

def hi(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')

hi("Sonja")

def hello(imie):
    print('Hej ' + imie + '!')

hello("Rachel")

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
print(dziewczyny)

def powitanie(imie):
    print('Witaj ' + imie + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Bea']
for imie in dziewczyny:
    powitanie(imie)
    print('Kolejna dziewczyna')

for i in range(1, 6):
    print(i)
