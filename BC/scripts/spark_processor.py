from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, regexp_replace, mean, max, min

# Inicializa a sessão do Spark voltada para o projeto BC
spark = SparkSession.builder.appName("BC_Gold_Processor").getOrCreate()

def processar_camadas_bc():
    # 1. Leitura da Bronze (O que você já baixou do BC)
    print("BC: Lendo dados brutos da Bronze...")
    df_raw = spark.read.json("data/bronze/inadimplencia_raw.json")
    
    # 2. Processamento Silver (Limpeza e Tipagem)
    print("BC: Gerando camada Silver...")
    df_silver = df_raw.withColumn("data", to_date(col("data"), "dd/MM/yyyy")) \
                      .withColumn("valor", regexp_replace(col("valor"), ",", ".").cast("double"))
    
    # Salva na Silver (Onde você viu os arquivos Parquet)
    df_silver.write.mode("overwrite").parquet("data/silver/inadimplencia_bc")
    
    # 3. Processamento Gold (Inteligência e Negócio)
    print("BC: Gerando camada Gold (Resumo de Risco)...")
    df_gold = df_silver.select(
        mean("valor").alias("media_inadimplencia"),
        max("valor").alias("pico_inadimplencia"),
        min("valor").alias("minimo_inadimplencia")
    )
    
    # Salva na Gold como CSV para fácil leitura humana
    df_gold.write.mode("overwrite").option("header", "true").csv("data/gold/risk_analysis")
    print("✔ Sucesso: Camadas Silver e Gold do BC atualizadas.")

if __name__ == "__main__":
    processar_camadas_bc()