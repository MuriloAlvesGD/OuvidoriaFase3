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