def novo_contato(lista_contato,nome_contato, numero_contato):
    contato = {"nome": nome_contato, "numero": numero_contato, "favorito": False}
    lista_contato.append(contato)
    print(f"Contato {nome_contato} adicionado com sucesso")
    return
def ver_contatos(lista_contatos):
    print("Lista de contatos")
    for indice, contato in enumerate(lista_contatos, start=1):
        favorito = "fa" if contato["favorito"] else ""
        nome = contato["nome"]
        numero = contato["numero"]
        print(f"\n{indice}. nome: {nome} telefone: {numero} favorito[{favorito}]")
def editar_contato(lista_contatos, indice, novo_nome):
    ajustar_indice = int(indice) -1
    lista_contatos[ajustar_indice]["nome"] = novo_nome
    print(f"Contato: {ajustar_indice}. atualizado")
def favoritar_contato(lista_contatos,lista_contatos_favoritos, indice):
    
    ajustar_indice = int(indice) -1
    if lista_contatos[ajustar_indice]["favorito"] == False:
        lista_contatos[ajustar_indice]["favorito"] = True
        lista_contatos_favoritos.append(lista_contatos[ajustar_indice])
        print(f"contato {indice} favoritado")
    else: 
        lista_contatos[ajustar_indice]["favorito"] = False
        lista_contatos_favoritos.remove(lista_contatos[ajustar_indice])
        print(f"contato {indice} desfavoritado")
     
    
    print(f"contato {indice} favoritado")
    return
def Ver_contatos_favoritados(lista_contatos_favoritados):
     print("Lista de contatos favoritados")
     for indice, contato in enumerate(lista_contatos_favoritados, start=1):
        favorito = "fa" if contato["favorito"] else ""
        nome = contato["nome"]
        numero = contato["numero"]
        print(f"\n{indice}. nome: {nome} telefone: {numero} favorito[{favorito}]")
        return