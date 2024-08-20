nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
telefone = input('Digite seu telefone: ')

alcool = input('Quanto de alcool foi abastecido?: ')
gasolina = input('Quanto de gasolina foi abastecido?: ')
captotal = 50
distancia = 32
dist = input('digite quantas vezes foi e voltou do trabalho: ')
valora = input('Qual o valor do alcool?: ')
valorb = input('Qual o valor da gasolina?: ')
div1 = dist * distancia
div2 = valora * alcool
div3 = valorb * gasolina

print('Seu nome é: ',nome)
print('Seu email é: ',email)
print('Seu telefone é: ',telefone)
print('A distância percorrida foi: ',div1)
print('O preço a pagar pelo alcool é: ',div2)
print('O valor a pagar pela gasolina é: ',div3)
autoa = div1 / 12
autob = div1 / 14
#valor gasto na semana
gastoa = div2 * 5

