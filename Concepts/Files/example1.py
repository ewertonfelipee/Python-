# txt = "\nConceitos de arquivos"
path = "path_ex"
file = open(path, "rb") # leitura binária

retorno = file.read()

path_output = "path_ex"
file_output = open(path_output, "wb") # escrita binária
file_output.write(retorno)


file_output.close()
file.close()