'''
receber nome, cpf, data de nascimento
imprima os dados e os tipos ja convertidos
'''
nome = input('Digite seu nome: ')
cpf = input('Digite seu cpf: ')
cpf = int(cpf)
dtn = input('Digite a data do seu nascimento: ')
dtn = int(dtn)


print('seu nome e:',nome)
print('seu cpf e:',cpf)
print('sua data de nascimento e:',dtn)
print(type(nome))
print(type(cpf))
print(type(dtn))