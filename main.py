#Importa Biblioteca

import os

#Lista Vazia

tarefas = []

#Laço de repetição

while True:

    #Usuário as tarefas que serão realizadas
    
    nova_tarefa = input('Insira a nova tarefa ou -Enter- para encerrar e exibir a lista: ')

    #Verifica se o usuário inseriu nova tarefa

    if nova_tarefa != '':
        tarefas.append(nova_tarefa) #Para inserir uma nova tarefa
        continue
    else:
        break

#Limpa o console

os.system('cls')

#Exibe a lista com todas as tarefas inseridas na lista

print(f'{'-'*30} LISTA DE TAREFAS {'-'*30}\n')

for tarefa in tarefas:
    print(tarefa)