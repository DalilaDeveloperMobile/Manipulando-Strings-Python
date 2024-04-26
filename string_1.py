nome = "daLilA"

print(nome.upper()) # Result: DALILA.
print(nome.lower()) # Result: dalila.
print(nome.title()) # Result: Dalila.

texto = "  Bem Vindos!   "

print("." + texto + ".") # Result: .  Bem Vindos!   .
print("." + texto.strip() + ".") # Result: .Bem Vindos!.
print("." + texto.rstrip() + ".") # Result: .  Bem Vindos!.
print("." + texto.lstrip() + ".") # Result: .Bem Vindos!   .

menu = "Python"

print('####' + menu + "####") # Result: ####Python####
print(menu.center(14)) # Result:    Python    
print(menu.center(14,'#')) # Result: ####Python####
print("-".join(menu)) # Result: P-y-t-h-o-n