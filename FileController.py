class FileController:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, content, mode='w'):
        try:
            with open(self.file_path, mode) as file:
                file.write(content + '\n')
                print(f"Contenu écrit dans le fichier: {self.file_path}")
        except Exception as e:
            print(f"Error dans la lecture du fichier: {e}")

    def read_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                print(f"Contenu lu dans fichier : {self.file_path}")
                return content
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} n'a pas été trouvé.")
            return None
        except Exception as e:
            print(f"Error dans la lecture du fichier: {e}")
            return None

    def isEmpty(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                return len(content) == 0
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} n'a pas été trouvé.")
            return True
        except Exception as e:
            print(f"Erro au vérifier si le fichier est vide: {e}")
            return None