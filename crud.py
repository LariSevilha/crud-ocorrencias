from datetime import datetime
def autenticar(nome,senha):
  arquivo = open('chave.txt', 'r')
  nomea = arquivo.readline().split()
  senhaa = arquivo.readline().split()
  nome_cripto, senha_cripto = asc(nome,senha)
  if nome_cripto == nomea and senha_cripto == senhaa:
     print('Seja bem vindo ao sistema!!')
     menu_ocorrencias(lista_ocorrencias,cout)
  else:
     print('Usuário e/ou senha incorreto. Tente Novamente!')
  arquivo.close()
  
def verifica_igualdade(valor1, valor2):
   if len(valor1) != len(valor2):
     return False
   
def asc(nome, senha):
    nomel = []
    senhal = []
    for i in nome:
     nomel.append(str(ord(i)))
    for i in senha:
      senhal.append(str(ord(i)))
    return nomel, senhal
    
def cripto_asc(nome, senha):
    print("nome em ascii: ", end="")
    for i in nome:
      print(ord(i), " ", end="")
    print("\nsenha em ascii: ", end="")
    for i in senha:
      print(ord(i), " ", end="")
      
def gravar_visitantes(nome,email):
    arquivo2 = open("visitas.txt", 'a', encoding="utf-8")
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    arquivo2.write(data_e_hora_em_texto + " " + nome + " " + email +"\n")
    arquivo2.close()
    
def menu_simples():
   opcao = str(input('Como você deseja logar:\n\n 1- Visitante \n\n 2- Administrador \n\n Digite: '))  
   if opcao == '1':
     visita()
   else:
     executar()
   
def visita():
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    gravar_visitantes(nome,email)
    listagem(lista_ocorrencias)

def executar():
    print('Entre com os seus dados: ')
    nome = input('Entre com seu nome: ')
    senha = input('Entre com sua senha: ')
    autenticar(nome, senha)

def menu_ocorrencias(lista_ocorrencias, count):
    opcao = 1
    while opcao != 0:
        print("---Menu de Ocorrências---")
        print("1 - Cadastro de ocorrência")
        print("2 - Listar todas ocorrências")
        print("3 - Listar todas ocorrências ativas")
        print("4 - Buscar Ocorrência por título")
        print("5 - Alterar atividade da ocorrência")
        print("6 - Remover Ocorrência")
        print("7 - Listar Ocorrências por mês")
        print("8 - Listar Ocorrências contendo a palavra")
        print("0 - Sair")
        opcao = int(input("Entre com a opção>>"))
        if opcao == 1:
            print("---Cadastro---")
            cadastro(lista_ocorrencias, count)
            count += 1
        elif opcao == 2:
            print("---Listagem---")
            listagem(lista_ocorrencias)
        elif opcao == 3:
            print("Listagem[ATIVAS]")
            listagem_ativas(lista_ocorrencias)
        elif opcao == 4:
            print("Busca por título")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("**Ocorrência Encontrada!**")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
            else:
                print("Ocorrência não encontrada!")
        elif opcao == 5:
            print("Alteração de Status de Atividade")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("**Ocorrência Encontrada!**")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
                resp = input("Deseja alterar a situação da atividade " 
                      "da ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias[posicao]["status"] = not lista_ocorrencias[posicao]["status"]
                    print("Alteração realizada com sucesso!")
                    regravarArquivo(lista_ocorrencias)
                else:
                    print("Saindo sem alterações")
            else:
                print("Ocorrência não encontrada!")
        elif opcao == 6:
            print("Remoção de Ocorrência")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("**Ocorrência Encontrada!**")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
                resp = input("Deseja remover a ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias.pop(posicao)
                    print("Remoção realizada com sucesso!")
                    regravarArquivo(lista_ocorrencias)
                else:
                    print("Saindo sem alterações")
            else:
                print("Ocorrência não encontrada!")
        elif opcao == 7:
            print("Listagem de Ocorrências por mês")
            mes = input("Entre com o mês de ocorrência:")
            lista_m = buscar_ocorrencia_mes(lista_ocorrencias, mes)
            if lista_m:
                print("**Ocorrência(s) Encontrada(s)!**")
                listagem(lista_m)
            else:
                print("Não existem ocorrências para o mês ", mes, "!")
        elif opcao == 8:
            print("Listagem de Ocorrências que contem a palavra:")
            titulo = input("Entre a palavra buscada na ocorrência:")
            lista_m = buscar_ocorrencia_palavra(lista_ocorrencias, titulo)
            if lista_m:
                print("**Ocorrência(s) Encontrada(s)!**")
                listagem(lista_m)
            else:
                print("Não existem ocorrências com a palavra ", titulo, "!")
        elif opcao == 0:
            print("Saindo do programa!!!")
        else:
            print("Opção Inválida!")
    

def cadastro(lista_ocorrencias, count):
    id = count
    titulo = input("Entre com o título da ocorrência:")
    descricao = input("Entre com a descrição da ocorrência:")
    implicacoes = input("Entre com as implicações da ocorrência:")
    em_atividade = input("Está em atividade? (sim|não)")
    status = True if em_atividade == "sim" else False
    data = input("Entre com a data de inclusão:")
    prazo = int(input("Entre com a estimativa de prazo em dias:"))
    ocorrencia = dict(id = id, titulo = titulo, 
                      descricao = descricao, 
                      implicacoes = implicacoes, 
                      status = status, data = data, prazo = prazo)
    lista_ocorrencias.append(ocorrencia)
    print("Ocorrência cadastrada com sucesso!")
    gravaOcorrencia(ocorrencia)

def listagem(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências---")
        for i in range(tamanho):
           impressao_ocorrencia(lista_ocorrencias[i], i)  
    else:
        print("Não existem ocorrências cadastradas.")
    
def listagem_ativas(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências ativas---")
        existem_ativas = False
        for i in range(tamanho):
            if lista_ocorrencias[i]["status"] == True:
                impressao_ocorrencia(lista_ocorrencias[i], i)
                existem_ativas = True
        if not existem_ativas:
            print("Não existem ocorrências ativas")
                
    else:
        print("Não existem ocorrências cadastradas.")

def impressao_ocorrencia(ocorrencia, i):
    print("###Ocorrência ", i + 1, "###")
    print("Id:", ocorrencia["id"])
    print("Título:",ocorrencia["titulo"])
    print("Descrição:",ocorrencia["descricao"])
    print("Implicações:",ocorrencia["implicacoes"])
    print("Status:", "sim" if ocorrencia["status"] == True else "não")
    print("Data de inclusão: ", ocorrencia["data"])
    print("Prazo (em dias):", ocorrencia["prazo"])

def buscar_ocorrencia(lista_ocorrencias, titulo):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        for i in range(tamanho):
            if lista_ocorrencias[i]["titulo"] == titulo:
                return i
        return -1
    else:
        return -1

def buscar_ocorrencia_mes(lista_ocorrencias, mes):
    tamanho = len(lista_ocorrencias)
    lista_mes = []
    if tamanho > 0:
        for i in range(tamanho):
            corte_mes = lista_ocorrencias[i]["data"]
            if corte_mes[3:5] == mes:
                lista_mes.append(lista_ocorrencias[i])
        return lista_mes
    else:
        return lista_mes

def buscar_ocorrencia_palavra(lista_ocorrencias, titulo):
    tamanho = len(lista_ocorrencias)
    lista_occ = []
    if tamanho > 0:
        for i in range(tamanho):
            if titulo in lista_ocorrencias[i]["titulo"]:
                lista_occ.append(lista_ocorrencias[i])
        return lista_occ
    else:
        return lista_occ

def gravaOcorrencia(ocorrencia):
    arquivo = open("ocorrencias.txt", "a", encoding="utf-8")
    arquivo.write("Id:" + str(ocorrencia["id"]) + "\n")
    arquivo.write("Título:" + ocorrencia["titulo"] + "\n")
    arquivo.write("Descrição:" + ocorrencia["descricao"] + "\n")
    arquivo.write("Implicações:" + ocorrencia["implicacoes"] + "\n")
    status = "sim" if ocorrencia["status"] == True else "não"
    arquivo.write("Status:"+ status + "\n" )
    arquivo.write("Data de inclusão:" + ocorrencia["data"] + "\n")
    arquivo.write("Prazo (em dias):" + str(ocorrencia["prazo"]) + "\n")
    arquivo.close()

def regravarArquivo(lista_ocorrencias):
    arquivo = open("ocorrencias.txt", "w", encoding="utf-8")
    for ocorrencia in lista_ocorrencias:
        gravaOcorrencia(ocorrencia)
    arquivo.close()

def carregar_ocorrencias():
    count = 1
    arquivo = open("ocorrencias.txt", "r", encoding="utf-8")
    lista_ocorrencias = []
    for i in arquivo:
        id = i #arquivo.readline()
        titulo = arquivo.readline()
        descricao = arquivo.readline()
        implicacoes = arquivo.readline()
        status = arquivo.readline()
        data = arquivo.readline()
        prazo = arquivo.readline()

        ocorrencia = dict(
            id = id[3:len(id)-1],
            titulo = titulo[7: len(titulo)-1], 
            descricao = descricao[10:len(descricao)-1],
            implicacoes = implicacoes[12:len(implicacoes)-1],
            status = True if status[7:len(status)] == "sim\n" else False,
            data = data[17:len(data)-1],
            prazo = prazo[16:len(prazo)-1]
        )
        count += int(ocorrencia["id"]) + 1
        lista_ocorrencias.append(ocorrencia)
    arquivo.close()
    return lista_ocorrencias, count

lista_ocorrencias, cout =carregar_ocorrencias()
menu_simples()