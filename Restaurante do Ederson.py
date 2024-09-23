import tkinter as tk
from tkinter import messagebox

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante do Ederson")
        self.root.geometry("600x800")

        # Inicialização das variáveis
        self.logins = ["admin"]
        self.senhas = ["123"]
        self.carrinho = []
        self.usuario = ""

        # Carregar imagens
        self.imagens = {
            "Entradas": tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/entradas.png").subsample(10, 10),
            "Pratos Principais": tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pratos_principais.png").subsample(10, 10),
            "Bebidas": tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas.png").subsample(10, 10),
            "Bebidas Alcoólicas": tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas_alcoólicas.png").subsample(10, 10),
            "Sobremesas": tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/sobremesas.png").subsample(10, 10),
            "Menu do Chef": tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/menu_do_chef.png").subsample(10, 10),
        }

        self.produtos = {
            "Entradas": ["Salada", "Sopa", "Pão de Alho", "Bruschetta", "Coxinha"],
            "Pratos Principais": ["Feijoada", "Estrogonofe", "Lasagna", "Pizza", "Hambúrguer"],
            "Bebidas": ["Refrigerante", "Água", "Suco", "Chá", "Limonada"],
            "Bebidas Alcoólicas": ["Cerveja", "Vinho", "Vodka", "Whisky", "Tequila"],
            "Sobremesas": ["Pudim", "Tiramisu", "Cheesecake", "Brownie", "Sorvete"],
            "Menu do Chef": ["Risoto", "Paella", "Sushi", "Ceviche", "Foie Gras"]
        }

        self.tela_login()

    def tela_login(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        self.caixa_usuario = tk.Entry(self.root)
        self.caixa_usuario.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.caixa_senha = tk.Entry(self.root, show='*')
        self.caixa_senha.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Confirmação de Senha:").grid(row=2, column=0, padx=10, pady=10)
        self.caixa_conf_senha = tk.Entry(self.root, show='*')
        self.caixa_conf_senha.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=3, column=1, pady=20, padx=20)
        tk.Button(self.root, text="Login", command=self.logar).grid(row=3, column=0, pady=20, padx=20)

    def tela_menu(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Olá, {self.usuario}", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        categorias = list(self.produtos.keys())
        for index, categoria in enumerate(categorias):
            row = index // 2 + 1
            column = index % 2
            tk.Button(
                self.root,
                text=categoria,
                image=self.imagens[categoria],
                compound='left',
                command=lambda c=categoria: self.tela_produtos(c)
            ).grid(row=row, column=column, pady=20, padx=20, sticky="nsew")

        tk.Button(self.root, text="Carrinho", command=self.tela_carrinho).grid(row=len(categorias) // 2 + 1, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")

        # Ajustar o peso das colunas e linhas para expandirem
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def tela_produtos(self, categoria):
        self.clear_screen()

        tk.Label(self.root, text=f"Escolha seus {categoria}", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        for index, produto in enumerate(self.produtos[categoria]):
            tk.Button(
                self.root,
                text=produto,
                command=lambda p=produto: self.adicionar_carrinho(p)
            ).grid(row=index + 1, column=0, pady=10, padx=20, sticky="nw")

        tk.Button(self.root, text="Voltar ao Menu", command=self.tela_menu).grid(row=len(self.produtos[categoria]) + 1, column=0, pady=20, padx=20, sticky="nw")

    def tela_carrinho(self):
        self.clear_screen()

        tk.Label(self.root, text="Carrinho de Compras", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        if not self.carrinho:
            tk.Label(self.root, text="Carrinho vazio").grid(row=1, column=0, pady=20, padx=20, columnspan=2)
        else:
            for index, item in enumerate(self.carrinho):
                tk.Label(self.root, text=item).grid(row=index + 1, column=0, pady=10, padx=20, sticky="nw")

            tk.Button(self.root, text="Finalizar Pedido", command=self.finalizar_pedido).grid(row=len(self.carrinho) + 1, column=0, pady=20, padx=20, sticky="nw")

        tk.Button(self.root, text="Voltar ao Menu", command=self.tela_menu).grid(row=len(self.carrinho) + 2, column=0, pady=20, padx=20, sticky="nw")

    def finalizar_pedido(self):
        self.clear_screen()
        if not self.carrinho:
            tk.Label(self.root, text="Carrinho vazio. Não é possível finalizar.").grid(row=0, column=0, padx=20, pady=20)
        else:
            tk.Label(self.root, text="Pedido Finalizado!", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20)
            tk.Label(self.root, text="Itens do Pedido:").grid(row=1, column=0, padx=20, pady=10)
            for index, item in enumerate(self.carrinho):
                tk.Label(self.root, text=item).grid(row=index + 2, column=0, padx=20, pady=5)

            tk.Button(self.root, text="Enviar Pedido", command=self.enviar_pedido).grid(row=len(self.carrinho) + 2, column=0, pady=20, padx=20, sticky="nw")

    def enviar_pedido(self):
        messagebox.showinfo("Pedido Enviado", "Seu pedido foi enviado à cozinha! Obrigado.")
        self.carrinho = []
        self.finalizar_sistema()

    def cadastrar(self):
        usuario = self.caixa_usuario.get()
        senha = self.caixa_senha.get()
        conf_senha = self.caixa_conf_senha.get()

        if usuario and senha and conf_senha:
            if senha != conf_senha:
                messagebox.showwarning("Senha", "Senhas não coincidem!")
            elif usuario in self.logins:
                messagebox.showwarning("Erro", "Usuário já cadastrado!")
            else:
                self.logins.append(usuario)
                self.senhas.append(senha)
                messagebox.showinfo("Cadastro", "Cadastro Realizado com Sucesso!")
                self.tela_login()
        else:
            messagebox.showwarning("Aviso", "Campos não preenchidos!")

    def logar(self):
        usuario = self.caixa_usuario.get()
        senha = self.caixa_senha.get()

        if usuario and senha:
            if usuario in self.logins:
                index = self.logins.index(usuario)
                if senha == self.senhas[index]:
                    self.usuario = usuario
                    messagebox.showinfo("Login", f"Olá {usuario}, você será direcionado ao menu agora!")
                    self.tela_menu()
                else:
                    messagebox.showwarning("Senha", "Senha Incorreta")
            else:
                messagebox.showwarning("Não Encontrado", "Usuário não cadastrado!")
        else:
            messagebox.showwarning("Aviso", "Campos não preenchidos!")

    def adicionar_carrinho(self, produto):
        self.carrinho.append(produto)
        messagebox.showinfo("Adicionado", f"{produto} adicionado ao carrinho!")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def finalizar_sistema(self):
        self.clear_screen()
        tk.Label(self.root, text="Obrigado por usar o sistema!", font=("Arial", 20)).pack(pady=20)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()
