# Sistema de Gerenciamento de Eventos Universitários - UniFECAF
# Desenvolvido por João Vitor Silva de Oliveira

eventos = []  # Lista que armazena todos os eventos
proximo_id = 1  # ID incremental para eventos


def cadastrar_evento():
    global proximo_id
    print("\n=== Cadastro de Evento ===")
    nome = input("Nome do evento: ")
    data = input("Data do evento (DD/MM/AAAA): ")
    descricao = input("Descrição: ")
    try:
        vagas = int(input("Número máximo de participantes: "))
    except ValueError:
        print("Valor inválido para vagas.")
        return

    evento = {
        "id": proximo_id,
        "nome": nome,
        "data": data,
        "descricao": descricao,
        "vagas": vagas,
        "inscritos": []
    }
    eventos.append(evento)
    proximo_id += 1
    print("Evento cadastrado com sucesso!")


def atualizar_evento():
    print("\n=== Atualizar Evento ===")
    try:
        id_evento = int(input("Digite o ID do evento a ser atualizado: "))
    except ValueError:
        print("ID inválido.")
        return

    for evento in eventos:
        if evento["id"] == id_evento:
            print(f"Evento encontrado: {evento['nome']}")
            evento["data"] = input("Nova data: ")
            try:
                evento["vagas"] = int(input("Novo número de vagas: "))
            except ValueError:
                print("Número de vagas inválido.")
                return
            print("Evento atualizado com sucesso!")
            return

    print("Evento não encontrado.")


def visualizar_eventos():
    print("\n=== Eventos Disponíveis ===")
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    for evento in eventos:
        vagas_restantes = evento["vagas"] - len(evento["inscritos"])
        print(f"\nID: {evento['id']}")
        print(f"Nome: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Descrição: {evento['descricao']}")
        print(f"Vagas restantes: {vagas_restantes}")


def inscrever_em_evento():
    print("\n=== Inscrição em Evento ===")
    try:
        id_evento = int(input("Digite o ID do evento: "))
    except ValueError:
        print("ID inválido.")
        return

    nome_aluno = input("Nome do aluno: ")

    for evento in eventos:
        if evento["id"] == id_evento:
            if len(evento["inscritos"]) < evento["vagas"]:
                evento["inscritos"].append(nome_aluno)
                print(f"{nome_aluno} inscrito com sucesso!")
            else:
                print("Não há vagas disponíveis.")
            return

    print("Evento não encontrado.")


def visualizar_inscricoes():
    print("\n=== Lista de Inscritos por Evento ===")
    try:
        id_evento = int(input("Digite o ID do evento: "))
    except ValueError:
        print("ID inválido.")
        return

    for evento in eventos:
        if evento["id"] == id_evento:
            print(f"\nEvento: {evento['nome']}")
            if evento["inscritos"]:
                for inscrito in evento["inscritos"]:
                    print(f"- {inscrito}")
            else:
                print("Nenhum inscrito até o momento.")
            return

    print("Evento não encontrado.")


def excluir_evento():
    print("\n=== Excluir Evento ===")
    try:
        id_evento = int(input("Digite o ID do evento a ser excluído: "))
    except ValueError:
        print("ID inválido.")
        return

    for evento in eventos:
        if evento["id"] == id_evento:
            eventos.remove(evento)
            print("Evento excluído com sucesso!")
            return

    print("Evento não encontrado.")


def menu():
    while True:
        print("\n==== MENU ====")
        print("1. Cadastrar evento")
        print("2. Atualizar evento")
        print("3. Visualizar eventos disponíveis")
        print("4. Inscrever-se em evento")
        print("5. Ver inscritos de um evento")
        print("6. Excluir evento")
        print("7. Sair")

        opcao = input("Escolha uma opção (1-7): ")

        if opcao == "1":
            cadastrar_evento()
        elif opcao == "2":
            atualizar_evento()
        elif opcao == "3":
            visualizar_eventos()
        elif opcao == "4":
            inscrever_em_evento()
        elif opcao == "5":
            visualizar_inscricoes()
        elif opcao == "6":
            excluir_evento()
        elif opcao == "7":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Iniciar o sistema
menu()
