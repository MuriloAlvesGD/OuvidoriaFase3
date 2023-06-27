from Metodos import *

def Alterar (conexao):
    opcaomodificar = 0
    while opcaomodificar != 3:
        print()
        print('MENU - ALTERAR MANIFESTAÇÃO')
        print()
        print('O que deseja fazer?')
        print('1) ALTERAR MANIFESTAÇÃO ABERTA')
        print('2) MARCAR MANIFESTAÇÃO COMO ENCERRADA')
        print('3) SAIR/VOLTAR PARA O MENU')
        opcaomodificar = int(input('-> '))
        print()

        # ALTERAR MANIFESTAÇÃO ABERTA
        if opcaomodificar == 1:
            manifestacoes = VerificarManifestacaoAberta(conexao)
            if manifestacoes[0][0] == 0:
                print('NO MOMENTO NÃO HÁ MANIFESTAÇÃO ABERTA')

            else:  # ONDE OCORRE O PROCESSO DE ALTERAÇÃO
                opcaoAlterar = 0
                while opcaoAlterar != 4:  # MENU DE ALTERAÇÕES POSSIVEIS
                    print('O QUE DESEJA ALTERAR?')
                    print('1) TITULO')
                    print('2) DESCRIÇÃO')
                    print('3) TITULO + DESCRIÇÃO')
                    print('4) VOLTAR/SAIR')
                    opcaoAlterar = int(input('->'))
                    print()

                    # TIPO DE ALTERAÇÃO SELECIONADA
                    if opcaoAlterar in (1, 2, 3):
                        cod = input('Qual o código da ocorrência que deseja alterar?')
                        manifestacao = pesquisarPorCodAberta(conexao, cod)
                        if type(manifestacao) == str:
                            print(manifestacao)

                        else:
                            padroes = definirAlteracoes(conexao, opcaoAlterar, cod)
                            print('ABAIXO ESTÁ A MANIFESTAÇÃO REGISTRADA:')
                            print(padroes[1])
                            print()
                            print('ESSA É A MANIFESTAÇÃO ALTERADA')
                            print(padroes[0])

                            confirmacao = 0
                            while confirmacao != 2:
                                print()
                                print('DESEJA REALIZAR A ALTERAÇÃO?')
                                print('1) SIM')
                                print('2) NÃO')
                                confirmacao = int(input('->'))

                                if confirmacao == 1:
                                    AlterandoManifestacao(conexao, padroes, cod)
                                    print()
                                    print('MANIFESTAÇÃO ALTERADA COM SUCESSO')
                                    confirmacao = 2

                                elif confirmacao == 2:
                                    print()
                                    print('OK NÃO ALTERAMOS A MANIFESTAÇÃO')
                                    print()

                                elif confirmacao != 2:
                                    print()
                                    print('OPÇÃO INVÁLIDA OU INEXISTENTE')
                                    print()

                    elif opcaoAlterar != 4:
                        print()
                        print('OPÇÃO INVÁLIDA OU INEXISTENTE')
                        print()

        # MARCAR COMO ENCERRADA
        elif opcaomodificar == 2:
            manifestacao = VerificarManifestacaoAberta(conexao)
            if type(manifestacao) == str:
                print(manifestacao)
            else:
                Encerrar = 0
                while Encerrar != 3:
                    print('QUAL O CÓDIGO DA MANIFESTAÇÃO QUE DESEJA ENCERRAR?')
                    cod = input('->')
                    manifestacao = pesquisarPorCodAberta(conexao, cod)
                    if type(manifestacao) == str:
                        print(manifestacao)
                    else:
                        print()
                        print('Por gentileza, confirma a manifestação que deseja encerrar:')
                        TipoNome = TipoCodparaNome(manifestacao[0][4])
                        print()
                        print(f'TIPO: {TipoNome}')
                        print(f'AUTOR: {manifestacao[0][3]}')
                        print(f'TITULO: {manifestacao[0][1]}')
                        print(f'DESCRIÇÃO:{manifestacao[0][2]}')
                        print()
                        while confirmacaoEncerrar != 3:  # CONFIRMANDO SE QUER ENCERRAR
                            print('Realmente deseja marcar como encerrada essa manifestação? ')
                            print('1) SIM QUERO ENCERRAR')
                            print('2) QUERO MARCAR OUTRA COMO ENCERRADA')
                            print('3) SAIR/VOLTAR PARA O MENU')  # VOLTA PARA O MENU DE ALTERAÇÕES
                            confirmacaoEncerrar = int(input('->'))

                            if confirmacaoEncerrar == 1:
                                EncerrarManifestacao(conexao, cod)
                                Encerrar = 3  # SAINDO DOS WHILEs
                                print('A MANIFESTAÇÃO FOI MARCADA COMO CONCLUÍDA')

                            elif confirmacaoEncerrar == 2:
                                print('INSIRA NOVAMENTE O CÓDIGO DA MANIFESTAÇÃO')
                                confirmacaoEncerrar = 3

                            elif confirmacaoEncerrar == 3:
                                Encerrar = 3

                            elif confirmacaoEncerrar != 3:
                                print('A OPÇÃO É INVÁLIDA OU INEXISTENTE')

        elif opcaomodificar != 3:
            print('OPÇÃO INVÁLIDA OU INEXISTENTE')
