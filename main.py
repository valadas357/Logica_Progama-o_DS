print("ola mundo")
'''
nome = 'Valadao'
idade = 17
peso = 80.3
altura = 1.70
instrutor = True

# visualizando os tipos de dados
print(type(nome))
print(type(idade))
print(type(peso))
print(type(altura))
print(type(instrutor))
'''
#FIXME: Entrada de dados
sobrenome = input("digite o seu sobrenome: ")
print(type(sobrenome))
#convertendo o valor do input
idade = input("digite sua idade: ")
idade = int(idade)
print(type(idade))

ano = int(input("em qual ano estamos: "))
print(type(ano))
if ano > 2024:
    print('dentro do if')