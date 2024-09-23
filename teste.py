# import tkinter as tk

# root = tk.Tk()

# # Exemplo com row, column e sticky
# tk.Label(root, text="Label 1").grid(row=0, column=0, sticky="w", padx=10, pady=10)
# tk.Entry(root).grid(row=0, column=1, sticky="ew", padx=10, pady=10)

# # Exemplo com rowspan e columnspan
# tk.Label(root, text="Label 2").grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
# tk.Button(root, text="Button").grid(row=2, column=1, rowspan=2, padx=10, pady=10)

# # Exemplo com sticky e preenchimento
# tk.Label(root, text="Label 3").grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
# tk.Entry(root).grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

# root.grid_rowconfigure(3, weight=1)  # Configuração para expansão
# root.grid_columnconfigure(1, weight=1)  # Configuração para expansão

# root.mainloop()

# import tkinter as tk

# def menu(usuario):
#     tela_menu = tk.Tk()
#     tela_menu.title("Menu")
#     tela_menu.geometry("800x800")

#     menu_label = tk.Label(tela_menu, text=f"Olá {usuario}, SEJA BEM VINDO", font=("Arial", 20))
#     menu_label.grid(row=0, column=0, sticky="nw", padx=20, pady=20)
#     tk_image = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Galeria/gato.png")  
#     botao_com_imagem = tk.Button(tela_menu, image=tk_image, command=lambda: print("Botão clicado"))
#     botao_com_imagem.image = tk_image  
#     botao_com_imagem.grid(row=1, column=0, padx=20, pady=20, sticky="nw")




#     tela_menu.mainloop()

# menu("Usuário")

# import tkinter as tk

# def menu(usuario):
#     tela_menu = tk.Tk()
#     tela_menu.title("Menu")
#     tela_menu.geometry("800x800")

#     # Carregar a imagem PNG ou GIF
#     tk_image = tk.PhotoImage(file="caminho/para/sua/imagem.png")  # Substitua pelo caminho da sua imagem

#     # Criar o botão com a imagem
#     botao_com_imagem = tk.Button(tela_menu, image=tk_image, command=lambda: print("Botão clicado"))
#     botao_com_imagem.image = tk_image  # Manter uma referência da imagem para evitar que seja coletada como lixo
#     botao_com_imagem.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

#     # Adicionar um rótulo de boas-vindas
#     menu_label = tk.Label(tela_menu, text=f"Olá {usuario}, SEJA BEM VINDO", font=("Arial", 20))
#     menu_label.grid(row=1, column=0, padx=20, pady=20, sticky="nw")

#     tela_menu.mainloop()

# menu("Usuário")

# import tkinter as tk
# from tkinter import messagebox

# tela_menu = tk.Tk()
# tela_menu.title("Menu")
# tela_menu.geometry("800x800")

# menu_label = tk.Label(tela_menu, text=f"Olá , SEJA BEM VINDO", font=("Arial", 20))
# menu_label.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

# # Carregar imagens
# try:
#     tk_principal = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pratos_principais.png")
#     tk_bebidas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas.png")
#     tk_alcoolicas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas_alcoólicas.png")
#     tk_sobremesas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/sobremesas.png")
#     tk_menu_chef = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/menu_do_chef.png")
#     tk_entradas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/entradas.png")
# except tk.TclError as e:
#     messagebox.showerror("Erro", f"Erro ao carregar uma ou mais imagens: {e}")
#     tela_menu.quit()
   

# # Criar botões com imagens e texto
# botao_entradas = tk.Button(
#     tela_menu,
#     text="Entradas",
#     image=tk_entradas,
#     compound='left',  # Imagem à esquerda do texto
#     command=lambda: print("Entradas")
# )
# botao_entradas.grid(row=1, column=0, pady=20, padx=50, sticky="nw")

# botao_principal = tk.Button(
#     tela_menu,
#     text="Prato Principal",
#     image=tk_principal,
#     compound='left',  # Imagem à esquerda do texto
#     command=lambda: print("Prato Principal")
# )
# botao_principal.grid(row=2, column=0, pady=20, padx=50, sticky="nw")

# botao_bebidas = tk.Button(
#     tela_menu,
#     text="Bebidas",
#     image=tk_bebidas,
#     compound='left',  # Imagem à esquerda do texto
#     command=lambda: print("Bebidas")
# )
# botao_bebidas.grid(row=3, column=0, pady=20, padx=50, sticky="nw")

# botao_alcoolicas = tk.Button(
#     tela_menu,
#     text="Bebidas Alcoólicas",
#     image=tk_alcoolicas,
#     compound='left',  # Imagem à esquerda do texto
#     command=lambda: print("Bebidas Alcoólicas")
# )
# botao_alcoolicas.grid(row=4, column=0, pady=20, padx=50, sticky="nw")

# botao_sobremesas = tk.Button(
#     tela_menu,
#     text="Sobremesas",
#     image=tk_sobremesas,
#     compound='left',  # Imagem à esquerda do texto
#     command=lambda: print("Sobremesas")
# )
# botao_sobremesas.grid(row=5, column=0, pady=20, padx=50, sticky="nw")

# botao_menu_chef = tk.Button(
#     tela_menu,
#     text="Menu do Chef",
#     image=tk_menu_chef,
#     compound='left',  # Imagem à esquerda do texto
#     command=lambda: print("Menu do Chef")
# )
# botao_menu_chef.grid(row=6, column=0, pady=20, padx=50, sticky="nw")

# tela_menu.mainloop()
# import tkinter as tk
# from tkinter import messagebox

# def menu(usuario):
#     tela_menu = tk.Tk()
#     tela_menu.title("Menu")
#     tela_menu.geometry("600x800")

#     menu_label = tk.Label(tela_menu, text=f"Olá {usuario}, SEJA BEM VINDO", font=("Arial", 20))
#     menu_label.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

#     # Carregar e redimensionar as imagens
#     try:
#         tk_principal = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pratos_principais.png").subsample(10, 10)
#         tk_bebidas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas.png").subsample(10, 10)
#         tk_alcoolicas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas_alcoólicas.png").subsample(10, 10)
#         tk_sobremesas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/sobremesas.png").subsample(10, 10)
#         tk_menu_chef = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/menu_do_chef.png").subsample(10, 10)
#         tk_entradas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/entradas.png").subsample(10, 10)
#     except tk.TclError as e:
#         messagebox.showerror("Erro", f"Erro ao carregar uma ou mais imagens: {e}")
#         tela_menu.quit()
#         return

#     # Manter referências às imagens
#     tela_menu.tk_principal = tk_principal
#     tela_menu.tk_bebidas = tk_bebidas
#     tela_menu.tk_alcoolicas = tk_alcoolicas
#     tela_menu.tk_sobremesas = tk_sobremesas
#     tela_menu.tk_menu_chef = tk_menu_chef
#     tela_menu.tk_entradas = tk_entradas

#     # Criar botões com imagens
#     botao_entradas = tk.Button(
#         tela_menu,
#         text="Ver Entradas",
#         image=tk_entradas,
#         compound='left', 
#         command=lambda: print("Entradas")
#     )
#     botao_entradas.grid(row=1, column=0, pady=20, padx=50, sticky="nw")

#     botao_principal = tk.Button(
#         tela_menu,
#         text="Ver Pratos Principais",
#         image=tk_principal,
#         compound='left',  
#         command=lambda: print("Pratos Principais")
#     )
#     botao_principal.grid(row=2, column=0, pady=20, padx=50, sticky="nw")

#     botao_bebidas = tk.Button(
#         tela_menu,
#         text="Ver Bebidas",
#         image=tk_bebidas,
#         compound='left',  
#         command=lambda: print("Bebidas")
#     )
#     botao_bebidas.grid(row=3, column=0, pady=20, padx=50, sticky="nw")

#     botao_alcoolicas = tk.Button(
#         tela_menu,
#         text="Ver Bebidas Alcoólicas",
#         image=tk_alcoolicas,
#         compound='left',  
#         command=lambda: print("Bebidas Alcoólicas")
#     )
#     botao_alcoolicas.grid(row=4, column=0, pady=20, padx=50, sticky="nw")

#     botao_sobremesas = tk.Button(
#         tela_menu,
#         text="Ver Sobremesas",
#         image=tk_sobremesas,
#         compound='left',  
#         command=lambda: print("Sobremesas")
#     )
#     botao_sobremesas.grid(row=5, column=0, pady=20, padx=50, sticky="nw")

#     botao_menu_chef = tk.Button(
#         tela_menu,
#         text="Ver Menu do Chef",
#         image=tk_menu_chef,
#         compound='left',  
#         command=lambda: print("Menu do Chef")
#     )
#     botao_menu_chef.grid(row=6, column=0, pady=20, padx=50, sticky="nw")

#     tela_menu.mainloop()

# menu("Ezequiel")

# def form():
#     usuario = caixa_usuario.get()
#     senha = caixa_senha.get()
#     conf_senha = caixa_conf_senha.get()

#     if usuario and senha and conf_senha:
#         if senha != conf_senha:
#             messagebox.showwarning("Senha", "Senhas não coincidem!")
#         elif usuario == senha:
#             messagebox.showwarning("Erro", "Usuário e senha não podem coincidir!")
#         else:
#             messagebox.showinfo("Cadastro", "Cadastro Realizado com Sucesso!")
#             pedido = messagebox.askyesno("Pedido", "Deseja fazer seu pedido?")
#             if pedido:
#                 tela.quit()
#                 menu(usuario)
#             else:
#                 tela.quit()
#     else:
#         messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos de cadastro e tente novamente!")

# def logar():
#     usuario = caixa_usuario.get()
#     senha = caixa_senha.get()

#     if usuario and senha:
#         if usuario in logins:
#             index = logins.index(usuario)
#             if senha == senhas[index]:
#                 messagebox.showinfo("Cadastro encontrado", f"Olá {usuario}, Seja Bem Vindo, \nvocê será direcionado ao menu agora!")
#                 tela.quit()
#                 menu(usuario)
#             else:
#                 messagebox.showwarning("Senha", "Senha Incorreta")
#         else:
#             messagebox.showwarning("Não encontrado", "Usuário não cadastrado!")
#     else:
#         messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos de cadastro e tente novamente!")

# # Definir logins e senhas
# logins = ["admin"]
# senhas = ["123"]

# # Escolher entre Login ou Cadastro
# escolha = messagebox.askyesno(title="Logar ou Cadastrar", message="Você já tem cadastro em nosso sistema?")

# if escolha:
#     tela = tk.Tk()
#     tela.title("Login")

#     tk.Label(tela, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
#     caixa_usuario = tk.Entry(tela)
#     caixa_usuario.grid(row=0, column=1, padx=10, pady=10)

#     tk.Label(tela, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
#     caixa_senha = tk.Entry(tela, show='*')
#     caixa_senha.grid(row=1, column=1, padx=10, pady=10)

#     tk.Button(tela, text="Login", command=logar).grid(row=2, column=1, pady=20, padx=50)

#     tela.mainloop()
# else:
#     tela = tk.Tk()
#     tela.title("Cadastro de Cliente")

#     tk.Label(tela, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
#     caixa_usuario = tk.Entry(tela)
#     caixa_usuario.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

#     tk.Label(tela, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
#     caixa_senha = tk.Entry(tela, show='*')
#     caixa_senha.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

#     tk.Label(tela, text="Confirmação de Senha:").grid(row=2, column=0, padx=10, pady=10)
#     caixa_conf_senha = tk.Entry(tela, show='*')
#     caixa_conf_senha.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

#     tk.Button(tela, text="Cadastrar", command=form).grid(row=3, column=1, pady=20, padx=20)

#     tela.mainloop()

import tkinter as tk
from tkinter import messagebox

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante do Ederson")
        self.root.geometry("600x800")

        self.logins = ["admin"]
        self.senhas = ["123"]

        self.carrinho = []
        tk_principal = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pratos_principais.png").subsample(10,10)
        tk_bebidas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas.png").subsample(10, 10)
        tk_alcoolicas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas_alcoólicas.png").subsample(10, 10)
        tk_sobremesas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/sobremesas.png").subsample(10, 10)
        tk_menu_chef = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/menu_do_chef.png").subsample(10, 10)
        tk_entradas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/entradas.png").subsample(10, 10)
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

    def tela_menu(self, usuario):
        self.clear_screen()

        tk.Label(self.root, text=f"Olá, {usuario}", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20)

        categorias = list(self.produtos.keys())
        for index, categoria in enumerate(categorias):
            tk.Button(
                self.root,
                text=categoria,
                command=lambda c=categoria: self.tela_produtos(c)
            ).grid(row=index + 1, column=0, pady=20, padx=50, sticky="nw")

        tk.Button(self.root, text="Carrinho", command=self.tela_carrinho).grid(row=len(categorias) + 1, column=0, pady=20, padx=50, sticky="nw")

    def tela_produtos(self, categoria):
        self.clear_screen()

        tk.Label(self.root, text=f"Escolha seus {categoria}", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20)

        for index, produto in enumerate(self.produtos[categoria]):
            tk.Button(
                self.root,
                text=produto,
                command=lambda p=produto: self.adicionar_carrinho(p)
            ).grid(row=index + 1, column=0, pady=10, padx=20, sticky="nw")

        tk.Button(self.root, text="Voltar ao Menu", command=lambda: self.tela_menu(usuario)).grid(row=len(self.produtos[categoria]) + 1, column=0, pady=20, padx=20, sticky="nw")

    def tela_carrinho(self):
        self.clear_screen()

        tk.Label(self.root, text="Carrinho de Compras", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20)

        if not self.carrinho:
            tk.Label(self.root, text="Carrinho vazio").grid(row=1, column=0, pady=20, padx=20)
        else:
            for index, item in enumerate(self.carrinho):
                tk.Label(self.root, text=item).grid(row=index + 1, column=0, pady=10, padx=20, sticky="nw")

            tk.Button(self.root, text="Finalizar Pedido", command=self.finalizar_pedido).grid(row=len(self.carrinho) + 1, column=0, pady=20, padx=20, sticky="nw")

        tk.Button(self.root, text="Voltar ao Menu", command=lambda: self.tela_menu(usuario)).grid(row=len(self.carrinho) + 2, column=0, pady=20, padx=20, sticky="nw")

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
                    messagebox.showinfo("Login", f"Olá {usuario}, você será direcionado ao menu agora!")
                    self.tela_menu(usuario)
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
        tk.Label(self.root, text="Obrigado por usar nosso sistema!", font=("Arial", 20)).pack(pady=20)
        self.root.after(3000, self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()


