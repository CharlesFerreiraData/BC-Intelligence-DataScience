from neo4j import GraphDatabase

class BCGraph:
    def __init__(self):
        # Conecta ao serviço Neo4j definido no Docker
        self.driver = GraphDatabase.driver("bolt://neo4j_db:7687", auth=("neo4j", "password123"))

    def criar_relacoes(self):
        with self.driver.session() as session:
            session.run("""
                MERGE (o:Orgao {nome: 'Banco Central'})
                MERGE (i:Indicador {nome: 'Inadimplencia PF'})
                MERGE (o)-[:GERA_DADOS]->(i)
            """)
        print("✔ BC: Relacionamentos criados no Neo4j.")

if __name__ == "__main__":
    BCGraph().criar_relacoes()