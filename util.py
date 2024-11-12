def definir_id(tarefas):
    """
    Define o ID de uma nova tarefa a ser cadastrada.
    
    ----------------
    
    Args: tarefas (list)
    input: none
    Returns: id (int)
    """
    
    if len(tarefas) == 0:
        return 1;
    return tarefas[-1]['id'] + 1;

def entrar_id():
    """
    Solicita o ID de uma tarefa ao usuário.
    
    ----------------
    
    Args: none
    input: id (int)
    Returns: id (int)
    """
    
    while True:
        try:
            id_tentative = int(input("Digite o ID da tarefa: "));
            
            if id_tentative <= 0:
                print("Digite um número maior que 0.");
            else:
                return id_tentative
        except ValueError:
            print("Digite um número inteiro.");
            
def entrar_titulo():
    """
    Solicita o título de uma tarefa ao usuário.
    
    ----------------
    
    Args: none
    input: título (str)
    Returns: título (str)
    """
    
    while True:
        titulo = input("Digite o título da tarefa: ");
        if len(titulo) < 2:
            print("Digite um título válido.");
        else:
            return titulo;
        
def obter_tarefa(tarefas):
    """
    Retorna uma tarefa a partir de seu ID.
    
    ----------------
    
    Args: tarefas (list)
    input: id (int)
    Returns: tarefa (dict) ou none
    """
    id = entrar_id();
    
    for tarefa in tarefas:
        if tarefa['id'] == id:
            return tarefa;
    
    print("Tarefa não encontrada.");
    return None;