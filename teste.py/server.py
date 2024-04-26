from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

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

    def perguntar_dificuldade(self, nome, disciplina):
        respostas = []
        if disciplina == '1':
            respostas.append(f"Bem-vindo(a), {nome}!")
            respostas.append("\nPara melhorar em Português, recomendo:")
            for dica in self.plano_estudos['Português']:
                respostas.append(f"- {dica}")
        elif disciplina == '2':
            respostas.append(f"Bem-vindo(a), {nome}!")
            respostas.append("\nPara melhorar em Matemática, recomendo:")
            for dica in self.plano_estudos['Matemática']:
                respostas.append(f"- {dica}")
        elif disciplina == '3':
            respostas.append(f"Bem-vindo(a), {nome}!")
            respostas.append("\nPara melhorar em Ciências, recomendo:")
            for dica in self.plano_estudos['Ciências']:
                respostas.append(f"- {dica}")
        elif disciplina == '4':
            respostas.append(f"Bem-vindo(a), {nome}!")
            respostas.append("\nPara melhorar em Biologia, recomendo:")
            for dica in self.plano_estudos['Biologia']:
                respostas.append(f"- {dica}")
        else:
            respostas.append("Opção inválida. Por favor, escolha novamente.")
        return respostas

ia = IA_Educacional()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pergunta_dificuldade', methods=['POST'])
def pergunta_dificuldade():
    data = request.get_json()
    nome = data['nome']
    disciplina = data['disciplina']
    respostas = ia.perguntar_dificuldade(nome, disciplina)
    return jsonify({'respostas': respostas})

if __name__ == '__main__':
    app.run(debug=True)
