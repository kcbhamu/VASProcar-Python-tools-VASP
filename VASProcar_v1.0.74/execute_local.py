
import os
import sys
import shutil

dir_files = 'VASP_files'

#---------------------------------------------------------------------------
# Verificando se a pasta "VASP_files" existe, se não existe ela é criada ---
#---------------------------------------------------------------------------
if os.path.isdir(dir_files):
   0 == 0
else:
   os.mkdir(dir_files)
   print('')
   print('Insira os arquivos de saida do VASP na pasta: VASP_files')
   print('')
   exit()

#---------------------------------------------------------------------------
# Executando o VASProcar ---------------------------------------------------
#---------------------------------------------------------------------------
main_dir = 'src\\'
run = main_dir + '_settings.py'
exec(open(run).read())



