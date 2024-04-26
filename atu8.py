import random

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

    def iniciar_aula(self):
        self.aluno = input("Qual é o seu nome? ")
        print(f"Bem-vindo(a), {self.aluno}!")

    def exercicio(self, assunto):
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

            print(f"\nQuestão {i + 1}:")
            print(f"Qual é o resultado de {num1} {operacao} {num2}?")
            resposta = int(input("Sua resposta: "))

            if resposta == resposta_correta:
                print(f"Correto! Parabéns! A resposta correta é {resposta_correta}.")
            else:
                print(f"Incorreto. A resposta correta é {resposta_correta}.")

    def perguntar_dificuldade(self):
        print("Escolha a disciplina em que você tem mais dificuldade:")
        print("1 - Português")
        print("2 - Matemática")
        print("3 - Ciências")
        print("4 - Biologia")
        
        escolha = input("Digite o número correspondente à disciplina: ")
        
        if escolha == "1":
            disciplina = "Português"
        elif escolha == "2":
            disciplina = "Matemática"
        elif escolha == "3":
            disciplina = "Ciências"
        elif escolha == "4":
            disciplina = "Biologia"
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            self.perguntar_dificuldade()
            return

        if disciplina == 'Português':
            print("\nPara melhorar em Português, recomendo:")
            for dica in self.plano_estudos[disciplina]:
                print(f"- {dica}")
        elif disciplina == 'Ciências':
            print("\nPara melhorar em Ciências, recomendo:")
            for dica in self.plano_estudos[disciplina]:
                print(f"- {dica}")
        else:
            print(f"\nEntendi que você tem dificuldade em {disciplina}. Vamos praticar alguns exercícios!")
            self.exercicio(disciplina)

# Exemplo de uso:
ia = IA_Educacional()
ia.iniciar_aula()
ia.perguntar_dificuldade()
