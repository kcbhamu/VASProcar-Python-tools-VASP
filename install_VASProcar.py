
import os
import sys
import site
import shutil

#---------------------------------------------------
# Obtendo o diretorio de instalação do VASProcar ---
#---------------------------------------------------

version = 'VASProcar_v1.0.80'

dir_inst = site.USER_SITE + '/vasprocar'

print("")
print("Diretorio de Instalacao:")
print(dir_inst)
print("")

#----------------------------------------------------------------------
# Copiando a pasta VASProcar_v1.0.77 para o diretório de instalação ---
#----------------------------------------------------------------------

if os.path.isdir(dir_inst):
   shutil.rmtree(dir_inst)
else:
   0 == 0

shutil.copytree(version, dir_inst)

print("!!! Instalacao Concluida !!!")
print("")
print("Para executar o codigo, utilize em qualquer pasta contendo os arquivos de saida do VASP, o comando: python -m vasprocar")
print("")

print("")
print("=================================================================")
print("Observacao:                                                      ")
print("Para o codigo funcionar corretamente, ele deve ter sido instalado")
print("em um diretorio do tipo:                                         ")
print("-----------------------------------------------------------------")
print("python/Lib/site-packages                                         ")
print("python3.?/Lib/site-packages                                      ")
print("-----------------------------------------------------------------")
print("Caso ele tenha sido instalado em um diretorio fora da instalacao ")
print("do python, mova a pasta vasprocar para o diretorio correto.      ")
print("=================================================================")
print("")
