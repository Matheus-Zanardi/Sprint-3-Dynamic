import json
import os
def verifica_email(email):
    if "@" not in email :
        
        return True
    if ".com" not in email:
        
        return True

def verifica_numero(palavra):

    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in num:
        if i in palavra:
            return True
    return False
def verifica_maiuscula(palavra):
    for caractere in palavra:
        if caractere.isupper():
            return True  # Se encontrar pelo menos uma letra maiúscula, retorna True
    # Se nenhum caractere maiúsculo for encontrado, retorna False
    return False

def salvar_em_json(dados):
    try:
        # Tenta abrir o arquivo em modo de leitura
        with open("usuarios.json", "r") as arquivo:
            # Carrega os dados existentes do arquivo
            lista_usuarios = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou se houver um erro de decodificação JSON, cria uma lista vazia
        lista_usuarios = {"usuarios": []}

    # Adiciona os novos dados à lista de usuários
    lista_usuarios["usuarios"].append(dados)

    # Abre o arquivo em modo de escrita para salvar os dados atualizados
    with open("usuarios.json", "w") as arquivo:
        json.dump(lista_usuarios, arquivo, indent=2)

def verifica_usuario(email, senha):
    with open("usuarios.json", "r") as arquivo:
        lista_usuarios = json.load(arquivo)
        dados = lista_usuarios['usuarios']
        for i in range(0, len(dados)):
            dados_usuario = lista_usuarios['usuarios'][i]   
            if email == dados_usuario["email"] and senha == dados_usuario["senha"]:
                nome_do_usuario = dados_usuario["nome"]
                rec = dados_usuario["Recorde"]
                print(f'login realizado com sucesso, bem vindo {nome_do_usuario}\nSeu recorde atual é :{rec}')
                return False
        
        return True

def alterar_recorde(email, novo_recorde):
    with open("usuarios.json", "r") as arquivo:
        dados = json.load(arquivo)

    for usuario in dados['usuarios']:
        if usuario['email'] == email:
            usuario['Recorde'] = novo_recorde
            break
    with open("usuarios.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)