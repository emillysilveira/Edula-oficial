import psycopg2

# Conexão com o banco de dados
conn = psycopg2.connect(dbname='avaliacao_diagnostica', user='usuario', password='senha')

# Função para criar uma questão
def criar_questao(texto_questao, alternativas, resposta_correta):
  cursor = conn.cursor()
  cursor.execute("INSERT INTO questoes (texto_questao, alternativas, resposta_correta) VALUES (%s, %s, %s)", (texto_questao, alternativas, resposta_correta))
  conn.commit()
  cursor.close()

# Exemplo de criação de uma questão
texto_questao = "Qual a capital do Brasil?"
alternativas = ["Rio de Janeiro", "São Paulo", "Brasília", "Belo Horizonte"]
resposta_correta = 2  # Índice da alternativa correta (Brasília)

criar_questao(texto_questao, alternativas, resposta_correta)
