🏛️ Projeto de Inteligência de Dados - Inadimplência PF (Banco Central)
Este projeto consiste em um ecossistema completo de dados que automatiza a coleta, o processamento, a análise preditiva e a visualização de indicadores 
financeiros de crédito no Brasil. O foco principal é a Taxa de Inadimplência da Pessoa Física (Recursos Livres), utilizando dados oficiais obtidos via API 
do Banco Central do Brasil.

🛠️ Arquitetura e Engenharia de Dados
O projeto foi construído seguindo os princípios da Arquitetura Medallion, garantindo a qualidade e a governança do dado em três estágios:
Camada Bronze (Raw): Realiza o consumo direto da API do BCB, armazenando os dados brutos em formato JSON exatamente como foram coletados.
Camada Silver (Trusted): Utiliza o Apache Spark (PySpark) para a limpeza dos dados. Nesta etapa, as datas são tipadas corretamente e os 
valores monetários são convertidos para decimais, sendo salvos em formato Parquet de alta performance.

Camada Gold (Analytics): Consolida as regras de negócio. Aqui são gerados os KPIs (Key Performance Indicators), como a média histórica, 
o pico máximo de inadimplência e o valor mínimo registrado no período.

🧠 Ciência de Dados e Predição
Além da engenharia, o projeto incorpora uma camada de Data Science para transformar dados históricos em visão de futuro:
Modelo Preditivo: Foi implementado um algoritmo de Regressão Linear que analisa a série temporal da inadimplência.
Inteligência de Negócio: O sistema calcula a tendência para o próximo mês, permitindo uma análise proativa sobre o risco de crédito.
Visualização Técnica: Um motor de geração de gráficos automatizado produz visualizações de linha que permitem identificar ciclos econômicos 
e tendências de alta ou baixa de forma visual e clara.

🔗 Inteligência em Grafos e API
O projeto não se limita a tabelas, explorando conexões complexas e entrega de dados:
Base em Grafos (Neo4j): Os dados são modelados em nós e relacionamentos, permitindo identificar como diferentes períodos e indicadores se 
conectam dentro de um ecossistema financeiro.
API REST (FastAPI): Uma interface de comunicação moderna foi criada para servir esses dados. Qualquer sistema externo pode consultar a API 
para receber o status atual da inadimplência e a predição gerada pelo modelo de Machine Learning.

🐳 Tecnologia e Infraestrutura
Toda a solução é conteinerizada com Docker, o que garante que o projeto funcione em qualquer ambiente sem a necessidade de instalações manuais 
complexas. Através do Docker Compose, o banco de dados de grafos e o motor de processamento trabalham em sincronia, isolados e seguros.

📈 Conclusão
O resultado final é uma ferramenta robusta que demonstra o ciclo completo de um profissional de dados moderno: desde a capacidade de extrair informação 
bruta de fontes oficiais até a entrega de uma predição inteligente via API, passando por um processamento de Big Data escalável.
