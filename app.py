import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i + 1}. [{status}] {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({"descricao": descricao, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada.")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Número da tarefa para concluir: ")) - 1
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída.")
    except (IndexError, ValueError):
        print("Número inválido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Número da tarefa para remover: ")) - 1
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print("Tarefa removida.")
    except (IndexError, ValueError):
        print("Número inválido.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()