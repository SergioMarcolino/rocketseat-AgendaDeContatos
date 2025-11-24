import contato


print("\n Escolha uma das opcoes abaixo")
lista_contatos = []
lista_contatos_favoritos = []
while True:
    print("1. Adicionar um novo contato")
    print("2. Ver lista de contatos")
    print("3. editar contado existente")
    print("4. marcar/desmarcar contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato ")
    
    escolha = input("qual opcao deseja escolher: ")
    
    if escolha == "1":
        nome_contato = input("Nome do contato: ")
        numero_contato = input("Numero do contato: ")
        contato.novo_contato(lista_contatos,nome_contato,numero_contato)
    elif escolha == "2":
             contato.ver_contatos(lista_contatos)   
    elif escolha == "3":
        indice = input("Qual contato deseja atualizar: ")
        novo_nome = input("Qual o novo nome: ")
        
        contato.editar_contato(lista_contatos, indice, novo_nome)
    elif escolha == "4":
        indice = input("Qual contato deseja atualizar: ")
        contato.favoritar_contato(lista_contatos,lista_contatos_favoritos, indice)
        print(lista_contatos_favoritos)
    elif escolha == "5":
        contato.Ver_contatos_favoritados(lista_contatos_favoritos)
        
             
    elif escolha == "6":
        break