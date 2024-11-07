import tkinter as tk
from tkinter import messagebox


class Lanchonete:
    def __init__(self):
        self.valor_pedido = 0
        self.pedidos = []
        self.cardapio = [
            ('Pizza Grande', 65.00),
            ('Pizza Média', 45.00),
            ('Pizza Pequena', 35.00),
            ('Refrigerante 2 LT', 15.00),
            ('Refrigerante Lata', 6.00),
            ('Refrigerante 600 ml', 9.00),
            ('Hot Dog Especial', 12.00),
            ('Hot Dog Simples', 8.00),
            ('Chocolate', 5.00)
        ]

    def adicionar_item(self, escolha):
        if 1 <= escolha <= len(self.cardapio):
            item, preco = self.cardapio[escolha - 1]
            self.pedidos.append((item, preco))
            self.valor_pedido += preco
            return True
        return False

    def finalizar_pedido(self, opcao_pagamento, parcelas=None):
        if opcao_pagamento == 1:
            desconto = self.valor_pedido * 0.9
            return f"Sua compra de R${self.valor_pedido:.2f} vai custar R${desconto:.2f} no final."
        elif opcao_pagamento == 2:
            desconto = self.valor_pedido * 0.95
            return f"Sua compra de R${self.valor_pedido:.2f} vai custar R${desconto:.2f} no final."
        elif opcao_pagamento == 3:
            parcela = self.valor_pedido / 2
            return f"Sua compra de R${self.valor_pedido:.2f} vai custar R${parcela:.2f} cada parcela."
        elif opcao_pagamento == 4 and parcelas:
            valor_final = self.valor_pedido * 1.2
            valor_parcela = valor_final / parcelas
            return f"Sua compra será parcelada em {parcelas}x de R${valor_parcela:.2f} COM JUROS. Sua compra de R${self.valor_pedido:.2f} vai custar R${valor_final:.2f}"
        else:
            return "Opção inválida. Por favor, digite uma opção válida"


def mostrar_cardapio():
    cardapio_texto = "\n".join(
        [f"[{idx + 1}] {item} - R${preco:.2f}" for idx, (item, preco) in enumerate(lanchonete.cardapio)])

    cardapio_window = tk.Toplevel(root)
    cardapio_window.title("Cardápio")
    cardapio_window.geometry("400x210+320+250")
    cardapio_window.resizable(False,False)

    lbl_cardapio = tk.Label(cardapio_window, text=cardapio_texto, justify=tk.LEFT, font=("Arial", 14))
    lbl_cardapio.pack()


def realizar_pedido():
    def adicionar_item():
        try:
            escolha = int(entry_escolha.get())
            if lanchonete.adicionar_item(escolha):
                lbl_total.config(text=f"Total: R${lanchonete.valor_pedido:.2f}")
                item, preco = lanchonete.cardapio[escolha - 1]
                listbox_pedidos.insert(tk.END, f"{item} - R${preco:.2f}")
                entry_escolha.delete(0, tk.END)  # Limpa o campo de entrada
            else:
                messagebox.showerror("Erro", "Escolha inválida.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido.")

    def finalizar_pedido_local():
        pedido_window.destroy()
        finalizar_pedido()  # Chama a aba de finalização de pedido

    pedido_window = tk.Toplevel(root)
    pedido_window.title("Realizar Pedido")
    pedido_window.geometry("300x400+750+250")

    lbl_escolha = tk.Label(pedido_window, text="Digite sua escolha:", font=("Arial", 12))
    lbl_escolha.pack()

    entry_escolha = tk.Entry(pedido_window)
    entry_escolha.pack()

    btn_adicionar = tk.Button(pedido_window, text="Adicionar", command=adicionar_item, font=("Arial", 12))
    btn_adicionar.pack()

    btn_finalizar = tk.Button(pedido_window, text="Finalizar Pedido", command=finalizar_pedido_local, font=("Arial", 12))
    btn_finalizar.pack()

    lbl_total = tk.Label(pedido_window, text=f"Total: R${lanchonete.valor_pedido:.2f}", font=("Arial", 12))
    lbl_total.pack()

    listbox_pedidos = tk.Listbox(pedido_window, height=15, width=25)
    listbox_pedidos.pack()


def finalizar_pedido():
    if lanchonete.valor_pedido == 0:
        messagebox.showinfo("Informação", "Por favor, realize o seu pedido antes de finalizar a compra!")
        return

    def calcular_pagamento():
        try:
            opcao = int(var_opcao.get())
            parcelas = None
            if opcao == 4:
                parcelas = int(entry_parcelas.get())

            resultado = lanchonete.finalizar_pedido(opcao, parcelas)
            messagebox.showinfo("Pagamento", resultado)
            lanchonete.__init__()  # Resetar a lanchonete após finalizar o pedido
            pagamento_window.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite uma opção válida e número de parcelas se aplicável.")

    pagamento_window = tk.Toplevel(root)
    pagamento_window.title("Formas de Pagamento")
    pagamento_window.geometry("380x200+750+250")

    lbl_pagamento = tk.Label(pagamento_window, text="Escolha a forma de pagamento:", font=("Arial", 12))
    lbl_pagamento.pack()

    var_opcao = tk.IntVar()
    tk.Radiobutton(pagamento_window, text="À Vista Dinheiro/Cheque/PIX (10% de desconto)", variable=var_opcao,
                   value=1, font=("Arial", 12)).pack(anchor=tk.W)
    tk.Radiobutton(pagamento_window, text="À Vista Cartão (5% de desconto)", variable=var_opcao, value=2, font=("Arial", 12)).pack(
        anchor=tk.W)
    tk.Radiobutton(pagamento_window, text="2x no Cartão (sem juros)", variable=var_opcao, value=3, font=("Arial", 12)).pack(anchor=tk.W)
    tk.Radiobutton(pagamento_window, text="3x ou mais no Cartão (20% de juros)", variable=var_opcao, value=4, font=("Arial", 12)).pack(
        anchor=tk.W)

    entry_parcelas = tk.Entry(pagamento_window)
    entry_parcelas.pack()

    btn_calcular = tk.Button(pagamento_window, text="Calcular", command=calcular_pagamento, font=("Arial", 12))
    btn_calcular.pack()


if __name__ == "__main__":
    lanchonete = Lanchonete()
    root = tk.Tk()
    root.title("Lanchonete Expresso")
    root.geometry("500x150+450+50")

    lbl_bem_vindo = tk.Label(root, text="== BEM VINDO À LANCHONETE EXPRESSO ==", font=("Arial", 16))
    lbl_bem_vindo.pack()

    btn_cardapio = tk.Button(root, text="Cardápio", command=mostrar_cardapio, font=("Arial", 14))
    btn_cardapio.pack()

    btn_pedido = tk.Button(root, text="Realizar Pedido", command=realizar_pedido, font=("Arial", 14))
    btn_pedido.pack()

    btn_sair = tk.Button(root, text="Sair", command=root.quit, font=("Arial", 14))
    btn_sair.pack()

    root.mainloop()
