'''
SISTEMA DE OUVIDORIA 2023 FASE 3

ALUNOS:
MURILO DOS SANTOS ALVES
DEMOSTENES DINIZ PORTO
DARLAN SADRAQUE
VALDEMIR DOMINGOS DA SILVA JÚNIOR
FELIPE RODRIGUES HONÓRIO
DAYANE RODRIGUES HONÓRIO

#IMPORTANTE:Em TODO O PROJETO A TABELA USADA DENTRO DO BANCO DE DADOS É "manifestacoes"

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

LEMBRE-SE ANTES DE UTILIZAR O SISTEMA, DEVE CRIAR A TABELA 'manifestacoes' no MySQL dentro do Banco de Dados que for usar
e inserir o acesso e Banco de Dados em 'abrirBancoDados'. Faça isso para pleno funcionamento do código.
'''

from Listagem import *
from Registrar import *
from PesquisaCodigo import *
from Alteracao import *
from Excluir import *

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

    #LISTAGEM
    if opcao ==1:
        Listagem(conexao)

    #REGISTRAR MANIFESTAÇÃO
    elif opcao ==2:
        Registrar(conexao)

    #EXIBIR QUANTIDADE DE MANIFESTAÇÕES
    elif opcao ==3:
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

    #PESQUISAR MANIFESTAÇÃO POR CÓD.
    elif opcao ==4:
        PesquisarPorCod(conexao)

    #ALTERAR MANIFESTAÇÃO
    elif opcao ==5:
        Alterar(conexao)

    #EXCLUIR MANIFESTAÇÃO
    elif opcao ==6:
        opcaodeletar = 0
        while opcaodeletar != 2:
            print()
            print('MENU - EXCLUIR MANIFESTAÇÃO')
            print('1)EXCLUIR MANIFESTAÇÃO')
            print('2) VOLTAR PARA O MENU')
            opcaodeletar = int(input('->'))
            print()

            if opcaodeletar == 1:
                lista=VerificarListaVazia(conexao)
                if lista==0:
                    print('APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS')

                else:
                    confirmacaoDeletar = 0
                    while confirmacaoDeletar != 3:
                        print('QUAL O CÓDIGO DA MANIFESTAÇÃO QUE DESEJA DELETAR?')
                        cod = input('->')
                        manifestacao=pesquisarPorCodigo(conexao,cod)
                        if type(manifestacao)==str:
                            print(manifestacao)

                        else:
                            TipoNome=TipoCodparaNome(manifestacao[0][4])
                            SituacaoNome=SituacaoCodParaNome(manifestacao[0][5])
                            print('Por gentileza, confirme se essa é a manifestação que deseja deletar:')
                            print()
                            print(f'SITUAÇÃO:{SituacaoNome}')
                            print(f'TIPO: {TipoNome}')
                            print(f'AUTOR: {manifestacao[0][3]}')
                            print(f'TITULO: {manifestacao[0][1]}')
                            print(f'DESCRIÇÃO:{manifestacao[0][2]}')
                            print()


                            confirmacao = 0
                            while confirmacao != 3:
                                print('Realmente deseja deletar essa manifestação? ')
                                print('1) SIM QUERO DELETAR')
                                print('2) QUERO DELETAR OUTRA')
                                print('3) SAIR PARA O MENU')
                                confirmacao = int(input('->'))

                                if confirmacao == 1:
                                    DeletarManifestacao(conexao, cod)
                                    confirmacao = 3
                                    confirmacaoDeletar = 3
                                    print('A MANIFESTAÇÃO FOI DELETADA')

                                elif confirmacao == 2:
                                    print('INSIRA NOVAMENTE O CÓDIGO DA MANIFESTAÇÃO')
                                    confirmacao = 3
                                    print()

                                elif confirmacao == 3:
                                    confirmacaoDeletar = 3

                                elif confirmacaoDeletar != 3:
                                    print('A OPÇÃO É INVÁLIDA OU INEXISTENTE')

            elif opcaodeletar != 2:
                print('A OPÇÃO É INVÁLIDA OU INEXISTENTE')

    elif opcao !=7:
        print('A OPÇÃO INSÉRIDA É INVÁLIDA OU INEXISTENTE')
print('OBRIGADO POR UTILIZAR NOSSO SISTEMA')
encerrarBancoDados(conexao)