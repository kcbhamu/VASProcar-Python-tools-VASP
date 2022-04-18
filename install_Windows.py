
import os
import sys
import shutil

#---------------------------------------------------
# Obtendo o diretorio de instalação do VASProcar ---
#---------------------------------------------------

version = 'VASProcar_v1.0.75'

dir_inst = os.path.dirname(sys.executable) + '\Lib' + '\\vasprocar'

print('')
print('Diretorio de Instalacao: ')
print(dir_inst)
print('')

#----------------------------------------------------------------------
# Copiando a pasta VASProcar_v1.0.75 para o diretório de instalação ---
#----------------------------------------------------------------------

if os.path.isdir(dir_inst):
   shutil.rmtree(dir_inst)
else:
   0 == 0

shutil.copytree(version, dir_inst)

print('!!! Instalacao Concluida !!!')
print('')
print('Para executar o codigo, utilize em qualquer pasta contendo os arquivos de saida do VASP, o comando: python -m vasprocar')
print('')

