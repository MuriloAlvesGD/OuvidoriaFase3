'''
SISTEMA DE OUVIDORIA 2023 FASE 2

ALUNOS:
MURILO DOS SANTOS ALVES
DEMOSTENES DINIZ PORTO
DARLAN SADRAQUE
VALDEMIR DOMINGOS DA SILVA JÚNIOR
FELIPE RODRIGUES HONÓRIO
DAYANE RODRIGUES HONÓRIO

#IMPORTANTE:Em TODO O CÓDIGO A TABELA USADA DENTRO DO BANCO DE DADOS É "manifestacoes"

A TABELA É CRIADA NO MySQL DENTRO DO BANCO DE DADOS

COMANDO:
create table manifestacoes (
cod int auto_increment,
titulo varchar(150),
descricao varchar(500),
autor varchar(150),
tipo int,
situacao int,
primary key (cod)
);

LEMBRE-SE ANTES DE UTILIZAR O CÓDIGO, DE CRIAR A TABELA 'manifestacoes' no MySQL dentro do Banco de Dados que for usar
e inserir o acesso e Banco de Dados em 'abrirBancoDados'. Faça isso para pelo funcionamento do código.
'''

from operacoesbd import *

listar=[]
opcao=0
         #abrirBancoDados(host,usuario,senha,bancodedados)
conexao = abrirBancoDados('localhost','root','2468','projetofase2') #ABRIR CONEXÃO COM O BANCO DE DADOS
while opcao!=7:
    print('SISTEMA DE OUVIDORIA')
    print()
    #MENU DO SISTEMA
    #OBS: "LISTAR POR TIPO" ESTÁ DENTRO DO MENU - LISTAR MANIFESTAÇÕES
    print('''MENU
1) LISTAR MANIFESTAÇÕES
2) REGISTRAR NOVA MANIFESTAÇÃO
3) EXIBIR QUANTIDADE DE MANIFESTAÇÕES
4) PESQUISAR MANIFESTAÇÃO POR CÓD.
5) ALTERAR MANIFESTAÇÃO
6) EXCLUIR MANIFESTAÇÃO
7) SAIR DO SISTEMA''')
    print()
    opcao=int(input('Vamos lá, o que deseja fazer? '))
    if opcao==1: #LISTAR MANIFESTAÇÕES
        opcaolistar=0
        while opcaolistar !=4:
            print()
            print('MENU - LISTAR MANIFESTAÇÕES')
            print('''
1) LISTAR MANIFESTAÇÕES ABERTAS
2) LISTAR MANIFESTAÇÕES ENCERRADAS
3) LISTAR MANIFESTAÇÕES POR TIPO
4) VOLTAR PARA O MENU
            ''')
            opcaolistar=int(input('->'))
            print()
            #definindo qual lista vai puxar pelo status/situação
            if opcaolistar==1:
                status='0'
                statusNome='ABERTAS'
            elif opcaolistar==2:
                status='1'
                statusNome='ENCERRADAS'
            # MESMO PROCEDIMENTO PARA AMBAS A LISTA (ABERTAS E ENCERRADAS)
            if opcaolistar==1 or opcaolistar==2:
                consultarlistagem='select * from manifestacoes where situacao='+ status #PUXA A SITUAÇÃO DEFINIDA ANTES
                listar=listarBancoDados(conexao, consultarlistagem)
                if len(listar)==0:
                    print('APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS')
                else: #SE HOUVER MANIFESTAÇÕES PROSSEGUE PARA PRINTAR
                    # INFORMANDO A SITUAÇÃO DAS MANIFESTAÇÕES QUE PUXOU
                    print(f'Essas são as MANIFESTAÇÕES {statusNome} presentes no banco de dados:')
                    for i in listar: #PRINTANDO CADA MANIFESTAÇÃO
                        #VERIFICANDO O TIPO DA MANIFESTAÇÃO E ASSOCIANDO UM NOME PARA CADA NÚMERO
                        if i[4]==1:
                            TipoNome='RECLAMAÇÃO'
                        elif i[4]==2:
                            TipoNome='ELÓGIOS'
                        elif i[4]==3:
                            TipoNome='SUGESTÕES'
                        else:
                            TipoNome='NÃO CADASTRADO'
                        #PRINTANDO OS RESULTADOS
                        print(f'CÓD.{i[0]} | TITULO={i[1]} | AUTOR={i[3]} |TIPO={TipoNome}')
            # PESQUISANDO MANIFESTAÇÕES POR TIPO
            elif opcaolistar==3:
                consultarlistagem='select * from manifestacoes' #VERIFICANDO SE EXISTE MANIFESTAÇÕES NO BD
                listar=listarBancoDados(conexao, consultarlistagem)
                if len(listar)==0:
                    print('APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS')
                else: #SÓ ENTRA SE TIVER MANIFESTAÇÃO CADASTRADA
                    tipoPesquisar=0
                    while tipoPesquisar!=4: #ENTRANDO NO MENU DOS TIPOS
                        print()
                        print('''TIPOS DE MANIFESTAÇÕES
1) RECLAMAÇÃO
2) ELÓGIOS
3) SUGESTÕES
4) VOLTAR''')
                        tipoPesquisar=int(input('Quais manifestações deseja ver? '))
                        print()
                        if tipoPesquisar in (1, 2, 3): #MESMO CÓDIGO PARA AS TRÊS MANIFESTAÇÕES
                            # O CÓDIGO APRESENTADO NA LISTA É IGUAL O DO BD
                            consultarlistagem='select * from manifestacoes where tipo=' + str(tipoPesquisar)
                            listar=listarBancoDados(conexao, consultarlistagem)
                            if len(listar)==0: #VERIFICANDO SE HÁ MANIFESTAÇÃO COM O TIPO PESQUISADO
                                print('NO MOMENTO NÃO HÁ MANIFESTAÇÕES COM TIPO PESQUISADO')
                            else: #PRINTANDO AS MANIFESTAÇÕES
                                if tipoPesquisar == 1:
                                    TipoNome = 'RECLAMAÇÃO'
                                elif tipoPesquisar == 2:
                                    TipoNome = 'ELÓGIOS'
                                elif tipoPesquisar == 3:
                                    TipoNome = 'SUGESTÕES'
                                else:
                                    TipoNome = 'NÃO CADASTRADO'
                                print(f'Essas são as manifestações existentes com o tipo {TipoNome}:')
                                for i in listar:
                                    if i[5] == 0:
                                        situacao = 'ABERTA'
                                    else:
                                        situacao = 'ENCERRADA'
                                    print()
                                    print(f'CÓD.{i[0]} | TITULO: {i[1]} | AUTOR: {i[3]} | SITUAÇÃO:{situacao}')
                        elif tipoPesquisar !=4:
                            print('OPÇÃO INVÁLIDA OU INEXISTENTE')
            elif opcaolistar!=4:
                print('OPÇÃO INVÁLIDA OU INEXISTENTE')
    elif opcao==2:
        inserirmanifestacao=0
        while inserirmanifestacao!=2:
            print()
            print('MENU - REGISTRAR NOVA MANIFESTAÇÃO')
            print()
            print('Deseja registrar uma nova MANIFESTAÇÃO?')
            print('1) SIM QUERO REGISTRAR')
            print('2) NÃO, VOLTAR PARA O MENU')
            inserirmanifestacao=int(input('->'))#CONFIRMAR SE QUER REGISTRAR UMA MANIFESTAÇÃO
            if inserirmanifestacao==1:
                print()
                print('Siga o processo a seguir:')
                validacaomanifestacao=0
                while validacaomanifestacao!=1:
                    validacaotipo=False
                    while validacaotipo==False: #Verificação de tipo válido, só avança caso aprovado
                        print()
                        print('De qual tipo é a sua manifestação? ')
                        print('''1) RECLAMAÇÃO
2) ELÓGIOS
3) SUGESTÕES ''')
                        tipo=int(input('->'))
                        if tipo in (1, 2, 3):
                            validacaotipo=True
                            print('TIPO INSERIDO É VÁLIDO')
                        else:
                            print('TIPO INSERIDO É INVÁLIDO')
                    #DEFININDO VARIAVEL COM O NOME DO TIPO PARA O USÚARIO VERIFICAR POSTERIORMENTE
                    if tipo == 1:
                        TipoNome = 'RECLAMAÇÃO'
                    elif tipo == 2:
                        TipoNome = 'ELÓGIOS'
                    elif tipo == 3:
                        TipoNome = 'SUGESTÕES'
                    #COLHENDO OS DADOS PARA INSERIR A MANIFESTAÇÃO
                    print()
                    print('Qual o seu nome?')
                    autor = input('->')
                    print()
                    print('Qual o título da manifestação?')
                    titulo=input('->')
                    print()
                    print('Insira a descrição da sua manifestação:')
                    descricao=input('->')
                    print()
                    #EXIBINDO A MANIFESTAÇÃO
                    print('Por gentileza, confirme as informações inseridas:')
                    print(f'Tipo da Manifestação: {TipoNome}')
                    print(f'Autor da Manifestação: {autor}')
                    print(f'Titulo da Manifestação: {titulo}')
                    print(f'Descrição da Manifestação: {descricao}')
                    print()
                    #CONFIRMANDO SE DESEJA INSERIR A MANIFESTAÇÃO
                    confirmacao=False
                    while confirmacao==False:
                        print('''Deseja inserir a manifestação com os dados apresentados?
        1) SIM, EU QUERO INSERIR
        2) NÃO, EU QUERO INSERIR UMA OUTRA MANIFESTAÇÃO
        3) VOLTAR''')
                        validacaomanifestacao=int(input('->'))
                        if validacaomanifestacao==1: #SE SIM, CONTINUA O PROCESSO E DEPOIS VOLTA PARA O MENU
                            # DEFININDO SQL
                            insercaoSQL = 'insert into manifestacoes (titulo,descricao,autor,tipo,situacao) values(%s,%s,%s,%s,%s)'
                            # DEFININDO VALORES, OBS: A SITUAÇÃO É "0" POR SE REFERIR A SITUAÇÃO:ABERTA
                            values = (titulo, descricao, autor, tipo, 0)
                            insertNoBancoDados(conexao, insercaoSQL, values)
                            print()
                            print('MANIFESTAÇÃO INSERIDA COM  SUCESSO!!')
                            confirmacao=True #SAINDO DO WHILE
                        elif validacaomanifestacao==2: #SAI DO WHILE DE CONFIRMAÇÃO E REINICIA O PROCESSO DE INSERÇÃO
                            print('Por favor, insira as informações que deseja:')
                            confirmacao=True
                        elif validacaomanifestacao==3: #VOLTANDO PARA O MENU
                            confirmacao=True
                            validacaomanifestacao=1 #SAI DO WHILE DO PROCESSO DE INSERÇÃO DA MANIFESTAÇÃO
                        elif validacaomanifestacao!=3:
                            print('OPÇÃO INVÁLIDA OU INEXISTENTE')
            elif inserirmanifestacao!=2:
                print('OPÇÃO INVÁLIDA OU INEXISTENTE')
    elif opcao==3:
        print('QUANTIDADE DE MANIFESTAÇÕES')
        print()
        consultarlistagem = 'select count(*) from manifestacoes'
        listar = listarBancoDados(conexao, consultarlistagem)
        print(f'TOTAL DE MANIFESTAÇÕES: {listar[0][0]}')
        consultarlistagem = 'select count(*) from manifestacoes where situacao=0'
        listar = listarBancoDados(conexao, consultarlistagem)
        print(f'TOTAL DE MANIFESTAÇÕES ABERTAS: {listar[0][0]}')
        consultarlistagem = 'select count(*) from manifestacoes where tipo=1 and situacao=0'
        listar = listarBancoDados(conexao, consultarlistagem)
        print(f'QUANTIDADE DE RECLAMAÇÕES ABERTAS: {listar[0][0]}')
        consultarlistagem = 'select count(*) from manifestacoes where tipo=2 and situacao=0'
        listar = listarBancoDados(conexao, consultarlistagem)
        print(f'QUANTIDADE DE ELÓGIOS ABERTOS: {listar[0][0]}')
        consultarlistagem = 'select count(*) from manifestacoes where tipo=3 and situacao=0'
        listar = listarBancoDados(conexao, consultarlistagem)
        print(f'QUANTIDADE DE SUGESTÕES ABERTAS: {listar[0][0]}')
        consultarlistagem = 'select count(*) from manifestacoes where situacao=1'
        listar = listarBancoDados(conexao, consultarlistagem)
        print(f'TOTAL DE MANIFESTAÇÕES ENCERRADAS: {listar[0][0]}')
        print()
    elif opcao==4:
        opcaopesquisar=0
        while opcaopesquisar!=2:
            print()
            print('MENU - PESQUISAR POR CÓDIGO')
            print()
            print('''1)PESQUISAR MANIFESTAÇÃO
2) SAIR/VOLTAR PARA O MENU''')
            opcaopesquisar=int(input('->'))
            if opcaopesquisar==1:
                consultarlistagem = 'select * from manifestacoes' #VERIFICANDO SE EXISTE MANIFESTAÇÕES NO BD
                manifestacao = listarBancoDados(conexao, consultarlistagem)
                if len(manifestacao) == 0:
                    print()
                    print('APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS')
                else: #SE HOUVER MANIFESTAÇÃO NO BD ENTRA PARA A PESQUISA
                    print()
                    print('Informe o código da manifestação')
                    cod=input('->')
                    # VERIFICANDO SE EXISTE MANIFESTAÇÃO COM O CÓDIGO INFORMADO
                    consultarlistagem='select * from manifestacoes where cod='+cod
                    manifestacao=listarBancoDados(conexao, consultarlistagem)
                    if len(manifestacao)==0:
                        print()
                        print('MANIFESTAÇÃO NÃO ENCONTRADA')
                    else: #CASO EXISTA ELE IRÁ MOSTRAR TODOS OS DADOS DA MANIFESTAÇÃO
                        print()
                        print(f'O cód.{cod}, está associado a seguinte manifestação:')
                        #VERIFICANDO A SITUAÇÃO DA MANIFESTAÇÃO
                        if manifestacao[0][5]==0:
                            situacao='ABERTA'
                        else:
                            situacao='ENCERRADA'
                        #VERIFICANDO O TIPO DA MANIFESTAÇÃO
                        if manifestacao[0][4] == 1:
                            TipoNome = 'RECLAMAÇÃO'
                        elif manifestacao[0][4] == 2:
                            TipoNome = 'ELÓGIOS'
                        elif manifestacao[0][4] == 3:
                            TipoNome = 'SUGESTÕES'
                        else:
                            TipoNome = 'NÃO CADASTRADO'
                        #IMPRIMINDO A MANIFESTAÇÃO
                        print()
                        print(f'SITUAÇÃO:{situacao}')
                        print(f'TIPO: {TipoNome}')
                        print(f'AUTOR: {manifestacao[0][3]}')
                        print(f'TITULO: {manifestacao[0][1]}')
                        print(f'DESCRIÇÃO:{manifestacao[0][2]}')
            elif opcaopesquisar !=2:
                print('OPÇÃO ESCOLHIDA É INVÁLIDA OU INEXISTENTE')
    elif opcao==5:
        opcaomodificar=0
        while opcaomodificar!=3:
            print()
            print('MENU - ALTERAR MANIFESTAÇÃO')
            print()
            print('O que deseja fazer?')
            print('1) ALTERAR MANIFESTAÇÃO ABERTA')
            print('2) MARCAR MANIFESTAÇÃO COMO ENCERRADA')
            print('3) SAIR/VOLTAR PARA O MENU')
            opcaomodificar = int(input('-> '))
            print()
            #ALTERAR MANIFESTAÇÃO ABERTA
            if opcaomodificar==1:
                #VERIFICANDO SE EXISTE MANIFESTAÇÕES NO BANCO DE DADOS
                consultarlistagem='select * from manifestacoes where situacao=0'
                listar=listarBancoDados(conexao, consultarlistagem)
                if len(listar)==0:
                    print('NO MOMENTO NÃO HÁ MANIFESTAÇÃO ABERTA')
                else:#SÓ ENTRARÁ NO PROXIMO MENU SE EXISTIR MANIFESTAÇÕES NO BANCO DE DADOS
                    opcaoAlterar=0
                    while opcaoAlterar != 4: #MENU DE ALTERAÇÕES POSSIVEIS
                        print('''O QUE DESEJA ALTERAR?
1) TITULO
2) DESCRIÇÃO
3) TITULO + DESCRIÇÃO
4) VOLTAR
''')
                        opcaoAlterar = int(input('->'))
                        print()
                        if opcaoAlterar in (1, 2, 3):
                            cod = input('Qual o código da ocorrência que deseja alterar?')
                            #VERIFICANDO EXISTÊNCIA DA MANIFESTAÇÃO NO BANCO DE DADOS
                            consultarlistagem = 'select * from manifestacoes where cod=' + cod + 'and situacao=0'
                            manifestacao = listarBancoDados(conexao, consultarlistagem)
                            if len(manifestacao) == 0: #CASO NÃO ENCONTRE A VARIAVEL manifestacao FICA VAZIA
                                print()
                                print('MANIFESTAÇÃO NÃO ENCONTRADA')
                            else:
                                #SALVANDO VARIAVEIS PARA ALTERAÇÃO
                                if opcaoAlterar == 1 or opcaoAlterar == 3:
                                    print('Qual o novo titulo da manifestação?')
                                    novoTitulo = input('->') #TITULO
                                    print()
                                if opcaoAlterar == 2 or opcaoAlterar == 3:
                                    print('Qual a nova descrição da manifestação?')
                                    novaDescricao = input('->') #DESCRIÇÃO
                                    print()
                                #DEFININDO ALTERAÇÕES E OPÇÕES DE AMOSTRAGEM
                                if opcaoAlterar == 1: #APENAS TITULO
                                    alteracoes = (novoTitulo,)
                                    alteracoesColuna='titulo = %s' #DEEFININDO COLUNA A SER ALTERADA NO SQL
                                    antes = 'titulo'
                                    printalteracao= f'NOVO TITULO: {novoTitulo}'
                                    printantes = f'TITULO={manifestacaoantes[0][0]}'
                                elif opcaoAlterar == 2: #APENAS DESCRIÇÃO
                                    alteracoes = (novaDescricao,)
                                    alteracoesColuna = 'descricao = %s' #DEEFININDO COLUNA A SER ALTERADA NO SQL
                                    antes = 'descricao'
                                    printalteracao = f'NOVA DESCRIÇÃO: {novaDescricao}'
                                    printantes = f'DESCRIÇÃO={manifestacaoantes[0][1]}'
                                elif opcaoAlterar == 3: #DESCRIÇÃO E TITULO
                                    alteracoes = (novoTitulo, novaDescricao)
                                    # DEEFININDO COLUNA A SER ALTERADA NO SQL
                                    alteracoesColuna = 'titulo = %s,descricao = %s'
                                    antes = 'titulo,descricao'
                                    printantes=f'TITULO={manifestacaoantes[0][0]} | DESCRIÇÃO={manifestacaoantes[0][1]}'
                                    printalteracao=f'NOVO TITULO: {novoTitulo} | NOVA DESCRIÇÃO: {novaDescricao}'
                                #BUSCANDO DADOS ORIGINAIS E COMPARANDO AMBOS
                                # DEFININDO O SQL DE CONSULTA
                                consultarlistagem = 'select '+antes+' from manifestacoes where cod='+cod
                                manifestacaoantes = listarBancoDados(conexao, consultarlistagem) #BUSCANDO OS DADOS
                                print('ABAIXO ESTÁ A MANIFESTAÇÃO REGISTRADA:')
                                print(printantes)
                                # O printantes FOI DEFINIDO ANTERIORMENTE COM BASE NA OPÇÃO PARA NÃO GERAR CONFLITO
                                # UMA VEZ QUE PEDE DADOS DE COLUNAS DIFERENTES
                                print()
                                print('ESSA É A MANIFESTAÇÃO ALTERADA')
                                print(printalteracao) #MESMA QUESTÃO DO printantes JÁ QUE É UM OU OUTRO OU OS DOIS
                                confirmacao=0
                                while confirmacao!=2: #CONFIRMAR A ALTERAÇÃO
                                    print()
                                    print('DESEJA REALIZAR A ALTERAÇÃO?')
                                    print('1) SIM')
                                    print('2) NÃO')
                                    confirmacao=int(input('->'))
                                    if confirmacao==1: #CONFIRMAÇÃO=SIM
                                        # DEFININDO SQL DE ATUALIZAÇÃO
                                        atualizarSQL = 'update manifestacoes set '+alteracoesColuna+' where cod=' + cod
                                        valores= alteracoes #DEFININDO VALORES
                                        atualizarBancoDados(conexao, atualizarSQL, valores) #ATUALIZANDO BANCO DE DADOS
                                        print()
                                        print('MANIFESTAÇÃO ALTERADA COM SUCESSO')
                                        confirmacao=2 #ALTERANDO PARA SAIR DO LOOP/WHILE
                                    elif confirmacao==2: #CONFIRMAÇÃO=NÃO, VOLTA PARA AS OPÇÕES DE ALTERAÇÃO
                                        print()
                                        print('OK NÃO ALTERAMOS A MANIFESTAÇÃO')
                                        print()
                                    elif confirmacao!=2: #OPÇÃO DE CONFIRMAÇÃO INVÁLIDA
                                        print()
                                        print('OPÇÃO INVÁLIDA OU INEXISTENTE')
                                        print()
                        elif opcaoAlterar !=4:
                            print()
                            print('OPÇÃO INVÁLIDA OU INEXISTENTE')
                            print()
            #MARCAR MANIFESTAÇÃO COMO ENCERRADA
            elif opcaomodificar==2:
                consultarlistagem='select * from manifestacoes where situacao=0'
                listar=listarBancoDados(conexao, consultarlistagem)
                if len(listar)==0: #VERIFICANDO EXISTÊNCIA DE MANIFESTAÇÕES COM SITUAÇÃO EM ABERTO
                    print('NO MOMENTO NÃO HÁ MANIFESTAÇÕES EM ABERTO')
                else:#ENCERRANDO MANIFESTAÇÃO. OBS: SÓ ENTRARÁ SE HOUVER MANIFESTAÇÕES EM ABERTO
                    Encerrar=0
                    while Encerrar!=3: #LOOP PARA CONFIRMAÇÃO
                        print('QUAL O CÓDIGO DA MANIFESTAÇÃO QUE DESEJA ENCERRAR?')
                        cod = input('->')
                        # CONSULTA SE O COD PESQUISADO É DE UMA MANIFESTAÇÃO COM SITUAÇÃO EM ABERTO/0
                        consultarlistagem = 'select * from manifestacoes where cod ='+cod+' and situacao=0'
                        manifestacao = listarBancoDados(conexao, consultarlistagem)
                        if len(manifestacao) == 0:
                            print()
                            print('MANIFESTAÇÃO NÃO ENCONTRADA')
                        else:#MOSTRANDO A MANIFESTAÇÃO QUE FOI PESQUISADA
                            print()
                            print('Por gentileza, confirma a manifestação que deseja encerrar:')
                            #DO IF ATÉ O ELSE TRANSFORMA O TIPO DE NUMERO PARA A PALAVRA CORRESPONDENTE NA AMOSTRAGEM
                            if manifestacao[0][4] == 1:
                                TipoNome = 'RECLAMAÇÃO'
                            elif manifestacao[0][4] == 2:
                                TipoNome = 'ELÓGIOS'
                            elif manifestacao[0][4] == 3:
                                TipoNome = 'SUGESTÕES'
                            else:
                                TipoNome = 'NÃO CADASTRADO'
                            print() #PRINTANDO OS ITENS
                            print(f'TIPO: {TipoNome}')
                            print(f'AUTOR: {manifestacao[0][3]}')
                            print(f'TITULO: {manifestacao[0][1]}')
                            print(f'DESCRIÇÃO:{manifestacao[0][2]}')
                            print()
                            while confirmacaoEncerrar!=3: #CONFIRMANDO SE QUER ENCERRAR
                                print('Realmente deseja marcar como encerrada essa manifestação? ')
                                print('1) SIM QUERO ENCERRAR')
                                print('2) QUERO MARCAR OUTRA COMO ENCERRADA')
                                print('3) SAIR/VOLTAR PARA O MENU')#VOLTA PARA O MENU DE ALTERAÇÕES
                                confirmacaoEncerrar=int(input('->'))
                                if confirmacaoEncerrar==1: #PASSANDO DE ABERTA PARA ENCERRADA
                                    situacao=(1,)
                                    #ALTERANDO A SITUAÇÃO DA MANIFESTAÇÃO, 1=ENCERRADA, 0=ABERTA
                                    atualizarSQL='update manifestacoes set situacao = %s where cod ='+cod
                                    atualizarBancoDados(conexao, atualizarSQL, situacao)
                                    Encerrar=3 #SAINDO DOS WHILE
                                    print('A MANIFESTAÇÃO FOI MARCADA COMO CONCLUÍDA')
                                elif confirmacaoEncerrar==2:
                                    print('INSIRA NOVAMENTE O CÓDIGO DA MANIFESTAÇÃO')
                                    confirmacaoEncerrar=3 #SAIR DO WHILE DE CONFIRMAÇÃO, MAS NÃO VOLTA PARA O MENU
                                elif confirmacaoEncerrar==3: #VOLTA PARA O MENU DE ALTERAR MANIFESTAÇÃO
                                    Encerrar=3
                                elif confirmacaoEncerrar!=3:
                                    print('A OPÇÃO É INVÁLIDA OU INEXISTENTE')
            elif opcaomodificar!=3:
                print('OPÇÃO INVÁLIDA OU INEXISTENTE')
    elif opcao==6:
        opcaodeletar=0
        while opcaodeletar!=2:
            print()
            print('MENU - EXCLUIR MANIFESTAÇÃO')
            print('''
1) EXCLUIR MANIFESTAÇÃO 
2) VOLTAR PARA O MENU''')
            opcaodeletar=int(input('->'))
            print()
            if opcaodeletar==1:
                consultarlistagem = 'select * from manifestacoes' #CONSULTANDO EXISTÊNCIA DE MANIFESTAÇÕES NO BD
                listar = listarBancoDados(conexao, consultarlistagem)
                if len(listar) == 0:
                    print('APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS NO BANCO DE DADOS')
                else: #SÓ ENTRA SE TIVER MANIFESTAÇÃO NO BD
                    confirmacaoDeletar=0
                    while confirmacaoDeletar!=3: #PESQUISANDO A MANIFESTAÇÃO PELO COD. E DELETANDO
                        print('QUAL O CÓDIGO DA MANIFESTAÇÃO QUE DESEJA DELETAR?')
                        cod = input('->')
                        # VERIFICANDO SE EXISTE MANIFESTAÇÃO COM O COD PESQUISADO
                        consultarlistagem = 'select * from manifestacoes where cod=' + cod
                        manifestacao = listarBancoDados(conexao, consultarlistagem)
                        if len(manifestacao) == 0: #SE NÃO HOUVER CÓD ELE PEDE NOVAMENTE PARA INSERIR UM CÓD.
                            print()
                            print('MANIFESTAÇÃO NÃO ENCONTRADA')
                            print()
                        else: #ENCONTRADO A MANIFESTAÇÃO COM O CÓD. INFORMADA
                            print()
                            print('Por gentileza, confirme se essa é a manifestação que deseja deletar:')
                            if manifestacao[0][5] == 0:
                                situacao = 'ABERTA'
                            else:
                                situacao = 'ENCERRADA'
                            if manifestacao[0][4] == 1:
                                TipoNome = 'RECLAMAÇÃO'
                            elif manifestacao[0][4] == 2:
                                TipoNome = 'ELÓGIOS'
                            elif manifestacao[0][4] == 3:
                                TipoNome = 'SUGESTÕES'
                            else:
                                TipoNome = 'NÃO CADASTRADO'
                            print()
                            print(f'SITUAÇÃO:{situacao}')
                            print(f'TIPO: {TipoNome}')
                            print(f'AUTOR: {manifestacao[0][3]}')
                            print(f'TITULO: {manifestacao[0][1]}')
                            print(f'DESCRIÇÃO:{manifestacao[0][2]}')
                            print()
                            confirmacao=0
                            while confirmacao!=3:
                                print('Realmente deseja deletar essa manifestação? ')
                                print('1) SIM QUERO DELETAR')
                                print('2) QUERO DELETAR OUTRA')
                                print('3) SAIR PARA O MENU')
                                confirmacao = int(input('->'))
                                if confirmacao == 1: #DELETANDO MANIFESTAÇÃO
                                    deletarSQL = 'delete from manifestacoes where cod=%s' #SQL PARA DELETAR PELO COD.
                                    values=(cod,) #DEFININDO VALUES COMO COD
                                    excluirBancoDados(conexao, deletarSQL, values) #EXCLUINDO NO BD
                                    confirmacao=3 #SAINDO DO WHILE
                                    confirmacaoDeletar = 3 #SAINDO PARA O MENU
                                    print('A MANIFESTAÇÃO FOI DELETADA')
                                elif confirmacao == 2: #RETORNANDO PARA O TOPO E PEDINDO NOVAMENTE O CÓD.
                                    print('INSIRA NOVAMENTE O CÓDIGO DA MANIFESTAÇÃO')
                                    confirmacao=3 #SAI DO WHILE DE CONFIRMACAO MAS NÃO VOLTA PARA O MENU
                                    print()
                                elif confirmacao==3: #VOLTA PARA O MENU
                                    confirmacaoDeletar=3
                                elif confirmacaoDeletar != 3:
                                    print('A OPÇÃO É INVÁLIDA OU INEXISTENTE')
            elif opcaodeletar!=2:
                print('A OPÇÃO É INVÁLIDA OU INEXISTENTE')
    elif opcao!=7:
        print('OPÇÃO INVÁLIDA OU INEXISTENTE')
print()
print('OBRIGADO POR UTILIZAR O NOSSO SISTEMA')
encerrarBancoDados(conexao)
