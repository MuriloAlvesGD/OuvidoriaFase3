from Metodos import *

def PesquisarPorCod (conexao):
    opcaopesquisar = 0
    while opcaopesquisar != 2:
        print()
        print('MENU - PESQUISAR POR CÓDIGO')
        print()
        print('1)PESQUISAR MANIFESTAÇÃO')
        print('2) SAIR/VOLTAR PARA O MENU')
        opcaopesquisar = int(input('->'))

        if opcaopesquisar == 1:
            verificacao = VerificarListaVazia(conexao)
            if type(verificacao) == str:
                print(verificacao)

            else:
                print()
                print('Informe o código da manifestação')
                cod = input('->')
                listar = pesquisarPorCodigo(conexao, cod)
                if type(listar) == str:
                    print(listar)

                #PRINT DA MANIFESTAÇÃO
                else:
                    TipoNome = TipoCodparaNome(listar[0][4])
                    SituacaoNome = SituacaoCodParaNome(listar[0][5])
                    print()
                    print(f'O cód.{cod}, está associado a seguinte manifestação:')
                    print()
                    print(f'SITUAÇÃO:{SituacaoNome}')
                    print(f'TIPO: {TipoNome}')
                    print(f'AUTOR: {listar[0][3]}')
                    print(f'TITULO: {listar[0][1]}')
                    print(f'DESCRIÇÃO:{listar[0][2]}')

        elif opcaopesquisar != 2:
            print('OPÇÃO ESCOLHIDA É INVÁLIDA OU INEXISTENTE')