import os
def scanea_directorio(str_path):
    # crea un array con los archivos del directorio escaneado
    files = []
    with os.scandir(str_path) as ficheros:
        # se registraran solo los archivos no las carpetas
        for fichero in ficheros:
            if os.path.isfile(fichero):
                files.append(str_path+'/'+fichero.name)
    out = files
    return out