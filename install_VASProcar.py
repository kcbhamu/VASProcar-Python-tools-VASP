
import os
import sys
import site
import shutil
import subprocess

#---------------------------------------------------
# Obtendo o diretorio de instalação do VASProcar ---
#---------------------------------------------------

version = 'VASProcar_v1.0.85'

dir_inst = site.USER_SITE + '/vasprocar'

#----------------------------------------------------------------------
# Copiando a pasta VASProcar_v1.0.85 para o diretório de instalação ---
#----------------------------------------------------------------------

if os.path.isdir(dir_inst):
   shutil.rmtree(dir_inst)
else:
   0 == 0

shutil.copytree(version, dir_inst)

print("")
print("##################################")
print("###### Instalacao Concluida ######")
print("##################################")
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

#----------------------------------------------------------------------
# Instalação/Atualização de Modulos -----------------------------------
#----------------------------------------------------------------------

print("===================================================================")
print("Deseja Instalar/Atualizar os modulos necessarios a correta execucao")
print("de todas as funcionalidades do VASProcar ?                         ")
print("-------------------------------------------------------------------")
print("[0] NAO                                                            ")
print("[1] SIM                                                            ")
print("===================================================================")
modulos = input(" "); modulos = int(modulos)
print(" ")

if (modulos == 1):

   # ---------------------------------------------------------
   # package_list_to_instal ----------------------------------
   # ---------------------------------------------------------
   
   packages = [
   "pip",
   "os", 
   "sys",
   "shutil",
   "numpy", 
   "scipy", 
   "matplotlib", 
   "plotly",
   "moviepy"
   ]

   for i in range(len(packages)):
       subprocess.run(["pip", "install", "--upgrade", packages[i]])
       print("[OK] " + packages[i])

   print(" ")
   print("##########################################################")
   print("###### Instalação/Atualização dos Modulos concluida ######")
   print("##########################################################")
   print(" ")
