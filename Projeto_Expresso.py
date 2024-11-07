from time import sleep

valor_pedido = 0

print("== BEM VINDO À LANCHONETE EXPRESSO ==")
while True:
    print("Opções:")
    print("[1] Cardápio | [2] Realizar pedido | [3] Sair do Sistema | [0] Finalizar pedido") #Menu de opções
    menu = int(input("Digite a sua opção: "))

    if menu == 1: #Para mostrar o cardápio
        print("Cardápio:")
        print("[1] Pizza Grande - R$65,00\n[2] Pizza Média - R$45,00\n[3] Pizza Pequena - R$35,00\n[4] Refrigerante 2 LT - R$15,00")
        print("[5] Refrigerante Lata - R$6,00\n[6] Refrigerante 600 ml - R$9,00\n[7] Hot Dog Especial - R$12,00\n[8] Hot Dog Simples - R$8,00\n[9] Chocolate - R$5,00\n")

    elif menu == 2: #Para realizar o pedido

        while True:
            escolha = int(input("Digite sua escolha: "))

            if escolha == 1:
                valor_pedido += 65.00

            elif escolha == 2:
                valor_pedido += 45.00

            elif escolha == 3:
                valor_pedido += 35.00

            elif escolha == 4:
                valor_pedido += 15.00

            elif escolha == 5:
                valor_pedido += 6.00

            elif escolha == 6:
                valor_pedido += 9.00

            elif escolha == 7:
                valor_pedido += 12.00

            elif escolha == 8:
                valor_pedido += 8.00

            elif escolha == 9:
                valor_pedido += 5.00
            elif escolha == 0:
                sleep(0.5)
                print(25 * '-')
                print(' PROCESSANDO SUA COMPRA')
                print(25 * '-')
                sleep(1.5)
                print(f"Sua compra foi finalizada e deu um total de R$ {valor_pedido}\n")
                print("===========FORMAS DE PAGAMENTO===========")

                print(
                    "[1] À VISTA DINHEIRO/CHEQUE/PIX (10% de desconto)\n[2] À VISTA CARTÃO (5% de desconto)\n[3] 2x NO CARTÃO (sem juros)\n[4] 3x OU MAIS NO CARTÃO (20% de juros)\n")
                opção = int(input("Qual é a opção: "))

                if opção == 1:
                    desconto = valor_pedido - (valor_pedido * 0.1)
                    print(f"\nSua compra de R${valor_pedido:.2f} vai custar R${desconto:.2f} no final.\n")
                    sleep(1.2)

                elif opção == 2:
                    print(f"Sua compra de R${valor_pedido:.2f} vai custar R${valor_pedido - (0.05 * valor_pedido):.2f} no final.")
                    sleep(1.2)

                elif opção == 3:
                    print(f"Sua compra de R${valor_pedido:.2f} vai custar R$ {valor_pedido / 2:.2f} cada parcela.")
                    sleep(1.2)

                elif opção == 4:
                    parcelas = int(input("Quantas parcelas: "))
                    valor_final = valor_pedido + (valor_pedido * 0.2)
                    ndp = valor_final / parcelas
                    print(f"\nSua compra será parcelada em {parcelas}x de R${ndp:.2f} COM JUROS.")
                    print(f"\nSua compra de {valor_pedido:.2f} vai custar R${valor_final:.2f}")
                    sleep(1.2)

                print('A LANCHE EXPRESSO AGRADECE SUA PREFERÊNCIA. VOLTE SEMPRE!')
                break
        break

    elif menu == 3: #Opção de sair do sistema
        print("Saindo do sistema...")
        break

    elif menu == 0:
        print("Por favor, realize o seu pedido antes de finalizar a compra!")

    else: #Se qualquer outro número além das opções 1,2,3 e 0 forem digitas no console
        print("Opção inválida. Por favor, digite uma opção válida")