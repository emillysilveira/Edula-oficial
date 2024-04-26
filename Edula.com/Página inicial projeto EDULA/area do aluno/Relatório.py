import random
from nltk import CFG, ChartParser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Definindo a gramática para geração de relatórios
grammar = CFG.fromstring("""
    S -> Subject Verb Adjective_objective Adjective? Noun Predicate '.' | Subject Verb Noun Predicate '.' | Subject Verb Predicate '.'
    Subject -> 'O aluno' | 'O estudante'
    Verb -> 'demonstrou' | 'exibiu' | 'apresentou'
    Adjective_objective -> 'um desempenho abaixo da média' | 'um desempenho satisfatório' | 'um desempenho excepcional'
    Adjective -> 'significativo' | 'considerável' | 'notável'
    Noun -> 'nas avaliações e testes de matemática' | 'durante o período de avaliação'
    Predicate -> 'com notas refletindo uma dificuldade em compreender e aplicar os conceitos matemáticos ensinados em sala de aula' | 'mostrando dificuldades em resolver problemas práticos e contextualizados'
""")

# Função para gerar sentenças aleatórias com base na gramática definida
def generate_sentence(grammar, start_symbol='S', max_depth=10):
    parser = ChartParser(grammar)
    for tree in parser.parse(start_symbol):
        if tree.height() <= max_depth:
            return ' '.join(tree.leaves())

# Função para limpar e tokenizar o texto
def preprocess_text(text):
    stop_words = set(stopwords.words('portuguese'))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return tokens

# Função para criar um relatório
def generate_report():
    subject = 'O aluno'
    report_parts = [
        "demonstrou um desempenho abaixo da média nas avaliações e testes de matemática, com notas refletindo uma dificuldade em compreender e aplicar os conceitos matemáticos ensinados em sala de aula.",
        "exibiu um desempenho satisfatório durante o período de avaliação.",
        "apresentou um desempenho excepcional, mostrando dificuldades em resolver problemas práticos e contextualizados."
    ]
    report = f"{subject} {random.choice(report_parts)}"
    return report

# Geração de relatórios de exemplo
print("Relatório Gerado:")
print(generate_sentence(grammar))
print(generate_report())
