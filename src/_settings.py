
import shutil
import os

def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

from _printMessages import PrintMessages

# set GRACE variables
execute_python_file(filename = "_grace_settings.py")

#-----------------------------------------------------------------------
# Com relação ao parâmetro de rede, escolha: ---------------------------
#-----------------------------------------------------------------------
# [1] Utilizar o parâmetro informado no arquivo CONTCAR.
# [2] Adotar como parâmetro o menor valor entre os modulos dos vetores
#     primitivos da rede cristalina (A1, A2 e A3). 
#-----------------------------------------------------------------------
param_estim = 1

# -----------------------------------------------------------------------
# Com relação ao Plot dos Gráficos via Matplotlib, como deseja salvar?
# Marque [0] para desabilitar ou [1] para habilitar o respectivo formato
# -----------------------------------------------------------------------
save_png = 1
save_pdf = 0
save_eps = 0

# ----------------------------------------------------------------------
# Verificando se a pasta output existe, se não existe ela é criada -----
# ----------------------------------------------------------------------
if os.path.isdir("output"):
    0 == 0
else:
    os.mkdir("output")
# -------------------

# ----------------------------------------------------------------------
# Obtenção do nº de arquivos PROCAR a serem lidos: --------------------
# ----------------------------------------------------------------------

n_procar = 0

try:
    f = open('PROCAR')
    f.close()
    n_procar = 1
except:
    0 == 0

for i in range(1, 100):
    try:
        f = open('PROCAR.'+str(i))
        f.close()
        n_procar = i
    except:
        0 == 0

# get CONTCAR/PROCAR info.
PrintMessages.wait()
execute_python_file(filename = '/informacoes_b.py')

# -----------------------------------------------------------------------
# Obtenção dos parâmetros de input do código: --------------------------
# -----------------------------------------------------------------------

PrintMessages.general_info_part1()

if (SO == 2):
   PrintMessages.print_SO_information()
   
PrintMessages.general_info_part2()

escolha = input(" ")
escolha = int(escolha)
print(" ")

# ======================================================================

if (escolha == 1 or escolha == -1):
    print("##############################################################")
    print("###################### Escolha a opcao: ######################")
    print("##############################################################")
    print("## Plot 2D da Estrutura de Bandas: [k-points, E(eV)]        ##")
    print("## [1] Padrao   --   [-1] Personalizado                     ##")
    print("## ======================================================== ##")
    print("## Superficie de Fermi (Plot 2D):                           ##")
    print("## [10] Padrao  --   [-10] Personalizado                    ##")
    print("## ======================================================== ##")
    print("## Curvas de Nivel (Plot 2D e 3D) de uma dada Banda:        ##")
    print("## [11] Padrao  --   [-11] Personalizado                    ##")
    print("## ======================================================== ##")
    print("## Plot 3D da Estrutura de Bandas: [ki, kj, E(eV)]          ##")
    print("## [12] Padrao  --   [-12] Personalizado                    ##")
    print("## ======================================================== ##")
    print("## Isosuperficie das bandas: [kx, ky, kz, E(eV) ou dE(eV)]  ##")
    print("## [13] Padrao  --   [-13] Personalizado                    ##")
    print("##############################################################")
    escolha = input(" ")
    escolha = int(escolha)
    print(" ")

# ----------------------------------------------------------------------
# Copiando arquivo para a pasta de output: -----------------------------
# ----------------------------------------------------------------------

source = main_dir + '/etc/BibTeX.dat'
destination = 'output/BibTeX.dat'
shutil.copyfile(source, destination)

source = main_dir + '/etc/DOI.png'
destination = 'output/DOI.png'
shutil.copyfile(source, destination)

if (escolha == 1 or escolha == -1):
    execute_python_file(filename = '/bandas_2D.py')
    
if (escolha == 10 or escolha == -10):
    execute_python_file(filename = '/fermi_surface.py')
    
if (escolha == 11 or escolha == -11):
    execute_python_file(filename = '/level_countour.py')
    
if (escolha == 12 or escolha == -12):
    execute_python_file(filename = '/bandas_3D.py')
    
if (escolha == 13 or escolha == -13):
    execute_python_file(filename = '/bandas_4D.py')
    
if (escolha == 2 or escolha == -2):
    execute_python_file(filename = '/projecao_spin.py')
    
if (escolha == 21 or escolha == -21):
    execute_python_file(filename = '/spin_texture.py')

if (escolha == 22 or escolha == -22):
    execute_python_file(filename = '/spin_texture_contour.py')

if (escolha == 23 or escolha == -23):
    execute_python_file(filename = '/spin_texture_contour_video.py') 
        
if (escolha == 3 or escolha == -3):
    execute_python_file(filename = '/projecao_orbitais.py')
    
if (escolha == 4 or escolha == -4):
    execute_python_file(filename = '/dos_pdos_ldos.py')
    
if (escolha == 5 or escolha == -5):
    execute_python_file(filename = '/projecao_localizacao.py')
    
if (escolha == 6 or escolha == -6):
    execute_python_file(filename = '/contribuicao.py')
    
if (escolha == 7 or escolha == -7):
    execute_python_file(filename = '/potencial.py')
    
if (escolha == 8 or escolha == -8):
    execute_python_file(filename = '/parchg.py')
    
if (escolha == 9 or escolha == -9):
    execute_python_file(filename = '/WaveFunction.py')
    
if (escolha == 777 or escolha == -777):
    execute_python_file(filename = '/kpoints_malha_2D_3D.py')
    
if (escolha == 888 or escolha == -888):
    execute_python_file(filename = '/correction_file.py')
