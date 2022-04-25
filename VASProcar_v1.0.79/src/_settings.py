
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

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
if os.path.isdir(dir_files + '/output'):
    0 == 0
else:
    os.mkdir(dir_files + '/output')
# ---------------------------------

# ----------------------------------------------------------------------
# Verificando a presença dos arquivos CONTCAR, OUTCAR e PROCAR: --------
# ----------------------------------------------------------------------

n_contcar = 0

try:
    f = open(dir_files + '/CONTCAR')
    f.close()
    n_contcar = 1
except:
    print('')
    print('... Arquivo CONTCAR ausente ...')

#-----------------------------------

n_outcar = 0

try:
    f = open(dir_files + '/OUTCAR')
    f.close()
    n_outcar = 1
except:
    print('')
    print('... Arquivo OUTCAR ausente ...')

#-----------------------------------

n_procar = 0

try:
    f = open(dir_files + '/PROCAR')
    f.close()
    n_procar = 1
except:
    0 == 0

try:
    f = open(dir_files + '/PROCAR.1')
    f.close()
    n_procar = 1
except:
    0 == 0    

if (n_procar == 0):
   print('')
   print('... Arquivo PROCAR ausente ...')

#-----------------------------------

if (n_contcar == 0 or n_outcar == 0 or n_procar == 0):   
   print('')
   print('')
   print('---------------------------------------------------------------------------')
   print('Apos inserir os arquivos ausentes no diretorio, aperte ENTER para continuar')
   print('---------------------------------------------------------------------------')
   confirmacao = input (" "); confirmacao = str(confirmacao)
   
# ----------------------------------------------------------------------
# Verificando a presença e o nº de arquivos PROCAR a serem lidos: ------
# ----------------------------------------------------------------------

n_procar = 0

try:
    f = open(dir_files + '/PROCAR')
    f.close()
    n_procar = 1
except:
    0 == 0

for i in range(1, 100):
    try:
        f = open(dir_files + '/PROCAR.'+str(i))
        f.close()
        n_procar = i
    except:
        0 == 0

# Get CONTCAR/OUTCAR/PROCAR info. -------------------------------------

execute_python_file(filename = 'informacoes_b.py')

print("##############################################################")
print("# Obtendo informacoes da rede e do calculo efetuado: ======= #")
print("##############################################################")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(" ")

# -----------------------------------------------------------------------
# Obtenção dos parâmetros de input do código: --------------------------
# -----------------------------------------------------------------------

print("##############################################################")
print("################### O que deseja Analisar? ###################")
print("##############################################################")
print("## [1] Energia: Plot 2D, 3D, isosuperficie, Superficies de  ##")
print("##              Fermi e Curvas de Nivel                     ##")
print("## ======================================================== ##")  

if (SO == 2):
   print("## [2] Spin: Plot 2D, 3D, isosuperficie, Projecao sobre as  ##")
   print("##                                       Curvas de Nivel    ##")
   print("## ======================================================== ##") 

print("## [3] Projecao dos Orbitais e da Localizacao dos estados   ##")
print("##     na rede, Densidade de Estados (DOS, p-DOs, l-DOS)    ##")
print("## ======================================================== ##") 
print("## [4] Funcao de Onda, Densidade de Carga, Potencial        ##")
print("##     Eletrostatico, Funcao Dieletrica                     ##")
print("## ======================================================== ##")
print("## [888] Gerar arquivo KPOINTS (Plano 2D ou Malha 3D na ZB) ##")
print("## ======================================================== ##")
print("## [999] Verificar e corrigir arquivos do VASP (PROCAR)     ##")
print("##############################################################")

opcao = input(" ")
opcao = int(opcao)
print(" ")

# ======================================================================

if (opcao < 100):
   print("##############################################################")
   print("###################### Escolha a opcao: ######################")
   print("##############################################################")

if (opcao == 1 or opcao == -1):
   print("## Estrutura de Bandas - Plot 2D:  [k-path, E(eV)]          ##")
   print("## [10] Padrao   --   [-10] Personalizado                   ##")
   print("## ======================================================== ##")
   print("## Superficie de Fermi - Projecao 2D:  [ki, kj, E(eV)]      ##")
   print("## [11] Padrao  --   [-11] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Curvas de Nivel da Banda (Projecao 2D e Plot 3D):        ##")
   print("## [12] Padrao  --   [-12] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Estrutura de Bandas - Plot 3D: [ki, kj, E(eV)]           ##")
   print("## [13] Padrao  --   [-13] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Isosuperficies da banda:  [kx, ky, kz, E(eV) ou dE(eV)]  ##")
   print("## [14] Padrao  --   [-14] Personalizado                    ##")
   print("##############################################################")
   opcao = input(" ")
   opcao = int(opcao)
   print(" ")

if (opcao == 2 or opcao == -2):
   print("## Projecao 2D das Componentes Sx|Sy|Sz:  [k-path, E(eV)]   ##")
   print("## [20] Padrao   --   [-20] Personalizado                   ##")
   print("## ======================================================== ##")
   print("## Projecoes 2D|3D|Isosuperficie das Componentes Sx|Sy|Sz   ##")
   print("## e dos vetores SiSj e SxSySz                              ##")
   print("## [21] Padrao  --   [-21] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Plot das Componentes Sx|Sy|Sz e vetores SiSj ao longo de ##")
   print("## uma dada Banda e Curva de Nivel (Energia constante)      ##")
   print("## [22] Padrao  --   [-22] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Video mostrando a evolucao de Sx|Sy|Sz ou vetores SiSj   ##")
   print("## em funcao da Energia (Curvas de Nível).                  ##")
   print("## [23] Padrao  --   [-23] Personalizado                    ##")
   print("##############################################################")   
   opcao = input(" ")
   opcao = int(opcao)
   print(" ")
   
if (opcao == 3 or opcao == -3):
   print("## Projecao 2D dos Orbitais S, P e D:  [k-path, E(eV)]      ##")       
   print("## [30] Padrao   --   [-30] Personalizado                   ##")
   print("## ======================================================== ##")
   print("## DOS, p-DOS e l-DOS (Plot 2D)                             ##")
   print("## [31] Padrao   --   [-31] Personalizado                   ##")
   print("## ======================================================== ##")
   print("## Projecao 2D da Localizacao das Bandas em regioes da rede ##")
   print("## [32] Padrao   --   [-32] Personalizado                   ##")
   print("## ======================================================== ##")
   print("## Contribuicao dos Orbitais e ions nos estados:  (Tabela)  ##")
   print("## [33] Padrao   --   [-33] Personalizado                   ##")
   print("##############################################################") 
   opcao = input(" ")
   opcao = int(opcao)
   print(" ")
   
if (opcao == 4 or opcao == -4):
   print("## Potencial Eletrostatico em X,Y,Z - Plot 2D               ##")
   print("## [40] Padrao   --   [-40] Personalizado                   ##")
   print("## ======================================================== ##")
   print("## Densidade de Carga Parcial em X,Y,Z - Plot 2D            ##")
   print("## [41] Padrao   --   [-41] Personalizado                   ##")
   print("## ======================================================== ##")
   print("## Funcao Dieletrica em X,Y,Z (Real e Imaginaria) - Plot 2D ##")
   print("## [42] Padrao   --   [-42] Personalizado                   ##")
   print("## ======================================================== ##")
   print("##           !!!!! EM TESTES - Nao Funcional !!!!!          ##")
   print("## Funcao de Onda em X,Y,Z (Real e Imaginaria) - Plot 2D    ##")
   print("## [43] Padrao   --   [-43] Personalizado                   ##")
   print("##############################################################")
   opcao = input(" ")
   opcao = int(opcao)
   print(" ")
   
# ----------------------------------------------------------------------
# Copiando arquivo para a pasta de output: -----------------------------
# ----------------------------------------------------------------------

source = main_dir + '/etc/BibTeX.dat'
destination = dir_files + '/output/BibTeX.dat'
shutil.copyfile(source, destination)

source = main_dir + '/etc/DOI.png'
destination = dir_files + '/output/DOI.png'
shutil.copyfile(source, destination)

#--------------------------------
escolha = opcao/((opcao**2)**0.5)
#--------------------------------

if (opcao == 10 or opcao == -10):
    execute_python_file(filename = 'bandas_2D.py')
    
if (opcao == 11 or opcao == -11):
    execute_python_file(filename = 'fermi_surface.py')
    
if (opcao == 12 or opcao == -12):
    execute_python_file(filename = 'level_countour.py')
    
if (opcao == 13 or opcao == -13):
    execute_python_file(filename = 'bandas_3D.py')
    
if (opcao == 14 or opcao == -14):
    execute_python_file(filename = 'bandas_4D.py')
    
if (opcao == 20 or opcao == -20):
    execute_python_file(filename = 'projecao_spin.py')
    
if (opcao == 21 or opcao == -21):
    execute_python_file(filename = 'spin_texture.py')

if (opcao == 22 or opcao == -22):
    execute_python_file(filename = 'spin_texture_contour.py')

if (opcao == 23 or opcao == -23):
    execute_python_file(filename = 'spin_texture_contour_video.py') 
        
if (opcao == 30 or opcao == -30):
    execute_python_file(filename = 'projecao_orbitais.py')
    
if (opcao == 31 or opcao == -31):
    execute_python_file(filename = 'dos_pdos_ldos.py')
    
if (opcao == 32 or opcao == -32):
    execute_python_file(filename = 'projecao_localizacao.py')
    
if (opcao == 33 or opcao == -33):
    execute_python_file(filename = 'contribuicao.py')
    
if (opcao == 40 or opcao == -40):
    execute_python_file(filename = 'potencial.py')
    
if (opcao == 41 or opcao == -41):
    execute_python_file(filename = 'parchg.py')

if (opcao == 42 or opcao == -42):
    execute_python_file(filename = 'dielectric_function.py')
    
if (opcao == 43 or opcao == -43):
    execute_python_file(filename = 'wave_function.py')
    
if (opcao == 888 or opcao == -888):
    execute_python_file(filename = 'kpoints_2D_3D.py')
    
if (opcao == 999 or opcao == -999):
    execute_python_file(filename = 'correction_file.py')