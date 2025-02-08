import json
import os

class JsonLocalData:
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(script_dir, "data.json")

    def get_data_rob(self, rob):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data.get(rob)
        except FileNotFoundError:
            print(f"Archivo '{self.file_path}' no encontrado.")
            return None
        except json.JSONDecodeError:
            print(f"El archivo '{self.file_path}' no contiene un JSON válido.")
            return None

    def set_data_rob(self, rob, value):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        data[rob] = value
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
