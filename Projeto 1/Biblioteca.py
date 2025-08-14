class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
class Livro:
    def __int__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
class Biblioteca:
    def __init__ (self):
        self.usuarios = []
        self.livros = []

    def cadastrar_usuario(self, nome, email):
        self.usuario.append(Usuario,(nome, email)) 
        print(f"Usuario '{nome}' cadastrado!")

    def cadastrar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))
        print(f"Livro '{titulo}' cadastrado!")

    def emprestra_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"Livro '{titulo}' foi emprestado com sucesso!")
                return
        print(f"Livro '{titulo}' não esta disponivel!")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"Livro '{titulo}' foi devolvido com sucesso!") 
                return
        print(f"Livro '{titulo}' Disponivel!")


biblioteca = Biblioteca()

biblioteca.cadastrar_usuario("Dark", "Dark.meliodas@gmail.com")