nome = "Dalila"
idade = 28

saldo = 45.435

dados = {"nome": "Dalila", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))
# Nome: Dalila Idade: 28

print("Nome: {} Idade: {}".format(nome, idade))
# Nome: Dalila Idade: 28

print("Nome: {1} Idade: {0}".format(idade, nome))
# Nome: Dalila Idade: 28

print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
# Nome: Dalila Idade: 28 Nome: Dalila Dalila

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
# Nome: Dalila Idade: 28

print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
# Nome: Dalila Idade: 28 Dalila Dalila 28

print("Nome: {nome} Idade: {idade}".format(**dados))
# Nome: Dalila Idade: 28

print(f"Nome: {nome} Idade: {idade}")
# Nome: Dalila Idade: 28

print(f"Nome: {nome} Idade: {idade} Saldo {saldo:.2f}")
# Nome: Dalila Idade: 28 Saldo 45.44

print(f"Nome: {nome} Idade: {idade} Saldo {saldo:10.1f}")
# Nome: Dalila Idade: 28 Saldo       45.4