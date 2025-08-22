import os
from colorama import init, Fore, Style

# Inicializa o colorama
init()

# --- Funções para o Gerenciamento de Tarefas ---


def adicionar_tarefa():
    tarefa = input(f"{Fore.CYAN}Digite a nova tarefa: {Style.RESET_ALL}")
    with open("tarefas.txt", "a") as arquivo:
        arquivo.write(f"[ ] {tarefa}\n")
    print(f"{Fore.GREEN}Tarefa adicionada com sucesso!{Style.RESET_ALL}")


def visualizar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
            if not tarefas:
                print(f"{Fore.YELLOW}Nenhuma tarefa encontrada.{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.BLUE}--- Suas Tarefas ---{Style.RESET_ALL}")
                for i, tarefa in enumerate(tarefas):
                    tarefa_formatada = tarefa.strip()
                    if tarefa_formatada.startswith("[x]"):
                        print(
                            f"{Fore.GREEN}{i+1}. {tarefa_formatada}{Style.RESET_ALL}")
                    else:
                        print(
                            f"{Fore.WHITE}{i+1}. {tarefa_formatada}{Style.RESET_ALL}")
                print(f"{Fore.BLUE}---------------------{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Nenhuma tarefa encontrada. O arquivo 'tarefas.txt' não existe.{Style.RESET_ALL}")


def remover_tarefa():
    visualizar_tarefas()
    if os.path.exists("tarefas.txt") and os.path.getsize("tarefas.txt") > 0:
        try:
            numero_tarefa = int(
                input(f"{Fore.CYAN}Digite o número da tarefa a ser removida: {Style.RESET_ALL}"))
            with open("tarefas.txt", "r") as arquivo:
                tarefas = arquivo.readlines()

            if 0 < numero_tarefa <= len(tarefas):
                tarefa_removida = tarefas.pop(numero_tarefa - 1)
                with open("tarefas.txt", "w") as arquivo:
                    arquivo.writelines(tarefas)
                print(
                    f"{Fore.GREEN}Tarefa '{tarefa_removida.strip()}' removida com sucesso!{Style.RESET_ALL}")
            else:
                print(
                    f"{Fore.RED}Número de tarefa inválido. Tente novamente.{Style.RESET_ALL}")
        except (ValueError, IndexError):
            print(
                f"{Fore.RED}Entrada inválida. Por favor, digite um número válido.{Style.RESET_ALL}")


def concluir_tarefa():
    visualizar_tarefas()
    if os.path.exists("tarefas.txt") and os.path.getsize("tarefas.txt") > 0:
        try:
            numero_tarefa = int(input(
                f"{Fore.CYAN}Digite o número da tarefa a ser concluída: {Style.RESET_ALL}"))
            with open("tarefas.txt", "r") as arquivo:
                tarefas = arquivo.readlines()

            if 0 < numero_tarefa <= len(tarefas):
                linha = tarefas[numero_tarefa - 1]
                if linha.startswith("[ ]"):
                    tarefas[numero_tarefa - 1] = linha.replace("[ ]", "[x]", 1)
                    with open("tarefas.txt", "w") as arquivo:
                        arquivo.writelines(tarefas)
                    print(
                        f"{Fore.GREEN}Tarefa concluída com sucesso!{Style.RESET_ALL}")
                else:
                    print(
                        f"{Fore.YELLOW}Esta tarefa já está concluída.{Style.RESET_ALL}")
            else:
                print(
                    f"{Fore.RED}Número de tarefa inválido. Tente novamente.{Style.RESET_ALL}")
        except (ValueError, IndexError):
            print(
                f"{Fore.RED}Entrada inválida. Por favor, digite um número válido.{Style.RESET_ALL}")


def sair_do_programa():
    print(f"{Fore.BLUE}Saindo do programa. Até mais!{Style.RESET_ALL}")
    exit()


def opcao_invalida():
    print(f"{Fore.RED}Opção inválida. Por favor, escolha entre 1 e 5.{Style.RESET_ALL}")

# --- O Novo Menu Principal com Dicionário ---


def main():
    menu_opcoes = {
        '1': adicionar_tarefa,
        '2': visualizar_tarefas,
        '3': remover_tarefa,
        '4': concluir_tarefa,
        '5': sair_do_programa
    }

    while True:
        print(
            f"\n{Fore.BLUE}--- Sistema de Gerenciamento de Tarefas ---{Style.RESET_ALL}")
        print(f"{Fore.WHITE}1. Adicionar nova tarefa{Style.RESET_ALL}")
        print(f"{Fore.WHITE}2. Visualizar todas as tarefas{Style.RESET_ALL}")
        print(f"{Fore.WHITE}3. Remover uma tarefa{Style.RESET_ALL}")
        print(f"{Fore.WHITE}4. Concluir uma tarefa{Style.RESET_ALL}")
        print(f"{Fore.WHITE}5. Sair do programa{Style.RESET_ALL}")

        escolha = input(
            f"{Fore.CYAN}Escolha uma opção (1-5): {Style.RESET_ALL}")

        acao = menu_opcoes.get(escolha, opcao_invalida)
        acao()


if __name__ == "__main__":
    main()
