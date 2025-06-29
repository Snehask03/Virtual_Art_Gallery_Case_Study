import os

class PropertyUtil:
    @staticmethod
    def get_property(relative_path):
        base_dir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(base_dir, relative_path)
        props = {}
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    props[key.strip()] = value.strip()
        return props