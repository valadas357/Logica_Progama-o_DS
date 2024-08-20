#tipos de concatenação
#Concatenação com sinal +
num = input('Digite seu nome: ')
#não é pssivel concatenar numero inteiro usando este metodo, a menos que 
#converta o numero inteiro em uma string
print('ola,'+ str(num) +'. Seja bem vindo!')
print(type(num))

#concatenação com ,
print('o numero digitado é:',num)

#concatenação com fstring f
print(f'O numero digitado é: {num} usando a concatenação "f"')

div = num / 3
#usando format para formatção numérica
#limitando a quantidade de casas devimais
print(f'O resultado da divisão é: {div:.5f}')