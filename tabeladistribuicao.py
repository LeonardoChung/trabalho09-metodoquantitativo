import numpy as np
import pandas as pd

# lê o dataset
df = pd.read_csv("Netflix Engagement Dataset.csv")

def tabela_distributiva(coluna):
    if df[coluna].dtype == 'object': # String
        freq = df[coluna].value_counts() # Contagem dos valores
        porcentagem = df[coluna].value_counts(normalize=True) * 100 # (contagem ÷ total) × 100
        tabela = pd.DataFrame({'frequência': freq, 'percentual (%)': porcentagem})
        
    else:    
        n = len(df[coluna])
        A = round(max(df[coluna]) - min(df[coluna]))  # Amplitude = maior - menor
        i = round(1 + 3.3 * np.log10(n))              # Quantidade de classes
        h = round(A / i)                              # Amplitude classe
    
        menor = min(df[coluna])
        intervalos = []
        fi = []
        xi = []
    
        while menor <= max(df[coluna]):
            maior = menor + h
            intervalo = f"{menor} - {maior}"  # Intervalos
            intervalos.append(intervalo)
            freq = len(df[(df[coluna] >= menor) & (df[coluna] < maior)])
            fi.append(freq) # Frequência
            xi.append((menor + maior) / 2) # Ponto médio 
            menor = maior
    
        Fi = np.cumsum(fi) # Frequência acumulada
    
        # Gera a tabela
        tabela = pd.DataFrame(
            data= zip(intervalos, fi, xi, Fi),
            columns=["intervalo", "frequência", "ponto médio", "frequência acumulada"]
            )
    print(tabela)

# testando
coluna = 'Promotional Offers Used'
tabela_distributiva(coluna)
