from util import *;

LISTA_TAREFAS = [];

def criar_tarefa(tarefas):
    """
    Cria uma nova tarefa e adiciona na lista de tarefas
    
    ----------------
    
    Args: tarefas (list)
    input: Título da tarefa (str)
    Returns: none
    """
    
    titulo = entrar_titulo();
    id = definir_id(tarefas);
    tarefas.append({
        'id': id,
        'nome': titulo,
        'concluida': False
    });
    
def exibir_todas(tarefas):
    """
    Exibe todas as tarefas armazenadas na lista de tarefas
    
    ----------------
    
    Args: tarefas (list)
    input: none
    Returns: none
    """
    
    if len(tarefas) == 0:
        print("Nenhuma tarefa armazenada.");
    else:
        for tarefa in tarefas:
            print(f"ID: {tarefa['id']} - Título: {tarefa['nome']} - Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}");
            
def exibir_tarefa(tarefas):
    """
    Exibe uma tarefa específica
    
    ----------------
    
    Args: tarefas (list)
    input: id (int)
    Returns: none
    """
    
    tarefa = obter_tarefa(tarefas);
    
    if tarefa:
        print(f"ID: {tarefa['id']} - Título: {tarefa['nome']} - Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}")
        
def concluir_tarefa(tarefas):
    """
    Conclui uma tarefa específica
    
    ----------------
    
    Args: tarefas (list)
    input: id (int)
    Returns: none
    """
    
    tarefa = obter_tarefa(tarefas);
    
    if tarefa:
        tarefa['concluida'] = True;
        print("Tarefa concluída.");
        
def excluir_tarefa(tarefas):
    """
    Exclui uma tarefa específica
    
    ----------------
    
    Args: tarefas (list)
    input: id (int)
    Returns: none
    """
    
    tarefa = obter_tarefa(tarefas);
    
    if tarefa:
        tarefas.remove(tarefa);
        print("Tarefa excluída.");
        
def menu():
    """
    Exibe o menu de opções
    
    ----------------
    
    Args: none
    input: opção (int)
    Returns: none
    """
    
    print("1 - Criar uma nova tarefa");
    print("2 - Exibir todas as tarefas");
    print("3 - Exibir uma tarefa específica");
    print("4 - Concluir uma tarefa");
    print("5 - Deletar uma tarefa");
    print("6 - Sair");
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "));
            if opcao < 1 or opcao > 6:
                raise ValueError();
            else:
                return opcao;
        except ValueError:
            print("Opção inválida.");
            
def main():
    """
    Função principal
    
    ----------------
    
    Args: none
    input: none
    Returns: none
    """
    
    opcao = menu();
    while opcao != 6:
        match opcao:
            case 1:
                criar_tarefa(LISTA_TAREFAS);
            case 2:
                exibir_todas(LISTA_TAREFAS);
            case 3:
                exibir_tarefa(LISTA_TAREFAS);
            case 4:
                concluir_tarefa(LISTA_TAREFAS);
            case 5:
                excluir_tarefa(LISTA_TAREFAS);
            case _:
                print("Opção inválida.");
        opcao = menu();
        
main();