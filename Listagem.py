from Metodos import *
def Listagem (conexao):
    opcaolistar = 0
    while opcaolistar != 4:
        print()
        print('MENU - LISTAR MANIFESTAÇÕES')
        print()
        print('1) LISTAR MANIFESTAÇÕES ABERTAS')
        print('2) LISTAR MANIFESTAÇÕES ENCERRADAS')
        print('3) LISTAR MANIFESTAÇÕES POR TIPO')
        print('4) VOLTAR PARA O MENU')
        opcaolistar = int(input('->'))
        print()

        # LISTAGEM POR SITUAÇÃO ABERTA/ENCERRADA
        if opcaolistar == 1 or opcaolistar == 2:
            listagem = ListarporSituacao(conexao, opcaolistar)
            if type(listagem) == str:
                print(listagem)
            else:  # listagem=(listar,statusNome)
                print(f'Essas são as MANIFESTAÇÕES {listagem[1]} presentes no banco de dados:')
                for i in listagem[0]:
                    TipoNome = TipoCodparaNome(i[4])
                    print(f'CÓD.{i[0]} | TITULO={i[1]} | AUTOR={i[3]} |TIPO={TipoNome}')


        # LISTAGEM POR TIPO
        elif opcaolistar == 3:
            verificacao = VerificarListaVazia(conexao)
            if verificacao[0][0] == 0:
                print('APARENTEMENTE NÃO HÁ MANIFESTAÇÕES CADASTRADAS')
            else:
                tipoPesquisar = 0
                while tipoPesquisar != 4:
                    print()
                    print('TIPOS DE MANIFESTAÇÕES')
                    print('1) RECLAMAÇÃO')
                    print('2) ELÓGIOS')
                    print('3) SUGESTÕES')
                    print('4) VOLTAR')
                    tipoPesquisar = int(input('Quais manifestações deseja ver? '))
                    print()

                    if tipoPesquisar in (1, 2, 3):
                        listagem = ListarPorTipo(conexao, tipoPesquisar)
                        if type(listagem) == str:
                            print(listagem)
                        else:  # listagem=(listar)
                            TipoNome = TipoCodparaNome(tipoPesquisar)
                            print(f'Essas são as manifestações existentes com o tipo {TipoNome}:')
                            for i in listagem:
                                SituacaoNome = SituacaoCodParaNome(i[5])
                                print(f'CÓD.{i[0]} | TITULO: {i[1]} | AUTOR: {i[3]} | SITUAÇÃO:{SituacaoNome}')

                    elif tipoPesquisar != 4:
                        print('OPÇÃO INVÁLIDA OU INEXISTENTE')

        elif opcaolistar != 4:
            print('OPÇÃO INVÁLIDA OU INEXISTENTE')