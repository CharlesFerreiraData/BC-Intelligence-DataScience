import requests
import json
import os

def extrair_bc(codigo, nome):
    print(f"BC: Acessando série {codigo}...")
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            os.makedirs("data/bronze", exist_ok=True)
            with open(f"data/bronze/{nome}.json", "w") as f:
                json.dump(response.json(), f)
            print(f"✔ BC: {nome}.json salvo com sucesso.")
    except Exception as e:
        print(f"✖ Erro na conexão com BC: {e}")

if __name__ == "__main__":
    # Série 21082: Inadimplência PF
    extrair_bc(21082, "inadimplencia_raw")