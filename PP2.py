def menu():
    print('''




    CRUD Gerenciador de contatos
    Escolha a opção desejada




    1. Criar contato
    2. lista de contatos
    3. Buscar contato
    4. editar contato
    5. Excluir contato
    0. Sair
   
    ''')






def criar_contato(contatos):
    nome = input("Digite o nome")
    telefone = input("Digite o numero de telefone")
    email = input("Digite o E-mail")
    contatos.append((nome,telefone,email))
    print(contatos)


def lista_contatos(contatos):
    if len(contatos) == 0:
        print("Não existem contatos")
    else:
        for contato in contatos:
            nome,telefone,email = contato
            print(f" nome : {nome},telefone : {telefone}, email : {email} ")
           


def buscar_contato(contatos):
    nome_especifico = input("Digite o nome do contato desejado ")
    for contato in contatos:
         nome,telefone,email = contato
         if nome == nome_especifico:
             print(f" nome : {nome},telefone : {telefone}, email : {email} ")
             break
         else:
             print("pessoa não encotrada")
   


def editar_contato(contatos):
    nome_especifico = input("Digite o nome do contato desejado")
    for contato in contatos:
        nome,telefone,email = contato
        if nome == nome_especifico:
            print(f"Nome: {nome}, telefone: {telefone}, email: {email}") 
            novo_nome = input("Novo nome")
            novo_telefone = input("Novo telefone")
            novo_email = input("novo Email")
            
            confirmar_alteração = input("Digite 1 para confirmar ou 0 para ignorar")
            confirmar_alteração = int(confirmar_alteração)
            if confirmar_alteração == 1:
                contatos[contatos.index(contato)] = novo_nome,novo_telefone,novo_email
                print(f"Nome {novo_nome}, telefone {novo_telefone}, Email {novo_email}")
                break
            else:
                print("telefone com nome desejado {nome_especifico} não encontrada ")
                
            
            
def excluir_contato(contatos):
    nome_especifico = input("Digite o nome do contato desejado")
    for contato in contatos:
        nome,telefone,email = contato
        if nome == nome_especifico:
            print(f"Nome {nome} telefone {telefone}, Email {email}")
            excluir_contato = input('para excluir o contato, digite 1 ou 0 para ignorar')
            excluir_contato = int(excluir_contato)
        if excluir_contato == 1:
            del contatos[contatos.index(contato)]
            print(f'telefone com nome desejado {nome_especifico} excluida')
        else:
            print(f'contato com nome {nome_especifico} não encontrada')
               



   


import json
def salvar_dados(contatos, filename="dados.json"):
        with open(filename, 'w') as f:
            json.dump(contatos, f)
  
def carregar_dados(filename="dados.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def main_1():
    contatos = carregar_dados()
    opcoes = ""
    while opcoes != "0":
        menu()
        opcoes = input("Escolha uma opção")
        if opcoes == "1":
            criar_contato(contatos)
        elif opcoes == "2":
            lista_contatos(contatos)
        elif opcoes == "3":
            buscar_contato(contatos)
        elif opcoes == "4":
            editar_contato(contatos)
        elif opcoes == "5":
            excluir_contato(contatos)   
        
        elif opcoes == "0":
            break
        else: print("Numero invalido")

if __name__ == "__main__":
    main_1()
       