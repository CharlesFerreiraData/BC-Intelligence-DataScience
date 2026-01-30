@echo off
echo ==================================================
echo   INICIANDO PIPELINE BC - BANCO CENTRAL
echo ==================================================

echo [1/5] Subindo containers...
docker-compose up -d

echo [2/5] Executando Ingestao (Bronze)...
docker exec -it bc_container python scripts/ingestion.py

echo [3/5] Executando Processamento Spark (Silver/Gold)...
docker exec -it bc_container python scripts/spark_processor.py

echo [4/5] Executando Ciencia de Dados (Predict ML)...
docker exec -it bc_container python scripts/ml_predict.py

echo [5/5] Carregando Inteligencia em Grafos (Neo4j)...
docker exec -it bc_container python scripts/graph_loader.py

echo ==================================================
echo   PIPELINE FINALIZADO COM SUCESSO!
echo   API: http://localhost:8000/status/credito
echo   Grafos: http://localhost:7474
echo ==================================================
pause