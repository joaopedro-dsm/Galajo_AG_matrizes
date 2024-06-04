# Galajo_AG_matrizes

**Grupo:** Galajo
<br>
**Integrantes:** Gabriela Frajtag, João Pedro da Silva Mariano, Laís Fernanda Medeiros Ruela
<br>
**Instituição:** Ilum - Escola de ciência
<br>
## Introdução
Este repositório apresenta o tabalho final de Algorítimos Genéticos (AG), da equipe Galajo. No notebook em questão, apresentamos, por AG, resoluções de um problema inspirado em provas da Olimpíada Brasileira de Matemática das Escolas Públicas (OBEMEP). A OBEMEP tem por tradição fazer questões utilizando o ano vigente da prova, sempre com números grandes, como: ..., 2022, 2023, 2024... Pensando em operações matriciais, criamos uma função chamada SIMPATIZAR, aonde queremos achar seu valor máximo para matrizes quadradas. A solução para esse problema usando matrizes até 3x3 é viável por busca em grade (força bruta), porém, quando a matriz é maior ou igual à 4x4 este custo computacional fica gigantesco. Observando uma matriz 4x4, temos 16! ≈ 2.1×10^13 tipos diferentes de matrizes para encontrar o valor máximo da SIMPATIZAR, isso poderia levar cerca de 243 dias em um único núcleo de CPU (assumindo que cada iteração leva 1 µs). Imagine isso para matrizes maiores... Então, nosso objetivo foi aplicar um método de maximização por Algorítimos Genéticos, tentando responder e nos debruçar em algumas perguntas intrínsecas ao problema. Alguns questionamentos não são tão fáceis de serem respondidos, como:
Quais padrões existentes nas matrizes solução? Há alguma solução analítica para esse problema? Quais operadores utilizar para o AG convergir melhor no valor máximo de SIMPATIZAR? 
Há muitos questionamentos, porém, este trabalho discute sobre alguns deles, por exemplo, o que acontece se usarmos tipos diferentes de mutação?

## Estrutura do Repositório

Nesse repositório, há três arquivos:
* README.md (arquivo atual para guiar o usuário)
* (?).ipynb (notebook jupyter com o Algorítimo Genético)
* funcoes.py (script de Python com as funções usadas no notebook)

### Requisitos
Para a execução correta do projeto, é necessário ter o ambiente configurado com as seguintes bibliotecas:
- **matplotlib:** utilizada para plotar e visualizar de dados 
- **numpy:** utilizada para operações matemáticas e manipulação de arrays.
  
## Teoria 
Distribuindo $n^2$ números distintos ($1,2,3,...n^2$) em uma matriz $n \times n$ 

Criamos uma operação chamada **SIMPATIZAR**.
Dada uma matriz $A$ de tamanho $n \times n$, definimos:

* $ P_{linha}(i) $ é o produto de todos os elementos na $i$-ésima linha
* $ P_{coluna}(i) $ é o produto de todos os elementos na $i$-ésima linha

A operação simpatizar é definida como:

$$ S = \sum_{i=1}^n P_{linha}(i) + \sum_{j=1}^n P_{coluna}(j) $$

em que $S$ é o simpatizante.

Chamaremos a matriz de **simpática-rainha** caso, para os números escolhidos, ela **maximize o simpatizante**

Sabendo que a matriz a seguir é uma solução para maximizar a função simpatizante, escolhemos $n = 4$ e vamos usar os números $1,2,3,4$ e organizandos em uma matriz $2 \times 2$. 
Podemos fazer isso da seguinter forma:

$$ A_1 = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} $$

Vamos simpatizar a matriz $A_1$: <br>
$P_{linha}$: $1 \cdot2 + 3 \cdot4 = 2 + 12 = 14$ <br>
$P_{coluna}$: $1 \cdot3 + 2 \cdot4 = 3 + 8 = 11$

Logo $S_{A_1} = 14 + 11 = 25$

## Conclusão


## Referências
[1] Cassar, Daniel. Material Didático do Curso de Redes Neurais e Algoritimos Genéticos. Ilum - Escola de Ciência, 2024.
[2] NUMPY. Documentação oficial. Disponível em: https://numpy.org/. Acesso em: 03 jun. 2024
[3] MATPLOTLIB. Documentação oficial. Disponível em: https://matplotlib.org/. Acesso em: 03 jun. 2024.
[4] PYTHON. Biblioteca Padrão. Itertools - Funções para criar iteradores para iterar sobre dados de maneira eficiente. Disponível em: https://docs.python.org/3/library/itertools.html. Acesso em: 03 jun. 2024.
[5] OBMEP. Provas Passadas. Disponível em: https://www.obmep.org.br/provas.htm. Acesso em: 03 jun. 2024
