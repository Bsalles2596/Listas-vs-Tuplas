## Listas:

# As listas em Python são estruturas de dados mutáveis, o que significa que seus elementos podem ser alterados, adicionados ou removidos após a criação da lista.
# As listas são definidas usando colchetes [] e seus elementos são separados por vírgulas.
# As listas podem conter diferentes tipos de dados, como números, strings, booleanos, etc.

## Exemplo de uso de uma lista:

frutas = ['maçã', 'banana', 'laranja', 'uva']
print(frutas)  # Saída: ['maçã', 'banana', 'laranja', 'uva']

frutas[1] = 'pêra'  # Alterando um elemento da lista
print(frutas)  # Saída: ['maçã', 'pêra', 'laranja', 'uva']

frutas.append('abacaxi')  # Adicionando um novo elemento à lista
print(frutas)  # Saída: ['maçã', 'pêra', 'laranja', 'uva', 'abacaxi']

frutas.remove('maçã') # Removendo um elemento
print(frutas)  # Saída: ['pêra', 'laranja', 'uva', 'abacaxi']

frutas.sort() # Ordenando a lista
print(frutas)  # Saída: ['abacaxi', 'laranja', 'pêra', 'uva']

## Tuplas:

# As tuplas em Python são estruturas de dados imutáveis, o que significa que seus elementos não podem ser alterados após a criação da tupla.
# As tuplas são definidas usando parênteses () e seus elementos são separados por vírgulas.
# As tuplas também podem conter diferentes tipos de dados, assim como as listas.

## Exemplo de uso de uma tupla:

coordenadas = (10.5, 20.2, 30.7)
print(coordenadas)  # Saída: (10.5, 20.2, 30.7)

## Tentativa de alterar um elemento da tupla
### coordenadas[0] = 15.0  # Erro: 'tuple' object does not support item assignment

### Acessando elementos da tupla
print(coordenadas[0])  # Saída: 10.5
print(coordenadas[1])  # Saída: 20.2
print(coordenadas[2])  # Saída: 30.7

## Outro exemplo de uso de Tuplas:
### Tupla com informações de um aluno e acessar seus elementos:

aluno = ('João', 21, 'Engenharia')

# Acessando elementos da tupla
print(aluno[0])  # Saída: 'João'
print(aluno[1])  # Saída: 21
print(aluno[2])  # Saída: 'Engenharia'

# Tentativa de alterar um elemento da tupla
# aluno[0] = 'Maria'  # Erro: 'tuple' object does not support item assignment


## Algumas diferenças práticas entre listas e tuplas:

# Mutabilidade: As listas são mutáveis, enquanto as tuplas são imutáveis.
# Uso: Listas são usadas quando você precisa de uma estrutura de dados flexível e modificável.
# Tuplas são usadas quando você precisa de uma estrutura de dados estática e imutável.
# Desempenho: As tuplas são, em geral, mais rápidas do que as listas, pois não precisam lidar com a possibilidade de mudanças.
# Uso em funções: Tuplas são comumente usadas como valores de retorno de funções, pois garantem que os valores não serão alterados involuntariamente.

