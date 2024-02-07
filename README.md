# python-lab

Estudos e documentações sobre Python, utilizados na curso Bach. Tecnologia da Informação - Univesp

## Indíce

- [1. Getting started](#1-getting-started)
- [2. Expressões Aritméticas e Operadores](#2-expressões-aritméticas-e-operadores)
- [2.1 Tipos de Dados (Introdução)](#21-tipos-de-dados-introdução)
- [2.2 Funções Utilitárias](#22-funções-utilitárias)
- [2.2.1 Matemática](#221-matemática)
- [3. Expressões Lógicas e Operadores](#3-expressões-lógicas-e-operadores)
- [3.1 Precedência](#31-precedência)

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

### 2.2 Funções Utilitárias

#### 2.2.1 Matemática

| Função  | Descrição                                        |
| ------- | ------------------------------------------------ |
| `abs()` | Retorna o valor absoluto de um número            |
| `min()` | Retorna o valor mínimo um conjunto de valores    |
| `max()` | Retorna o valor máximo de um conjunto de valores |

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
