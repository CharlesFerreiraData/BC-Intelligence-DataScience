from fastapi import FastAPI
import duckdb

app = FastAPI(title="BC Data Science API")

@app.get("/status/credito")
def get_credito():
    # Lê a última taxa real da Silver
    relatorio = duckdb.query("SELECT valor FROM 'data/silver/inadimplencia_bc/*.parquet' ORDER BY data DESC LIMIT 1").fetchone()
    valor_atual = relatorio[0] if relatorio else 0
    
    # Lê a predição gerada pelo script de ML
    try:
        with open("data/gold/previsao_ml.txt", "r") as f:
            predicao = f.read()
    except:
        predicao = "Execute o script de ML primeiro"

    return {
        "projeto": "BC - Intelligence",
        "taxa_atual_bcb": f"{valor_atual}%",
        "predict_proximo_mes": f"{predicao}%",
        "analise": "Risco Elevado" if float(predicao.replace('%','')) > 4.0 else "Risco Controlado"
    }