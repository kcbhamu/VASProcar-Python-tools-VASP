
import os
import sys
import site
import shutil

#---------------------------------------------------
# Obtendo o diretorio de instalação do VASProcar ---
#---------------------------------------------------

version = 'VASProcar_v1.0.84'

dir_inst = site.USER_SITE + '/vasprocar'

#----------------------------------------------------------------------
# Copiando a pasta VASProcar_v1.0.84 para o diretório de instalação ---
#----------------------------------------------------------------------

if os.path.isdir(dir_inst):
   shutil.rmtree(dir_inst)
else:
   0 == 0

shutil.copytree(version, dir_inst)

print("")
print("!!! Instalacao Concluida !!!")
print("")
print("===================================================================")
print("Para executar o codigo, utilize em qualquer diretorio que contenha ")
print("os arquivos de saida do VASP, o seguinte comando:                  ")
print("-------------------------------------------------                  ")
print("python -m vasprocar   ou   python3.? -m vasprocar                  ")
print("                                                                   ")
print("Substitua python3.? pela versao contida no Diretorio de Instalação ")
print(f'------------------------------------------------------------------')
print(f'{dir_inst}                                                        ')
print("===================================================================")
print("")

print("")
print("===================================================================")
print("Observacao:                                                        ")
print("Para o codigo funcionar corretamente, ele deve ter sido instalado  ")
print("em um diretorio do tipo:                                           ")
print("-------------------------------------------------------------------")
print("python/site-packages   ou   python3.?/site-packages                ")
print("-------------------------------------------------------------------")
print("Caso ele tenha sido instalado em um diretorio fora da instalacao   ")
print("do python, mova a pasta vasprocar para o diretorio correto.        ")
print("===================================================================")
print("")
