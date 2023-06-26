from Metodos import *

def Excluir (conexao):
    opcaodeletar = 0
    while opcaodeletar != 2:
        print()
        print('MENU - EXCLUIR MANIFESTAÇÃO')
        print('1)EXCLUIR MANIFESTAÇÃO')
        print('2) VOLTAR PARA O MENU')
        opcaodeletar = int(input('->'))
        print()

        if opcaodeletar == 1:
            lista = VerificarListaVazia(conexao)
            if lista == 0:
                print('APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS')

            else:
                confirmacaoDeletar = 0
                while confirmacaoDeletar != 3:
                    print('QUAL O CÓDIGO DA MANIFESTAÇÃO QUE DESEJA DELETAR?')
                    cod = input('->')
                    manifestacao = pesquisarPorCodigo(conexao, cod)
                    if type(manifestacao) == str:
                        print(manifestacao)

                    else:
                        TipoNome = TipoCodparaNome(manifestacao[0][4])
                        SituacaoNome = SituacaoCodParaNome(manifestacao[0][5])
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

