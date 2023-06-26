from Metodos import *
def Registrar (conexao):
        inserirmanifestacao = 0
        while inserirmanifestacao != 2:
                print()
                print('MENU - REGISTRAR NOVA MANIFESTAÇÃO')
                print()
                print('Deseja registrar uma nova MANIFESTAÇÃO?')
                print('1) SIM QUERO REGISTRAR')
                print('2) NÃO, VOLTAR PARA O MENU')
                inserirmanifestacao = int(input('->'))  # CONFIRMAR SE QUER REGISTRAR UMA MANIFESTAÇÃO

                # INSERINDO MANIFESTAÇÃO
                if inserirmanifestacao == 1:
                        print()
                        print('Siga o processo a seguir:')

                        # O WHILE SERVE PARA CASO O USUARIO QUEIRA DESCARTAR A MANIFESTAÇÃO E INSERIR COM OUTROS DADOS
                        validacaomanifestacao = 0
                        while validacaomanifestacao != 1:

                                # VERIFICANDO SE O TIPO É VÁLIDO
                                validacaotipo = False
                                while validacaotipo == False:
                                        print()
                                        print('De qual tipo é a sua manifestação? ')
                                        print('1) RECLAMAÇÃO')
                                        print('2) ELÓGIOS')
                                        print('3) SUGESTÕES')
                                        tipo = int(input('->'))

                                        if tipo in (1, 2, 3):
                                                validacaotipo = True
                                                print('TIPO INSERIDO É VÁLIDO')
                                        else:
                                                print('TIPO INSERIDO É INVÁLIDO')

                                # RECOLHENDO DADOS DA MANIFESTAÇÃO
                                print()
                                print('Qual o seu nome?')
                                autor = input('->')
                                print()
                                print('Qual o título da manifestação?')
                                titulo = input('->')
                                print()
                                print('Insira a descrição da sua manifestação:')
                                descricao = input('->')
                                print()

                                # EXIBINDO A MANIFESTAÇÃO
                                TipoNome = TipoCodparaNome(tipo)
                                print('Por gentileza, confirme as informações inseridas:')
                                print(f'Tipo da Manifestação: {TipoNome}')
                                print(f'Autor da Manifestação: {autor}')
                                print(f'Titulo da Manifestação: {titulo}')
                                print(f'Descrição da Manifestação: {descricao}')
                                print()

                                # CONFIRMANDO SE DESEJA INSERIR A MANIFESTAÇÃO
                                confirmacao = False
                                while confirmacao == False:
                                        print('Deseja inserir a manifestação com os dados apresentados?')
                                        print('1) SIM, EU QUERO INSERIR')
                                        print('2) NÃO, EU QUERO INSERIR UMA OUTRA MANIFESTAÇÃO')
                                        print('3) VOLTAR')
                                        validacaomanifestacao = int(input('->'))

                                        # CONFIRMADO A INSERÇÃO, INSERE NA TABELA
                                        if validacaomanifestacao == 1:
                                                values = (titulo, descricao, autor, tipo, 0)
                                                InserirManifestacao(conexao, values)
                                                print()
                                                print('MANIFESTAÇÃO INSERIDA COM  SUCESSO!!')

                                        # SAI DO WHILE DE CONFIRMAÇÃO E REINICIA O PROCESSO DE INSERÇÃO
                                        elif validacaomanifestacao == 2:
                                                print('Por favor, insira as informações que deseja:')
                                                confirmacao = True

                                        # VOLTANDO PARA O MENU
                                        elif validacaomanifestacao == 3:
                                                confirmacao = True
                                                validacaomanifestacao = 1  # SAI DO WHILE DO PROCESSO DE INSERÇÃO DA MANIFESTAÇÃO

                                        elif validacaomanifestacao != 3:
                                                print('OPÇÃO INVÁLIDA OU INEXISTENTE')
                elif inserirmanifestacao != 2:
                        print()
                        print('OPÇÃO INVÁLIDA OU INEXISTENTE')
