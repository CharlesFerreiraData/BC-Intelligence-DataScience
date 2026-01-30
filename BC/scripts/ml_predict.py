import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

def treinar_e_prever():
    # Lê a camada Silver que o Spark gerou
    df = pd.read_parquet("data/silver/inadimplencia_bc")
    df = df.sort_values("data")
    
    # Prepara os dados: Transforma data em número para o modelo entender
    df['data_ordinal'] = pd.to_datetime(df['data']).map(pd.Timestamp.toordinal)
    X = df[['data_ordinal']].values
    y = df['valor'].values
    
    # Treina o modelo matemático
    model = LinearRegression()
    model.fit(X, y)
    
    # Prediz o valor para daqui a 30 dias
    proxima_data = np.array([[X[-1][0] + 30]])
    predicao = model.predict(proxima_data)[0]
    
    # Salva o resultado na camada Gold
    os.makedirs("data/gold", exist_ok=True)
    with open("data/gold/previsao_ml.txt", "w") as f:
        f.write(f"{predicao:.2f}")
    print(f"✔ ML: Predição de {predicao:.2f}% gerada.")

if __name__ == "__main__":
    treinar_e_prever()