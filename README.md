# python-lab

Documentação inicial com alguns conceitos básicos
Estudos e documentações sobre Python, utilizados na curso Bach. Tecnologia da Informação - Univesp

## Outras documentações

- [Documentação Pyhon intermediária](mid-python.md)

## Indíce

- [1. Getting started](#1-getting-started)
- [2. Expressões Aritméticas e Operadores](#2-expressões-aritméticas-e-operadores)
- [2.1 Tipos de Dados (Introdução)](#21-tipos-de-dados-introdução)
- [2.2 Funções Utilitárias](#22-funções-utilitárias)
- [2.2.1 Matemática](#221-matemática)
- [3. Expressões Lógicas e Operadores](#3-expressões-lógicas-e-operadores)
- [3.1 Precedência](#31-precedência)
- [4. Variáveis](#4-variáveis)
- [5. Listas, Tuplas](#5-listas-tuplas)
- [5.1 Listas](#51-listas)
- [5.2 Tuplas](#52-tuplas)
- [6. Tipos de Dado](#6-tipos-de-dado)

## 1. Getting started

- Download do VSCode (Visual Studio Code): https://code.visualstudio.com/download

- Baixar extensões do VSCode para trabalhar com Python:

  - Name: Jupyter
    Id: ms-toolsai.jupyter
    Description: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.
    Version: 2023.11.1100101639
    Publisher: Microsoft
    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

  - Name: Pylance
    Id: ms-python.vscode-pylance
    Description: A performant, feature-rich language server for Python in VS Code
    Version: 2023.12.1
    Publisher: Microsoft
    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

  - Name: Python
    Id: ms-python.python
    Description: IntelliSense (Pylance), Linting, Debugging (Python Debugger), code formatting, refactoring, unit tests, and more.
    Version: 2023.22.1
    Publisher: Microsoft
    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python

- Download da versão mais recente do Python para Windows: https://www.python.org/downloads/

## 2. Expressões Aritméticas e Operadores

**Operadores Aritméticos**

| Operadores | Descrição                    |
| ---------- | ---------------------------- |
| `+`        | Adição                       |
| `-`        | Subtração                    |
| `*`        | Multiplicação                |
| `/`        | Divisão                      |
| `//`       | Quociente da divisão inteiro |
| `%`        | Resto da divisão             |
| `**`       | Potência                     |

**Precedência de Operadores**

- Mesma regra da álgebra
- Multiplicação e divisão tem precedência sobre soma e subtração
- Os parênteses (`()`) são usados para modificar a ordem de precedência
  ```python
  >>> 3 + 2 * 2 # 3 + 4 -> 7
  >>> (3 + 2) * 2 # 5 * 2 -> 10
  ```
- Se não há nenhuma precedência entre os operadores, sempre realizar a avaliação da **ESQUERDA** para a **DIREITA**

### 2.1 Tipos de Dados (Introdução)

| Tipo    | Descrição                     |
| ------- | ----------------------------- |
| `int`   | Números inteiros              |
| `float` | Números flutuantes (decimais) |

- Qualquer operação de soma/subtração/multiplicação envolvendo apenas números de natureza `int` irá retornar `int`
- Se ao menos um número for `float` irá retornar `float`
- A divisão de dois números `int` irá retornar um `float`

### 2.2 Strings

- Armazenam objetos que contém uma cadeia de caracteres
- Com ela pode ser feita atribuições e comparções também
- São imutáveis, ou seja, não é possível alterar caracteres isolados de uma string já criada

```python
>>> s = 'abc'
>>> t = 'dfg'
>>> s == t # False
>>> s != t # True
>>> s < t # True -> Pois ele compara a ordem alfabética das strings
>>> s + t # abcdfg
>>> s * 2 # Funciona somente quando um dos operador é inteiro e ele multiplica a string tornando -> abcabc
>>> ch = 'b'
>>> ch in s # True -> Define que o caractere 'ch' contém em 's'
```

- Operadores que não funcionam com strings:

  - `-`, `/`, `//`, `%`, `**`

- Indexação de strings:

  ```python
  >>> nome = 'Ryan'
  >>> nome[0] # Imprime -> R
  >>> nome[2] # Imprime -> a
  >>> nome[-1] # Imprime -> n
  >>> nome[0:2] # Substrings - Imprime -> Ry
  >>> nome[:3] # Substring pegando do inicio até 3 - Imprime -> Rya
  >>> nome[-1:] # Substring indicando o valor final até o final - Imprime -> n
  >>> len(nome) # Imprime -> 4
  ```

### 2.2 Funções Utilitárias

#### 2.2.1 Matemática

| Função  | Descrição                                        |
| ------- | ------------------------------------------------ |
| `abs()` | Retorna o valor absoluto de um número            |
| `min()` | Retorna o valor mínimo um conjunto de valores    |
| `max()` | Retorna o valor máximo de um conjunto de valores |

#### 2.2.2 Strings

| Função                  | Descrição                                                        |
| ----------------------- | ---------------------------------------------------------------- |
| `exemplo.find(s)`       | Retorna o índice que a substring `s` aparece em `exemplo`        |
| `exemplo.count(s)`      | Retorna a frequência em que a substring `s` aparece em `exemplo` |
| `exemplo.replace(p, s)` | Substitui a string `p` pela substring `s` em `exemplo`           |
| `exemplo.capitalize()`  | Substitui o primeiro caractere de `exemplo` em maiúscula         |
| `exemplo.upper()`       | Transforma toda a string de `exemplo` em maiúscula               |
| `exemplo.lower()`       | Transforma toda a string de `exemplo` em minúscula               |
| `exemplo.strip()`       | Remove espaço em branco em excesso                               |

## 3. Expressões Lógicas e Operadores

- Operadores relacionais:

| Operador | Descrição        |
| -------- | ---------------- |
| `==`     | Igual á          |
| `!=`     | Diferente de     |
| `>`      | Maior que        |
| `<`      | Menor que        |
| `>=`     | Maior ou igual á |
| `<=`     | Menor ou igual á |

- Expressões aritméticas possuem precedência sobre ás lógicas:

  ```python
  # Primeiro é resolvido o bloco (2 + 1) antes de ser feita a relação
  >>> 2 + 1 >= 3 # True
  ```

- Operadores lógicos:

| Operador | Descrição                                                            |
| -------- | -------------------------------------------------------------------- |
| `and`    | Operador E                                                           |
| `or`     | Operador OU                                                          |
| `not`    | Negação de uma condição                                              |
| `in`     | Pertence á                                                           |
| `not in` | Não pertence á                                                       |
| `is`     | Identidade - Verifica se um elemento é de um determinado tipo        |
| `not is` | Identidade negada - Verifica se um elemento é de um determinado tipo |

- Exemplos operadores `in` e `not in`:

  ```python
  >>> 4 in [4,3,6,9] # True
  >>> 5 not in (5,16,3,7) # False
  ```

- Exemplos operadores `is` e `not is`:
  ```python
  >>> 4 is not 1 # True
  >>> 5.0 is int(5) # False
  ```

### 3.1 Precedência

- Precedência entre operadores lógicos:

  - `not` -> `or` `and`

- Precedência entre todos os operadores:
  | Parênteses mais internos - `()`
  | Operadores aritméticos - `+ - / * // % **` (Potência `**` tem a maior preferência)
  | Operadores relacionais - `== != > < >= <=`
  | Operadores lógicos - `and or not`
  °

## 4. Variáveis

```python
>>> x = 3
>>> nome = 'Ryan'
```

- Detalhe para o operador de atribuição: `=`
- Formato geral: `<variável> = <expressão>`
- Definição de nome de `a-z`, `A-Z`, underscore (`_`) e exeto para os primeiros caracteres números de `0-9`

**Palavras Reservadas**

```python
and	as	assert	break	class	continue
def	del	elif	else	except	exec
finally	for	from	global	if	import
in	is	lambda	nonlocal	not	or
pass	raise	return	try	while	with
yield	True	False	None
```

## 5. Listas, Tuplas

### 5.1 Listas

- Uma lista é representado por uma sequência de objetos
- Estes objetos podem ser de diferentes tipos tais como: `strings`, `numbers`, `floats`, etc.
- Listas são mutáveis, ao contrário das `strings`

```python
>>> pets = ['cão', 'gato', 'peixe']
>>> l = [1, 'ab', [], [1, 2]] # Lista heterogenea
```

**Operadores**

```python
>>> pets[0] # retorna a string 'cão'
>>> l[-1] # retorna o array [1, 2]
```

Outros operadores: `in`, `not in`, `+`, `*`, `len()`, `min()`, `max()`, `sum()`

### 5.2 Tuplas

- Tuplas são iguais as listas porém são imutáveis
- Sua criação deve ser usada o parênteses (`()`) ao inves dos colchetes (`[]`)

```python
>>> dias = ('seg', 'ter', 'qua')
```

### Funções utilitárias

| Função               | Descrição                                             |
| -------------------- | ----------------------------------------------------- |
| `pets.append('cão')` | Inclui um elemento ao final da lista                  |
| `pets.count()`       | Retorna quantos elementos a lista possui              |
| `pets.index(2)`      | Retonar o elemento de uma determinada posição passada |
| `pets.insert(1)`     | Inclui um elemento em uma determinada posição passada |

## 6. Tipos de Dado

- Variáveis em Python não possuem um tipo declaradamente, elas apontam temporariamente para um objeto na memória onde está armazenado o tipo e o valor dos dados
- Cada dado é armazenado na memória no formato de objetos
- Cada objeto possui um tipo e um valor
- Função para indetificar um tipo de uma variável
  ```python
  >>> type(3) # retorna 'int'
  ```

Para tipos inteiros pode ser armazenado valores consideravelmente altos (dependendo da memória do computador), já para `float's` a um limite de até 64 bits

```python
>>> 2**1024 # retorna 11781361728633673532 ... 53056587776
>>> 2.0**1024 # retorna ERRO
```

Em `float's` também os valores são aproximados, e normalmente a depender do tamanho do resultado é usado notação ciêntifica para expressa-lôs

**Conversão Implícita**

- Se em uma expressão houver operandos de diferentes tipos o python irá converter para o que contém os outros
  - `bool -> int -> float`

```python
>>> True + 5 # retorna 6
>>> 3 + 0.35 # retorna 3.35
```

**Coneversão Explícita**

- Pode ser usado construtores para que seja feita a conversão te tipos explícitamente

```python
>>> int(3.4) # retorna 3
>>> float(4) # retorna 4.0
>>> str(2.74) # retorna '2.74'
```

## 7. Biblioteca Padrão Python (std)

- A biblioteca padrão do python contém muitas outras funções úteis no dia a dia
- +200 de módulos formam esta lib

Exemplo de apliações que possuem módulos predefinidos:

- Programação para rede de computadores
- Programação web
- Desenvolvimento de GUI
- Banco de dados
- Funções matemáticas
- Gerador de números pseudoaleatórios

**Módulo math**

```python
>>> import math # import da biblioteca math
>>> math.sqrt(4) # retorna 2.0
>>> math.log(8, 2) # retorna 3.0
```

- Alguma funções deste módulo

| Função         | Descrição                           |
| -------------- | ----------------------------------- |
| `sqrt(x)`      | Raíz quadrada de um número          |
| `ceil(x)`      | Arredonda para o menor inteiro >= x |
| `floor(x)`     | Arredonda para o maior inteiro <= x |
| `cos(x)`       | Faz o cálculo do cosseno            |
| `sen(x)`       | Faz o cálculo do seno               |
| `log(x, base)` | Faz o log de 'x' na base 'base'     |
| `pi`           | Constante PI                        |
| `e`            | Constante e                         |

**Módulo fraction**

- É utilizada para representar frações e trabalhar com números racionais

```python
>>> import fractions
>>> a = fractions.Fraction(1, 2)
>>> b = fractions.Fraction(3, 4)
>>> a + b # retorna Fraction()
```

- Algumas vantagens deste módulo é que ele permite exibir valores muito maiores comparado com o tipo `float`
- Por outro lado o tipo `float` é mais rápido em comparação com o `fractions`
