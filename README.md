![Captura de tela 2024-04-17 123206](https://github.com/DalilaDeveloperMobile/Conhecendo-Linguagem-Python/assets/29806802/83eba503-c094-4431-b85f-e7b4cc9d92de)
### Passos Iniciais Realizados Nesse Bootcamp Python AI Backend Developer. [dio_me](https://www.dio.me/)
### ✅ Manipulando Strings Com Python.

### <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> Conhecendo métodos úteis da classe string:

```
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
```
### <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> Interpolação de variáveis:
```
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
```
### <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> Fatiamento de string:
```
nome = "Guilherme Arthur de Carvalho"

print(nome[0])
# G

print(nome[-2])
# h

print(nome[:9])
# Guilherme

print(nome[10:])
# Arthur de Carvalho

print(nome[10:16])
# Arthur

print(nome[10:16:2])
# Atu

print(nome[:])
# Guilherme Arthur de Carvalho

print(nome[::-1])
# ohlavraC ed ruhtrA emrehliuG
```
### <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> String múltiplas linhas:
```
nome = "Dalila"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
      Essa mensagem tem diferentes recuos.  
"""

print(mensagem)

# Result:

#    Olá meu nome é Dalila,
# Eu estou aprendendo Python.
#      Essa mensagem tem diferentes recuos. 

print(
    """
       ============== MENU ==============

       1 - Depositar
       2 - Sacar
       0 - Sair

       ==================================
"""
)

# Result 

 #      ============== MENU ==============

 #      1 - Depositar
 #      2 - Sacar
 #      0 - Sair

 #      ==================================
```
<h3 align="center"> Made with <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> by Dalila...</h3>
<div align="center"  style="display: inline-block">
  <a href="https://www.linkedin.com/in/dalila-cust%C3%B3dio-046076181/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
  <a href = "mailto:dalila.dalila70@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://instagram.com/dalila.dalila70" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
  <a target="_blank" href="https://api.whatsapp.com/send?phone=5588997138541"><img  alt="Whatsapp" width="117px" src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a> 
</div>
