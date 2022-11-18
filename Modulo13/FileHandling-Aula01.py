#             MODOS DE ABERTURA DE ARQUIVOS
# =================================================================
#                           |	TEXTO	   |	BINÁRIO
# =================================================================
# Leitura	                |	"r"	       |	"rb"
# Leitura/Escrita       	|	"r+"	   |	"rb+"
# -----------------------------------------------------------------
# Escrita	                |	"w"	       |	"wb"
# Escrita/Leitura	        |	"w+"	   |	"wb+”
# -----------------------------------------------------------------
# Anexar	                |	"a"	       |	"ab"
# Anexar/Leitura	        |	"a+"	   |	"ab+"

# Escrita
# texto = 'Jornda Python - Manipulação de Arquivos'
#
# arquivo = open('D:\\Jornada Python - Python Academy - 2022\\JornadaPython-PythonAcademy\\Modulo13\\dados.txt', 'w')
#
# arquivo.write(texto)

# Leitura

# arquivo = open('D:\\Jornada Python - Python Academy - 2022\\JornadaPython-PythonAcademy\\Modulo13\\dados.txt', 'r')
#
# retorno = arquivo.read()
#
# print(retorno)

# Adicionar

# texto = '\n\nVenha dominar Python!'
#
# arquivo = open('D:\\Jornada Python - Python Academy - 2022\\JornadaPython-PythonAcademy\\Modulo13\\dados.txt', 'a')
#
# arquivo.write(texto)
#
# # Fechar arquivo
#
# arquivo.close()

# Arquivos Binários
# Abertura
arquivo_png = open('D:\\Jornada Python - Python Academy - 2022\\JornadaPython-PythonAcademy\\Modulo13\\logo.png', 'rb')

retorno_png = arquivo_png.read()

print(retorno_png)

# Criando arquivo
arquivo_saida = open('D:\\Jornada Python - Python Academy - 2022\\JornadaPython-PythonAcademy\\Modulo13\\logo_saida.png', 'wb')

arquivo_saida.write(retorno_png)

arquivo_saida.close()
arquivo_png.close()
