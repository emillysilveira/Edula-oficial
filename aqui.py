from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///serio.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

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
    

@app.route("/")
def loginnn():
    return ("loginnn.html")


@app.route('/alu.html')
def alu():
    return ('alu.html')













if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)