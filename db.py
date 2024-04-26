from sqlalchemy import create_engine, Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria um engine de banco de dados (substitua 'sqlite:///example.db' pelo seu banco de dados)
engine = create_engine('sqlite:///isso.db')

# Cria uma base de classe declarativa
Base = declarative_base()

# Define a classe que representa a tabela do banco de dados
class User(Base):
    _tablename_ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sobrenome = Column(String)
    email = Column(String)
    senha = Column(String)
    receber_email = Column(Boolean)

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine, autocommit=True)
session = Session()

# Exemplo de como adicionar um usuário ao banco de dados
new_user = User(name='John', sobrenome='Doe', email='john@example.com', senha='123456', receber_email=True)
session.add(new_user)

# Exemplo de como consultar todos os usuários no banco de dados
users = session.query(User).all()
for user in users:
    print(user.name, user.email)
    return render_template ('cad.html')