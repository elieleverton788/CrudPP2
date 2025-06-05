def menu():
    print('''
    CRUD Gerenciador de contatos
    Escolha a opção desejada

    1. Criar contato
    2. Listar contatos
    3. Buscar contato
    4. Editar contato
    5. Excluir contato
    6. Listar grupos
    7. Criar grupo
    0. Sair
    ''')

def criar_grupo(grupos):
    nome_grupo = input("Digite o nome do grupo: ")
    if nome_grupo in grupos:
        print("Grupo já existe.")
    else:
        grupos.append(nome_grupo)
        print(f"Grupo '{nome_grupo}' criado com sucesso!")

def listar_grupos(grupos):
    if len(grupos) == 0:
        print("Nenhum grupo cadastrado.")
    else:
        print("Grupos existentes:")
        for grupo in grupos:
            print(f"- {grupo}")

def criar_contato(contatos, grupos):
    nome = input("Digite o nome: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o e-mail: ")

    listar_grupos(grupos)
    grupo = input("Digite o nome do grupo do contato (ou deixe em branco): ")

    if grupo and grupo not in grupos:
        print("Grupo não existe, criando automaticamente.")
        grupos.append(grupo)

    contato = {"nome": nome, "telefone": telefone, "email": email, "grupo": grupo}
    contatos.append(contato)
    print("Contato criado com sucesso!")

def lista_contatos(contatos):
    if len(contatos) == 0:
        print("Não existem contatos.")
    else:
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Grupo: {contato['grupo']}")

def buscar_contato(contatos):
    nome_especifico = input("Digite o nome do contato desejado: ")
    encontrado = False
    for contato in contatos:
        if contato["nome"] == nome_especifico:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Grupo: {contato['grupo']}")
            encontrado = True
            break
    if not encontrado:
        print("Pessoa não encontrada.")

def editar_contato(contatos, grupos):
    nome_especifico = input("Digite o nome do contato que deseja editar: ")
    for contato in contatos:
        if contato["nome"] == nome_especifico:
            print(f"Nome atual: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Grupo: {contato['grupo']}")
            
            novo_nome = input("Novo nome (pressione Enter para manter): ") or contato["nome"]
            novo_telefone = input("Novo telefone (pressione Enter para manter): ") or contato["telefone"]
            novo_email = input("Novo email (pressione Enter para manter): ") or contato["email"]

            listar_grupos(grupos)
            novo_grupo = input("Novo grupo (pressione Enter para manter): ") or contato["grupo"]

            if novo_grupo and novo_grupo not in grupos:
                print("Grupo não existe, criando automaticamente.")
                grupos.append(novo_grupo)

            contato.update({"nome": novo_nome, "telefone": novo_telefone, "email": novo_email, "grupo": novo_grupo})
            print("Contato atualizado com sucesso.")
            return
    print("Contato não encontrado.")

def excluir_contato(contatos):
    nome_especifico = input("Digite o nome do contato que deseja excluir: ")
    for contato in contatos:
        if contato["nome"] == nome_especifico:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            confirmar = input("Digite 1 para confirmar ou 0 para cancelar: ")
            if confirmar == "1":
                contatos.remove(contato)
                print("Contato excluído.")
                return
            else:
                print("Exclusão cancelada.")
                return
    print("Contato não encontrado.")

import json

def salvar_dados(contatos, grupos, filename="dados.json"):
    with open(filename, 'w') as f:
        json.dump({"contatos": contatos, "grupos": grupos}, f)

def carregar_dados(filename="dados.json"):
    try:
        with open(filename, 'r') as f:
            dados = json.load(f)
            return dados.get("contatos", []), dados.get("grupos", [])
    except FileNotFoundError:
        return [], []

def main():
    contatos, grupos = carregar_dados()
    opcoes = ""
    while opcoes != "0":
        menu()
        opcoes = input("Escolha uma opção: ")
        if opcoes == "1":
            criar_contato(contatos, grupos)
        elif opcoes == "2":
            lista_contatos(contatos)
        elif opcoes == "3":
            buscar_contato(contatos)
        elif opcoes == "4":
            editar_contato(contatos, grupos)
        elif opcoes == "5":
            excluir_contato(contatos)
        elif opcoes == "6":
            listar_grupos(grupos)
        elif opcoes == "7":
            criar_grupo(grupos)
        elif opcoes == "0":
            salvar_dados(contatos, grupos)
            print("Saindo e salvando os dados...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()





