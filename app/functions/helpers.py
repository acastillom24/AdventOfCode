

def read_file_txt(path_file: str) -> list:
    """Función para leer un archivo de texto y devolver una lista de líneas.
    
    Args:
        path_file (str): Ruta del archivo de texto a leer.
    
    Returns:
        list: Lista de líneas del archivo de texto.
    """
    
    with open(path_file) as f:
        lines = f.readlines()
    f.close()
    return lines
