# Problema do simpatizante
## OBMEP - o inferno
**Grupo:** Galajo
<br>
**Integrantes:** Gabriela Frajtag, João Pedro da Silva Mariano, Laís Fernanda Medeiros Ruela
<br>
**Instituição:** Ilum - Escola de ciência
<br>
## Introdução
Este repositório apresenta o tabalho final de Algoritmos Genéticos (AG) da equipe Galajo. No notebook em questão, apresentamos, por AG, resoluções de um problema inspirado em provas da Olimpíada Brasileira de Matemática das Escolas Públicas (OBMEP). A OBMEP tem por tradição fazer questões utilizando o ano vigente da prova, sempre com números grandes, como: ..., 2022, 2023, 2024... Pensando em operações matriciais, criamos uma função chamada SIMPATIZAR, aonde queremos achar seu valor máximo para matrizes quadradas. A solução para esse problema usando matrizes até 3x3 é viável por busca em grade (força bruta), porém, quando a matriz é maior ou igual à 4x4 este custo computacional fica gigantesco. Observando uma matriz 4x4, temos 16! ≈ 2.1×10^13 tipos diferentes de matrizes para encontrar o valor máximo da SIMPATIZAR, isso poderia levar cerca de 243 dias em um único núcleo de CPU (assumindo que cada iteração leva 1 µs). Imagine isso para matrizes maiores... Então, nosso objetivo foi aplicar um método de maximização por Algoritmos Genéticos, tentando responder e nos debruçar em algumas perguntas intrínsecas ao problema. Alguns questionamentos não são tão fáceis de serem respondidos, como:
Quais padrões existentes nas matrizes solução? Há alguma solução analítica para esse problema? Quais operadores utilizar para o AG convergir melhor no valor máximo de SIMPATIZAR? 
Há muitos questionamentos, porém, este trabalho discute sobre alguns deles, por exemplo, o que acontece se usarmos tipos diferentes de mutação?

## Estrutura do Repositório

Nesse repositório, há três arquivos:
* README.md (arquivo atual para guiar o usuário)
* AG_Projeto_Final_Galajo.ipynb (notebook jupyter com o Algoritmo Genético)
* funcoes.py (script de Python com as funções usadas no notebook)

### Requisitos
Para a execução correta do projeto, é necessário ter o ambiente configurado com as seguintes bibliotecas:
- **matplotlib:** utilizada para plotar e visualizar de dados 
- **numpy:** utilizada para operações matemáticas e manipulação de arrays.
  
## Teoria 
Distribuindo $n^2$ números distintos ($1,2,3,...n^2$) em uma matriz $n \times n$ 

Criamos uma operação chamada **SIMPATIZAR**.
Dada uma matriz $A$ de tamanho $n \times n$, definimos:

- $P_{linha}(i)$ é o produto de todos os elementos na $i$-ésima linha
- $P_{coluna}(j)$ é o produto de todos os elementos na $j$-ésima coluna

A operação simpatizar é definida como:

$$ S = \sum_{i=1}^n P_{linha}(i) + \sum_{j=1}^n P_{coluna}(j) $$

em que $S$ é o simpatizante.

Chamaremos a matriz de **simpática-rainha** caso, para os números escolhidos, ela **maximize o simpatizante**

Sabendo que a matriz a seguir é uma solução para maximizar a função simpatizante, escolhemos $n = 4$ e vamos usar os números $1,2,3,4$ e organizandos em uma matriz $2 \times 2$. 
Podemos fazer isso da seguinter forma:

$$
A_1 = \begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

Vamos simpatizar a matriz $A_1$:

- $P_{linha}: 1 \cdot 2 + 3 \cdot 4 = 2 + 12 = 14$
- $P_{coluna}: 1 \cdot 3 + 2 \cdot 4 = 3 + 8 = 11$

Logo $$S_{A_1} = 14 + 11 = 25$$

## Conclusão
Pudemos observar após esse estudo que, apesar de alguns operadores se mostrarem melhores que outros, e a combinação de todos eles ter apresentado o melhor resultado final, a diferença entre o simpatizante máximo, a média e a mediana de cada um dos operadores não foi significativamente relevante.
 
Algumas hipóteses foram formuladas para resolver esse impasse. A primeira é que, possivelmente, uma população inicial maior e um maior número de gerações poderiam produzir um resultado melhor e talvez até convergir com mais rapidez. Além disso, outros parâmetros podem ser alterados, como a chance de cruzamento e a chance de mutação.
 
Outra questão é que, ao utilizar o cruzamento ordenado durante o desenvolvimento deste notebook, notamos que ele não estava dando bons resultados e frequentemente caía em máximos locais. Utilizar o cruzamento de ponto simples com correção melhorou esse problema, mas talvez seja interessante testar outros tipos de cruzamento e observar se nosso algoritmo converge mais rapidamente e resulta em melhores valores para o simpatizante.
 
Propomos, portanto, como perspectivas futuras, testar essas hipóteses e utilizar diferentes métodos a fim de verificar se otimizamos nosso algoritmo, além de testá-lo em matrizes com valores de $n$ maiores e observar como o simpatizante se comporta.

## Referências
- [1] Cassar, Daniel. Material Didático do Curso de Redes Neurais e Algoritmos Genéticos. Ilum - Escola de Ciência, 2024.
- [2] NUMPY. Documentação oficial. Disponível em: https://numpy.org/. Acesso em: 03 jun. 2024
- [3] MATPLOTLIB. Documentação oficial. Disponível em: https://matplotlib.org/. Acesso em: 03 jun. 2024.
- [4] PYTHON. Biblioteca Padrão. Itertools - Funções para criar iteradores para iterar sobre dados de maneira eficiente. Disponível em: https://docs.python.org/3/library/itertools.html. Acesso em: 03 jun. 2024.
- [5] OBMEP. Provas Passadas. Disponível em: https://www.obmep.org.br/provas.htm. Acesso em: 03 jun. 2024
