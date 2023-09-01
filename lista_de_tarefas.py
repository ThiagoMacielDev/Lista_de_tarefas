def listar():
    if task_list:
        print('\nLista de tarefas: ', *task_list, sep='\n')
        # print()
        return 0
    print("\nNao há nada para listar")

def remover():
    item = task_list.pop()
    user_log.append([remover, item])

def adicionar(item):
    task_list.append(item)
    user_log.append([adicionar, item])

def desfazer(num_op=-1):
    try:
        acao = user_log[num_op][0].__name__
        item = user_log[num_op][1]
        if acao == adicionar.__name__:
            user_log.pop(num_op)
            remover()
        else:
            desfazer(num_op-1)
    except:
        print("Não há nada para desfazer")

def refazer(num_op=-1):
    try:
        acao = user_log[num_op][0].__name__
        item = user_log[num_op][1]
        if acao == remover.__name__:
            user_log.pop(num_op)
            adicionar(item)
        else:
            return refazer(num_op-1)
    except:
        print("Não há nada para refazer")

def menu(opcao_usuario):
    comando_usuario = funcoes[opcao_usuario]
    return comando_usuario()

task_list = []
user_log = []
funcoes = [listar,desfazer,refazer]

while True:
    user_input = input("\nComandos \n[0] listar \n[1] desfazer \n[2] refazer\nDigite a tarefa ou comando: ").lower()
    if user_input.isdigit():
        menu(int(user_input))
    else:
        adicionar(user_input)