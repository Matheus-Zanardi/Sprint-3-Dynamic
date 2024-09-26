import funcoes
import json
import os
from funcoes import verifica_usuario

print('\n\n***************** 𝒞𝑙𝑖𝑛𝑒 𝒬𝑢𝑒𝑠𝑡 *****************\n\n')
print('************** Bem vindo ao jogo **************')
print('\nVamos aprmorar suas habilidades motoras e te ajudar e realizar com mais precisão e perfeição as suas cirurgias\n\n')


print('Já tem cadastro no app? (s/n)')
resposta_cadastro = input(':').lower()
while resposta_cadastro != 's' and resposta_cadastro != 'n':
    print('insira uma resposta valida => (s/n)')
    resposta_cadastro = input(':').lower()
if resposta_cadastro == 'n':
    print('Vamos fazer o seu cadastro.')
    print('Digite seu nome:')
    nome_usuario = input(':')
    funcoes.verifica_numero(nome_usuario)
    while  funcoes.verifica_numero(nome_usuario) == True:
        print('O nome não pode conter numeros')
        print('Digite seu nome:')
        nome_usuario = input(':')
        funcoes.verifica_numero(nome_usuario)

    print('Digite seu email')
    email_usario = input(':')
    funcoes.verifica_email(email_usario)
    while funcoes.verifica_email(email_usario) == True:
        print('O email deve conter um @ e um .com')
        print('Digite seu email')
        email_usario = input(':')
        funcoes.verifica_email(email_usario)


    print('A senha deve ter pelo menos um numero e uma letra maiuscula')
    print('Digite sua senha')
    senha_usuario = input(':')
    
    funcoes.verifica_maiuscula(senha_usuario)
    while funcoes.verifica_maiuscula(senha_usuario) == False:
        print('Senha precisa de pelo menos 1 letra maiuscula')
        print('A senha deve ter pelo menos um numero e uma letra maiuscula')
        print('Digite sua senha')
        senha_usuario = input(':')
        funcoes.verifica_maiuscula(senha_usuario)

    while  funcoes.verifica_numero(senha_usuario) == False:
        print('A senha precisa ter pelo menos 1 numero')
        print('A senha deve ter pelo menos um numero e uma letra maiuscula')
        print('Digite sua senha')
        senha_usuario = input(':')
        funcoes.verifica_maiuscula(senha_usuario)

    usuario_dados = {"nome": nome_usuario, "email": email_usario, "senha": senha_usuario, "Recorde" : 0}
    funcoes.salvar_em_json(usuario_dados)
resposta_cadastro = 's'

while resposta_cadastro != 's' and resposta_cadastro != 'n':
    print('insira uma resposta valida => (s/n)')
    resposta_cadastro = input(':').lower()
if resposta_cadastro == 's':

    print('Você já realizou o cadastro, agora vamos logar')
    print('Digite o seu email, para logar')
    email_logar = input(':')
    
    print('Digite a sua senha, para logar')
    senha_logar = input(':')
    # funcoes.verifica_usuario(email_logar, senha_logar)
    if funcoes.verifica_usuario(email_logar, senha_logar) == True:
        while funcoes.verifica_usuario(email_logar, senha_logar):
            print('Login incorreto!')
            print('Tente novamente')
            print('Digite o seu email, para logar')
            email_logar = input(':')
            print('Digite a sua senha, para logar')
            senha_logar = input(':')
            
            funcoes.verifica_usuario(email_logar, senha_logar)
continuar = 0
while continuar == 0:
    print("\nVamos iniciar o Jogo")
    print("A dificuldae se refere ao tempo que o usuario tem para realizar o jogo")
    print("Selecione a dificulade:\n")
    print("Facil(1)")
    print("Médio(2)")
    print("Difícil(3)")

    esc = int(input(":"))
    while esc not in (1,2,3):
        print('Dificuldade invalida')
        print("Selecione a dificulade:\n")
        print("Facil(1)")
        print("Médio(2)")
        print("Difícil(3)")
        esc = int(input(":"))

    tempo = 0
    if esc == 1:
        tempo =30
    elif esc == 2:
        tempo = 20
    else:
        tempo = 10

    print("Agora vai começar a cirurgia")
    print(f"você tem {tempo} miutos para realizar a atividade")
    print('...')
    print("vamos simular como foi a cirugia")

    print("Digite quantos minutos você levou para realizar (numeros inteiros!)")
    tp = int(input(':'))
    print("Digite a porcentagem da sua precisão ao realizar a cirurgia (0 a 100)")
    precisao = int(input(':'))

    if precisao < 60:
        pontuacao = 0
    else:
        pontuacao = (precisao/10)

    if tp > tempo:
        precisao = 0

    print(f'Sua Pontuação foi {pontuacao}')


    with open("usuarios.json", "r") as arquivo:
        dados = json.load(arquivo)

    for usuario in dados['usuarios']:
         if usuario['email'] == email_logar:
            if usuario['Recorde'] < pontuacao:
                funcoes.alterar_recorde(email_logar, pontuacao)

    with open("usuarios.json", "r") as arquivo:
        dados = json.load(arquivo)

    for usuario in dados['usuarios']:
        if usuario['email'] == email_logar:
            print(f"{usuario['nome']}, seu record é {usuario['Recorde']}")

    print('Deseja jogar novamente? (s/n)')
    jgnvmt = input(':')
    while jgnvmt not in ('s', 'n'):
        print('Deseja jogar novamente? (s/n)')
        print('insira um valor valido')
        jgnvmt = input(':')
    if jgnvmt == 'n':
        continuar = 1
print('\nObrigado por Jogar')
print('Continue Praticando')
print('O futuro precisa dos melhores medicos')
   
