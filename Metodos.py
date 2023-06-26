from operacoesbd import *
#METÓDOS GLOBAIS
def VerificarListaVazia(conexao):
    consultarlistagem = 'select count(*) from manifestacoes'
    listar = listarBancoDados(conexao, consultarlistagem)
    return listar

def TipoCodparaNome(i):
    if i == 1:
        TipoNome = 'RECLAMAÇÃO'
    elif i == 2:
        TipoNome = 'ELÓGIOS'
    elif i == 3:
        TipoNome = 'SUGESTÕES'
    else:
        TipoNome = 'NÃO CADASTRADO'
    return TipoNome

def SituacaoCodParaNome(i):
    if i == 0:
        situacao = 'ABERTA'
    else:
        situacao = 'ENCERRADA'
    return situacao


#LISTAR
def ListarporSituacao(conexao,opcaolistar):
    if opcaolistar == 1:
        status = '0'
        statusNome = 'ABERTAS'
    elif opcaolistar == 2:
        status = '1'
        statusNome = 'ENCERRADAS'
    if opcaolistar == 1 or opcaolistar == 2:
        consultarlistagem = 'select * from manifestacoes where situacao=' + status
        listar = listarBancoDados(conexao, consultarlistagem)
        if len(listar) == 0:
            listagem='APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS'
        else:
            listagem=(listar,statusNome)
        return listagem

def ListarPorTipo(conexao,tipo):
    consultarlistagem = 'select * from manifestacoes where tipo=' + str(tipo)
    listar = listarBancoDados(conexao, consultarlistagem)
    if len(listar) == 0:
        listar='NO MOMENTO NÃO HÁ MANIFESTAÇÕES COM TIPO PESQUISADO'
    return listar


#REGISTRAR
def InserirManifestacao(conexao, values):
    # DEFININDO SQL
    insercaoSQL = 'insert into manifestacoes (titulo,descricao,autor,tipo,situacao) values(%s,%s,%s,%s,%s)'
    # DEFININDO VALORES, OBS: A SITUAÇÃO É "0" POR SE REFERIR A SITUAÇÃO:ABERTA
    insertNoBancoDados(conexao, insercaoSQL, values)
    return True  # SAINDO DO WHILE


#PESQUISAR POR CÓD.
def pesquisarPorCodigo(conexao,cod):
    consultarlistagem = 'select * from manifestacoes where cod=' + cod
    listar = listarBancoDados(conexao, consultarlistagem)
    if len(listar) == 0:
        listar='MANIFESTAÇÃO NÃO ENCONTRADA'
    return listar


#ALTERAR
def VerificarManifestacaoAberta(conexao):
    consultarlistagem = 'select count(*) from manifestacoes where situacao=0'
    listar = listarBancoDados(conexao, consultarlistagem)
    return listar

def pesquisarPorCodAberta(conexao,cod):
    consultarlistagem = 'select * from manifestacoes where cod=' + cod + ' and situacao=0'
    listar = listarBancoDados(conexao, consultarlistagem)
    if len(listar) == 0:
        listar='MANIFESTAÇÃO NÃO ENCONTRADA'
    return listar

def definirAlteracoes(conexao,opcaoAlterar,cod):
    if opcaoAlterar == 1:
        print('Qual o novo titulo da manifestação?')
        novoTitulo = input('->')
        antes = 'titulo'
        print()

    elif opcaoAlterar == 2:
        print('Qual a nova descrição da manifestação?')
        novaDescricao = input('->')
        antes = 'descricao'
        print()

    elif opcaoAlterar == 3:
        print('Qual o novo titulo da manifestação?')
        novoTitulo = input('->')
        print()
        print('Qual a nova descrição da manifestação?')
        novaDescricao = input('->')
        antes = 'titulo,descricao'
        print()

    consultarlistagem = 'select ' + antes + ' from manifestacoes where cod=' + cod
    manifestacaoantes = listarBancoDados(conexao, consultarlistagem)

    if opcaoAlterar == 1:
        alteracoes = (novoTitulo,)
        alteracoesColuna = 'titulo = %s'
        printalteracao = f'NOVO TITULO: {novoTitulo}'
        printantes = f'TITULO={manifestacaoantes[0][0]}'

    elif opcaoAlterar == 2:
        alteracoes = (novaDescricao,)
        alteracoesColuna = 'descricao = %s'
        printalteracao = f'NOVA DESCRIÇÃO: {novaDescricao}'
        printantes = f'DESCRIÇÃO={manifestacaoantes[0][1]}'

    elif opcaoAlterar == 3:
        alteracoes = (novoTitulo, novaDescricao)
        alteracoesColuna = 'titulo = %s,descricao = %s'
        printalteracao = f'NOVO TITULO: {novoTitulo} | NOVA DESCRIÇÃO: {novaDescricao}'
        printantes = f'TITULO={manifestacaoantes[0][0]} | DESCRIÇÃO={manifestacaoantes[0][1]}'

    padroes=(printalteracao, printantes, alteracoes, alteracoesColuna)
    return padroes

def AlterandoManifestacao(conexao,padroes,cod):
    atualizarSQL = 'update manifestacoes set ' + padroes[3] + ' where cod=' + cod
    atualizarBancoDados(conexao, atualizarSQL, padroes[2])

def EncerrarManifestacao(conexao, cod):
    situacao = (1,)
    atualizarSQL = 'update manifestacoes set situacao = %s where cod =' + cod
    atualizarBancoDados(conexao, atualizarSQL, situacao)


#EXCLUIR
def DeletarManifestacao(conexao,cod):
    deletarSQL = 'delete from manifestacoes where cod=%s'  # SQL PARA DELETAR PELO COD.
    values = (cod,)  # DEFININDO VALUES COMO COD
    excluirBancoDados(conexao, deletarSQL, values)  # EXCLUINDO NO BD