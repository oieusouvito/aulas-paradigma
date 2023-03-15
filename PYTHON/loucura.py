a=1
b=3
c=2
lista = [a,b,c,4,5,6]

#Fazendo na mão
soma = 0
contador = 0
for x in lista:
    soma = soma + x
    contador = contador + 1
media_bruta = soma/contador
soma1 = 0
for x in lista:
    soma1 = soma1 + (x-media_bruta)**2 
desvio = (soma1/contador)**(1/2)

#Usando bibliotecas
soma_facil = sum(lista)
N = len(lista)
media_facil = soma_facil/N
soma2 = 0
for x in lista:
    soma2 += (x-media_facil)**2
desvio2 = (soma2/N)**(1/2) 

#prints
print('======================================')
print("Contas feitas com o uso de bibliotecas")
print(f'Soma: {soma_facil}')
print(f'Tamanho da lista: {N}')
print(f'Media: {media_facil}')
print(f'Desvio padrão: {desvio2}')
print('======================================')
print('Contas feitas sem o uso de bibliotecas')
print(f'Soma: {soma}')
print(f'Contador: {contador}')
print(f'Média: {media_bruta}')
print(f'Desvio padrão: {desvio}')

#criando objetos
def mean(valores):
    return(sum(valores)/len(valores))

def padrao(valores):
    a = mean(valores)
    soma2 = 0
    for x in valores:
        soma2 += (x-media_facil)**2
        desvio2 = (soma2/N)**(1/2)
    return desvio  

#Usando objetos
media5 = mean(lista)
print(media5)
c = padrao(lista)
print(c)
