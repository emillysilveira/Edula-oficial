from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import openai

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edula.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    numero = db.collun(db.string(1000), nullable=False)
class IA_Educacional:
    def __init__(self):
        self.aluno = ""
        self.plano_estudos = {
            'Português': ['Interpretação de texto.',
                          'Leitura e compreensão de textos diversos: narrativos, descritivos, informativos.',
                          'Identificação de elementos textuais: Personagens, enredo, tempo, espaço.',
                          'Inferências: Compreensão implícita de informações no texto.',
                          'Uso de estratégias de leitura: Identificação de palavras-chave, contexto, etc.',
                          'Praticar a escrita através de redações e resumos.',
                          'Produção Textual:',
                          'Redação de textos narrativos simples',
                          'Elaboração de parágrafos com coerência e coesão.',
                          'Uso correto da pontuação: Pontos finais, vírgulas, ponto e vírgula',
                          'Organização textual: Introdução, desenvolvimento e conclusão.'],
            'Matemática': ['Praticar exercícios de matemática todos os dias por 30 minutos.', 
                           'Assistir vídeos explicativos sobre os tópicos que você tem dificuldade.', 
                           'Revisar os conceitos básicos antes de avançar para tópicos mais complexos.'],
            'Ciências': ['Realizar experimentos práticos para visualizar os conceitos abstratos.',
                         'Participar de debates e discussões sobre tópicos científicos.',
                         'Criar mapas mentais para organizar e revisar os principais conceitos.',
                         'Explorar sites educacionais para obter informações adicionais.'],
            'Biologia': ['Estudar a anatomia e fisiologia do corpo humano.',
                         'Entender os processos de reprodução e genética.',
                         'Explorar a diversidade da vida e ecossistemas.',
                         'Analisar os impactos ambientais e medidas de preservação.']
        }

    def exercicio(self, assunto):
        questions = []
        for i in range(3):
            operacoes = ['Adição', 'Subtração', 'Multiplicação', 'Divisão']
            operacao = random.choice(operacoes)
            if operacao == 'Adição':
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
                resposta_correta = num1 + num2
            elif operacao == 'Subtração':
                num1 = random.randint(1, 10)
                num2 = random.randint(1, num1)
                resposta_correta = num1 - num2
            elif operacao == 'Multiplicação':
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
                resposta_correta = num1 * num2
            elif operacao == 'Divisão':
                num2 = random.randint(1, 10)
                resposta_correta = random.randint(1, 10)
                num1 = num2 * resposta_correta

            question = {
                "number": i + 1,
                "question": f"Qual é o resultado de {num1} {operacao} {num2}?",
                "answer": resposta_correta
            }
            questions.append(question)
        return questions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        repetir_senha = request.form['repetir_senha']
        
        # Verificar senhas
        if senha != repetir_senha:
            return 'As senhas não coincidem!'
        
        # Criar novo usuário dentro do contexto de aplicação
        with app.app_context():
            novo_usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()
        
        return 'Usuário cadastrado com sucesso!'
    
    # Se for método GET, renderizar o template HTML
    return render_template('cad.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Adicione aqui o código para lidar com o login
        pass
    return render_template('loginnn.html')

@app.route("/alu", methods=['GET', 'POST'])
def aula():
    if request.method == 'POST':
        # Adicione aqui o código para iniciar a aula
        pass
    return render_template('alu.html')

@app.route("/ia", methods=['GET', 'POST'])
def ia():
    if request.method == 'POST':
        # Iniciar interação com a IA
        ia = IA_Educacional()
        questions = ia.exercicio("Matemática")
        return render_template('ia.html',questions=questions)
    
    return render_template('ia.html')









if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
