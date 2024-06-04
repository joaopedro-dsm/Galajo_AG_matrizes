###############################################################################
#                           Problema do Simpatizante                          #
###############################################################################

# as funções escritas aqui foram baseadas nas funções disponibilizadas por Daniel Cassar

import random
import numpy as np

# função para criar matriz
def cria_candidato(n):
    """Cria um indivíduo (matriz de ordem n) para o problema dos simpatizantes

    Args:
      n: inteiro que representa a ordem das matrizes
    """
    # criando uma array de numeros de 1 até n*n
    array_numeros = np.arange(1, n*n + 1)
    
    # misturando os numeros
    np.random.shuffle(array_numeros)
    
    # criando a matriz quadrada com os numeros misturados
    matriz = array_numeros.reshape(n, n)
    
    return matriz

# função para criar a população de candidatos
def populacao(tamanho, n):
    """Cria uma população para o problema das matrizes

    Args:
      tamanho: tamanho da população
      n: inteiro que representa a ordem das matrizes
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato(n))
    return populacao

# cálculo da função objetivo (o próprio simpatizante)
def fitness(matriz):
    """
    Calcula o fitness (simpatizante) de uma matriz.

    Args:
      matriz: matriz para a qual o fitness será calculado.

    Returns:
      simpatizante: valor do simpatizante para a matriz.
    """
    matriz = np.array(matriz)  # Converte a matriz para um array NumPy, se já não for
    ordem_matriz = len(matriz)
    produto_linhas = 0
    produto_colunas = 0
    
    for i in range(ordem_matriz):
        produto_linha = np.prod(matriz[i])
        produto_linhas += produto_linha
        
    for j in range(ordem_matriz):
        produto_coluna = np.prod(matriz[:, j])
        produto_colunas += produto_coluna
        
    simpatizante = produto_linhas + produto_colunas
    return simpatizante

# função que calcula o fitness de uma população
def calcular_fitness_populacao(populacao):
    """
    Calcula o fitness (simpatizante) para cada indivíduo em uma população.

    Args:
      populacao: uma lista de matrizes, onde cada matriz representa um indivíduo na população.

    Returns:
      fitness_values: uma lista de valores de fitness correspondentes a cada matriz na população.
    """
    fitness_values = []
    for individuo in populacao:
        fitness_values.append(fitness(individuo))
    return fitness_values

###############################################################################
#                                   Seleção                                   #
###############################################################################

def selecao_torneio_max(populacao, fitness_vals, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    maximização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si
    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(list(enumerate(populacao)), tamanho_torneio)
        fitness_sorteados = [fitness_vals[indice] for indice, _ in sorteados]
        max_fitness = max(fitness_sorteados)
        indice_max_fitness = fitness_sorteados.index(max_fitness)
        selecionados.append(sorteados[indice_max_fitness][1])

    return selecionados

###############################################################################
#                                  Cruzamento                                 #
###############################################################################

def cruzamento_ordenado(pai, mae, chance_de_cruzamento):
    """
    Realiza o cruzamento ordenado entre dois indivíduos (matrizes) para gerar dois novos filhos.

    Args:
      pai: matriz representando o pai.
      mae: matriz representando a mãe.
      chance_de_cruzamento: probabilidade de ocorrer o cruzamento.

    Returns:
      Dois novos indivíduos (matrizes) resultantes do cruzamento, ou os pais originais se o cruzamento não ocorrer.
    """
    if random.random() < chance_de_cruzamento:
        
        # transformando os indivíduos em listas unidimensionais
        pai_lista = pai.reshape(-1).tolist()
        mae_lista = mae.reshape(-1).tolist()
        tamanho_individuo = len(mae_lista)
        
        # pontos de corte
        corte1 = random.randint(0, tamanho_individuo - 2)
        corte2 = random.randint(corte1+1, tamanho_individuo)

        # filho1
        filho1 = [None] * tamanho_individuo
        filho1[corte1:corte2] = mae_lista[corte1:corte2]
        posicao = corte2
        index = corte2 % tamanho_individuo
        while len([gene for gene in filho1 if gene is None]) > 0: #continua até que não haja mais None valores nos filhos
            if pai_lista[posicao % tamanho_individuo] not in filho1:
                filho1[index] = pai_lista[posicao % tamanho_individuo]
                index += 1
            posicao += 1
            index %= tamanho_individuo
        
        # filho2 
        filho2 = [None] * tamanho_individuo
        filho2[corte1:corte2] = pai_lista[corte1:corte2]
        posicao = corte2
        index = corte2 % tamanho_individuo
        while len([gene for gene in filho2 if gene is None]) > 0:
            if mae_lista[posicao % tamanho_individuo] not in filho2:
                filho2[index] = mae_lista[posicao % tamanho_individuo]
                index += 1
            posicao += 1
            index %= tamanho_individuo
        
        # reshapando os filhos
        filho1 = np.array(filho1).reshape(pai.shape)
        filho2 = np.array(filho2).reshape(mae.shape)

        return filho1, filho2
    else:
        return pai, mae
    
    
    
def ponto_simples_correcao(pai, mae, chance_de_cruzamento):
    """
    Função modificada da criada pelo ChatGPT
    
    Realiza o cruzamento de ponto simples entre dois indivíduos (matrizes) e corrige os filhos para garantir que
    todos os números sejam únicos, ou seja, os indivíduos sejam válidos.

    Args:
      pai: matriz representando o primeiro pai.
      mae: matriz representando a primeira mãe.
      chance_de_cruzamento: probabilidade de ocorrer o cruzamento.

    Returns:
      Dois novos indivíduos (matrizes) resultantes do cruzamento e correção, ou os pais originais se o cruzamento não ocorrer.
    """
    n = len(pai)
    if random.random() < chance_de_cruzamento:
        # Transformando os indivíduos em listas unidimensionais
        pai_lista = pai.flatten().tolist()
        mae_lista = mae.flatten().tolist()
        tamanho_individuo = len(pai_lista)
        
        # Ponto de corte
        ponto_corte = random.randint(1, tamanho_individuo - 2)
        
        # Filhos
        filho1_flat = pai_lista[:ponto_corte] + mae_lista[ponto_corte:]
        filho2_flat = mae_lista[:ponto_corte] + pai_lista[ponto_corte:]
        
        # Função de correção de indivíduo
        def corrigir_individuo(individuo_flat, n):
            todos_numeros = set(range(1, n * n + 1))
            unico, contagem = np.unique(individuo_flat, return_counts=True)
            faltando = list(todos_numeros - set(unico))
            
            repetidos = unico[contagem > 1]
            for numero in repetidos:
                indices_repetidos = np.where(individuo_flat == numero)[0]
                for i in range(1, len(indices_repetidos)):
                    individuo_flat[indices_repetidos[i]] = faltando.pop(0)
            
            return individuo_flat.reshape((n, n))
        
        # Convertendo de volta para np.array e corrigindo
        filho1_flat = np.array(filho1_flat)
        filho2_flat = np.array(filho2_flat)
        filho1 = corrigir_individuo(filho1_flat, n)
        filho2 = corrigir_individuo(filho2_flat, n)
        
        return filho1, filho2
    else:
        return pai, mae


###############################################################################
#                                   Mutação                                   #
###############################################################################

def mutacao_troca(populacao, chance_de_mutacao):
    """
    Realiza a mutação de troca em cada indivíduo da população com uma certa chance.

    Args:
      populacao: uma lista de matrizes, onde cada matriz representa um indivíduo na população.
      chance_de_mutacao: probabilidade de ocorrer uma mutação em um indivíduo.

    Returns:
      A população com os indivíduos possivelmente mutados.
    """
    for individuo in populacao:
        
        # transformar o individuo em uma lista unidimensional
        individuo_lista = individuo.reshape(-1).tolist()
        
        if random.random() < chance_de_mutacao:
            gene1 = random.randint(0, len(individuo_lista) -1)
            gene2 = random.randint(0, len(individuo_lista) -1)
                                   
            while gene1 == gene2:
                gene1 = random.randint(0, len(individuo_lista) -1)
                gene2 = random.randint(0, len(individuo_lista) -1)
            
            individuo_lista[gene1], individuo_lista[gene2] = individuo_lista[gene2], individuo_lista[gene1]
        
            # reshapando o indiviuo mutado                              
            individuo = np.array(individuo_lista).reshape(individuo.shape)                           
        

def mutacao_troca2(populacao, chance_de_mutacao):
    """
    Realiza a mutação de troca em cada gene de cada indivíduo da população com uma certa chance.

    Args:
      populacao: uma lista de matrizes, onde cada matriz representa um indivíduo na população.
      chance_de_mutacao: probabilidade de ocorrer uma mutação em um gene de um indivíduo.

    Returns:
      A população com os indivíduos com genes possivelmente mutados.
    """
    
    for individuo in populacao:
        
        # transformar o individuo em uma lista unidimensional
        individuo_lista = individuo.reshape(-1).tolist()
        tamanho_individuo = len(individuo_lista)
    
        for i in range(tamanho_individuo):
            if random.random() < chance_de_mutacao:
                x = random.randint(0, tamanho_individuo-1)
             
                while i == x:
                    x = random.randint(0, tamanho_individuo-1)   
            
                individuo_lista[x], individuo_lista[i] = individuo_lista[i], individuo_lista[x]
        
        individuo = np.array(individuo_lista).reshape(individuo.shape)  
                
        
def mutacao_permuta_linhas(populacao, chance_de_mutacao):
    """
    Realiza a mutação de permutação entre linhas em cada indivíduo da população com uma certa chance.

    Args:
      populacao: uma lista de matrizes, onde cada matriz representa um indivíduo na população.
      chance_de_mutacao: probabilidade de ocorrer uma mutação de permutação entre linhas em um indivíduo.

    Returns:
      A população com os indivíduos possivelmente mutados.
    """
    
    for individuo in populacao:
        # transformando a matriz em uma lista mas mantendo a ordem
        individuo_lista = individuo.tolist()
        
        if random.random() < chance_de_mutacao:
            
            gene1 = random.randint(0, len(individuo_lista) -1)
            gene2 = random.randint(0, len(individuo_lista) -1)
                                   
            while gene1 == gene2:
                gene1 = random.randint(0, len(individuo_lista) -1)
                gene2 = random.randint(0, len(individuo_lista) -1)
                                       
            individuo_lista[gene1], individuo_lista[gene2] = individuo_lista[gene2], individuo_lista[gene1]
            individuo = np.array(individuo_lista)
            

def mutacao_inverte_linhas(populacao, chance_de_mutacao):
    """
    Realiza a mutação de inversão de linhas ([1, 2, 3] vira [3, 2, 1]) em cada indivíduo da população com uma certa chance.

    Args:
      populacao: uma lista de matrizes, onde cada matriz representa um indivíduo na população.
      chance_de_mutacao: probabilidade de ocorrer uma mutação de inversão de linhas em um indivíduo.

    Returns:
      A população com os indivíduos possivelmente mutados.
    """
    
    for individuo in populacao:
        
        # transformando a matriz em uma lista mas mantendo a ordem
        individuo_lista = individuo.tolist()
        
        if random.random() < chance_de_mutacao:
            
            gene = random.randint(0, len(individuo_lista) -1)
            individuo_lista[gene] = individuo_lista[gene][::-1]
        
        individuo = np.array(individuo_lista)