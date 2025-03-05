import os

def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

check_access(r"C:\Users\Miras\Desktop\Kak vzlomat pentagon.docx")