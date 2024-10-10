class FileController:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, content, mode='w'):
        try:
            with open(self.file_path, mode) as file:
                file.write(content + '\n')
                print(f"Conteúdo escrito no arquivo: {self.file_path}")
        except Exception as e:
            print(f"Erro ao escrever no arquivo: {e}")

    def read_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                print(f"Conteúdo lido do arquivo: {self.file_path}")
                return content
        except FileNotFoundError:
            print(f"O arquivo {self.file_path} não foi encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return None

    def isEmpty(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                return len(content) == 0
        except FileNotFoundError:
            print(f"O arquivo {self.file_path} não foi encontrado.")
            return True
        except Exception as e:
            print(f"Erro ao verificar se o arquivo está vazio: {e}")
            return None