import pandas as pd


def linha():
    print('-' * 55)

#função para coletar dados de um jogador
def capturar_dados_jogador():
    dicionario = {}
    dicionario['nome'] = str(input('Nome do jogador: '))
    partidas = entrada_valida_int(f'Quantas partidas {dicionario["nome"]} jogou? ')
    dicionario['gols'] = [entrada_valida_int(f'Quantos gols na partida {g+1}? ') for g in range(partidas)]
    dicionario['total'] = sum(dicionario['gols'])
    return dicionario

#valida entradas numéricas 
def entrada_valida_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print('O valor não pode ser negativo.')
            else:
                return valor
        except ValueError:
            print('Erro! Digite um número inteiro.')

#função para listar jogadores cadastrados
def listar_jogadores(geral):
    print('JOGADORES CADASTRADOS:')
    for i, v in enumerate(geral):
        print(f"{i} - {v['nome']}")

#exibe a tabela de dados no terminal
def exibir_tabela(geral):
    print(f"{'Cod':<5}{'Nome':<15}{'Gols':<25}{'Total':<5}")
    linha()
    for i, v in enumerate(geral):
        print(f"{i:<5}{v['nome']:<15}{str(v['gols']):<25}{v['total']:<5}")
    linha()

#salva em uma planilha excel
def salvar_dados_excel(geral):
    salvar = str(input('Deseja salvar os dados em uma planilha do Excel [S/N]:')).upper()
    if salvar == 'S':
        nome_arquivo = str(input('Qual o nome do arquivo?')).strip()

        #verifica se o usuário add a extensão do arquivo
        if not nome_arquivo.endswith('.xlsx'):
            nome_arquivo += '.xlsx'

        df = pd.DataFrame(geral)  #converte a lista em um dataframe
        df.insert(0, 'cod', pd.Series(range(len(df))))
        
        df.to_excel(nome_arquivo, index=False)
        
        print(f'\033[32mDados salvos com sucesso no arquivo {nome_arquivo}\033[0m')
        
    else:
        print('\033[31mOs dados não serão salvos.\033[0m')
        print()

#consulta de dados de um jogador
def consultar_jogador(geral):
    while True:
        print()
        linha()
        jogador = entrada_valida_int('Mostrar dados de qual jogador? [999 para parar]: ')
        if jogador == 999:
            break
        if jogador >= len(geral):
            print('ERRO! Jogador não encontrado.')
        else:
            print(f'- LEVANTAMENTO DO JOGADOR: {geral[jogador]["nome"]}')
            for i, g in enumerate(geral[jogador]["gols"]):
                print(f'No jogo {i} fez {g} gols')
            print()
            linha()
            

#função principal
def main():
    geral = []
    
    linha()
    print('\033[34m          Olá, seja bem vindo ao JogoData!\033[0m')
    linha()

    while True:
        geral.append(capturar_dados_jogador())

        while True:
            resposta = str(input('Quer continuar? [S/N]:')).upper()[0]
            if resposta in 'SN':
                linha()
                break
            print('ERRO! Digite apenas S ou N.')
        
        if resposta == 'N':
            linha()
            break

    #exibe tabela de jogadores
    exibir_tabela(geral)
    
    #salva os dados em Excel
    salvar_dados_excel(geral)

    #consulta de jogadores
    consultar_jogador(geral)

    print('\033[34mVolte sempre!\033[0m')

#executa o programa
if __name__ == "__main__":
    main()
