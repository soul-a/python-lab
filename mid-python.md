# Mid Python

Documentação intermediária python, com o básico de algoritmos e programação usando a linguagem python com a IDE `VSCode`

## Sumário

## Getting started

Execução de programas python através do terminal:

```bash
python3 arq.py
```

## Funções de interação com usuário

Funções tais como, `print()`, `input()`, `eval()`

1. `print()`

A função print() é usada para imprimir um valor que está sendo indicado em seus argumentos

```python
print('Ola mundo') # Retorna no console 'Ola mundo'
print(445) # Retorna no console 445
```

É possível passar mais de um valor para a impressão

```python
horas = 13
print('Agora são', horas, 'horas') # Retonra no console 'Agora são 13 horas'
```

A função também possui outros parâmetros, tais como:

- `sep`: Indica como será separado os valores passados entre as vírgulas, por padrão é um espaço em branco
- `end`: Define como vai ser o final da impressão

```python
dia = 8
mes = 2
ano = 2002
python(dia, mes, ano, sep='/', end='.\n') # Retorna no console '08/02/2002.'
```

2. `input()`

A função `input()` aguarda o usuário digital algo no shell
Este comando sempre irá retornar uma string

```python
nomePessoa = input('Digite o nome da pessoa:') # nomePessoa recebe o valor digitado aqui
```

3. `eval()`

Possibilida que você use uma `string` como uma expressão literal usando esta função `eval()`

```python
eval('3 < 4') # Retorna True
eval('10') # Retorna 10
```

## Definição de funções

- As funções permitem modularizar etapas melhorando a manutenção do programa com o tempo
- As funções podem ou não ter retorno sendo apenas procedural (Que executam e não indicam valor de retorno)
- É importante sempre definir a função antes de executal na odem sequêncial de cima para baixo

Definição do formato de uma função:

```python
def <nome_da_função> (<parametros>):
  <intruções>
  # ...
  return <valor> # opcional, pois existem funções que não possuim valor
```

Exemplos de uma função matemática representado no python:

f(x) = x² + 1

```python
def f (x):
  result = x**2 + 1
  return result
```

Exemplo de função com vários parâmetros:

```python
def aplicar_juros(valor, juros):
  result = valor * (1 + (juros / 100))
  return result
```

## Documentação de programas

- Permite que outros desenvolvedores entendam a regra de negócio descrita nos processos
- Documentar também ajuda usuários e entender o que o programa faz

Comentarios são representados através de `#` em python, no momento de compilação os comentarios são ignorados, servindo apenas como auxilio no código

```python
def f (x):
  result = x**2 + 1 # Faz o calculo da função e armazena em result
  return result # Retorna o resultado da função
```

Caso a documentação ocupe várias linha é possível fazer unando o três aspas simples ou duplas `''' '''`

```python
'''
Chama a saída do console para apresentar
em tela a palabra 'UNIVESP'
'''
print('UNIVESP')
```

É importante saber balancear os comentários, usando apenas quando necessário para que não haja comentarios de mais ou de menos

Podemos balancear da seguinte forma:

- Usar variáveis e instruções com nomes mais significativos
- Documentar trechos de códigos mais críticos

**Docstring**

A documentação de funções também é importante para isso existe do `docstring` usado para documentar funções, podendo serem chamadas através da função `help()`

Exemplo de como documentar um função:

```python
def f (x):
  'Função que calcula sua IM em função de X, sendo IM = x² + 1'
  result = x**2 + 1
  return result
```

Quando chamarmos `help(f)` irá nos retornar está primeira linha explicativa

## Estrutura de condição de uma ou duas vias

- Permitem escolher um conjunto de ações
- Blocos são delimitados por identação
- As condições são representadas por expressões lógicas ou relacionais
- Podem conter um, duas ou mais vias

**Seleção de um via**

- Tem o objetivo de testar um condição antes de continuar

```python
if(condicao):
  # TODO
# Continue
```

**Seleção de duas vias**

- Dois blocos alternativos dependendo da condição

```python
if(condicao):
  # TODO
else:
  # TODO
# Continue
```

**Seleção de três vias ou mais**

- Possibilidade de testar diversas condições com blocos para cada uma delas

```python
if(condicao1):
  #todo
elif(condicao2):
  #todo
elif(condicao3):
  #todo
else
  #todo
#Continue
```
