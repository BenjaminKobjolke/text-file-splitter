import os
from pathlib import Path

class FileHandler:
    def read_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: Input file not found at {filepath}")
            return None
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return None

    def write_file(self, filepath, content):
        try:
            Path(os.path.dirname(filepath)).mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filepath}: {e}")
