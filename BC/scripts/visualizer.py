import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

def gerar_grafico():
    print("BC: Lendo dados da Silver para visualização...")
    # O Spark salva em parquet, o pandas lê direto
    path = "data/silver/inadimplencia_bc"
    df = pd.read_parquet(path)
    
    # Ordenar por data para o gráfico fazer sentido
    df = df.sort_values("data")

    # Criar o gráfico profissional
    plt.figure(figsize=(12, 6))
    plt.plot(df['data'], df['valor'], marker='o', linestyle='-', color='#003399', label='Taxa de Inadimplência')
    
    plt.title('Evolução da Inadimplência PF - Banco Central do Brasil', fontsize=14)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Taxa (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Salvar o resultado
    os.makedirs("data/gold", exist_ok=True)
    plt.savefig("data/gold/grafico_inadimplencia.png")
    print("✔ Sucesso: Gráfico salvo em data/gold/grafico_inadimplencia.png")

if __name__ == "__main__":
    gerar_grafico()