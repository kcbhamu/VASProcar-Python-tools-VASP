
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
if os.path.isdir(dir_files + '\output'):
    0 == 0
else:
    os.mkdir(dir_files + '\output')
# ---------------------------------

# ----------------------------------------------------------------------
# Obtenção do nº de arquivos PROCAR a serem lidos: --------------------
# ----------------------------------------------------------------------

n_procar = 0

try:
    f = open(dir_files + '\PROCAR')
    f.close()
    n_procar = 1
except:
    0 == 0

for i in range(1, 100):
    try:
        f = open(dir_files + '\PROCAR.'+str(i))
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
print("################### O que deseja calcular? ###################")
print("##############################################################")
print("## [1] Estrutura de Bandas (Plot 2D, 3D, isosuperficie,     ##")
print("##                   Superficie de Fermi e Curvas de Nivel) ##")
print("## ======================================================== ##")  

if (SO == 2):
   print("## -------------------------------------------------------- ##")
   print("## Plot 2D das Componentes Sx|Sy|Sz em [k-points, E(eV)]    ##")
   print("## [2] Padrao   --   [-2] Personalizado                     ##")
   print("## -------------------------------------------------------- ##")
   print("## Projecoes 2D|3D|Isosuperficie das Componentes Sx|Sy|Sz   ##")
   print("## e dos vetores SiSj e SxSySz                              ##")
   print("## [21] Padrao  --   [-21] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Plot das Componentes Sx|Sy|Sz ao longo de uma dada Banda ##")
   print("## e Curva de Nivel (Energia constante).                    ##")
   print("## [22] Padrao  --   [-22] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Compilacao de um video que mostra a evolucao de uma dada ##")
   print("## Componente ou Vetor de Spin em funcao da Energia.        ##")
   print("## [23] Padrao  --   [-23] Personalizado                    ##")
   print("## ======================================================== ##")
   
print("## Projecao dos Orbitais S, P e D (Plot 2D):                ##")       
print("## [3]: Configuracao Padrao   --   [-3]: Personalizado      ##")
print("## ======================================================== ##")
print("## DOS, p-DOS e l-DOS (Plot 2D):                            ##")
print("## [4]: Configuracao Padrao   --   [-4]: Personalizado      ##")
print("## ======================================================== ##")
print("## Projecao da Localizacao dos estados em regioes (Plot 2D) ##")
print("## [5]: Configuracao Padrao   --   [-5]: Personalizado      ##")
print("## ======================================================== ##")
print("## Contribuicao de Orbitais e ions nos estados (Tabela):    ##")
print("## [6]: Configuracao Padrao   --   [-6]: Personalizado      ##")
print("## ======================================================== ##")
print("## Potencial Eletrostatico em X,Y,Z (Plot 2D):              ##")
print("## [7]: Configuracao Padrao   --   [-7]: Personalizado      ##")
print("## ======================================================== ##")
print("## Densidade de Carga Parcial em X,Y,Z (Plot 2D):           ##")
print("## [8]: Configuracao Padrao   --   [-8]: Personalizado      ##")
print("## ======================================================== ##")
print("##           !!!!! EM TESTES - Nao Funcional !!!!!          ##")
print("## Funcao de Onda em X,Y,Z - Parte Real e Imag. (Plot 2D):  ##")
print("## [9]: Configuracao Padrao   --   [-9]: Personalizado      ##")
print("## ======================================================== ##")
print("## [777] Gerar arquivo KPOINTS (Plano 2D ou Malha 3D na ZB) ##")
print("## ======================================================== ##")
print("## [888] Efetuar verificacao e correcao de arquivos do VASP ##")
print("##############################################################")

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

source = main_dir + '\etc\BibTeX.dat'
destination = dir_files + '\output\BibTeX.dat'
shutil.copyfile(source, destination)

source = main_dir + '\etc\DOI.png'
destination = dir_files + '\output\DOI.png'
shutil.copyfile(source, destination)

if (escolha == 1 or escolha == -1):
    execute_python_file(filename = 'bandas_2D.py')
    
if (escolha == 10 or escolha == -10):
    execute_python_file(filename = 'fermi_surface.py')
    
if (escolha == 11 or escolha == -11):
    execute_python_file(filename = 'level_countour.py')
    
if (escolha == 12 or escolha == -12):
    execute_python_file(filename = 'bandas_3D.py')
    
if (escolha == 13 or escolha == -13):
    execute_python_file(filename = 'bandas_4D.py')
    
if (escolha == 2 or escolha == -2):
    execute_python_file(filename = 'projecao_spin.py')
    
if (escolha == 21 or escolha == -21):
    execute_python_file(filename = 'spin_texture.py')

if (escolha == 22 or escolha == -22):
    execute_python_file(filename = 'spin_texture_contour.py')

if (escolha == 23 or escolha == -23):
    execute_python_file(filename = 'spin_texture_contour_video.py') 
        
if (escolha == 3 or escolha == -3):
    execute_python_file(filename = 'projecao_orbitais.py')
    
if (escolha == 4 or escolha == -4):
    execute_python_file(filename = 'dos_pdos_ldos.py')
    
if (escolha == 5 or escolha == -5):
    execute_python_file(filename = 'projecao_localizacao.py')
    
if (escolha == 6 or escolha == -6):
    execute_python_file(filename = 'contribuicao.py')
    
if (escolha == 7 or escolha == -7):
    execute_python_file(filename = 'potencial.py')
    
if (escolha == 8 or escolha == -8):
    execute_python_file(filename = 'parchg.py')
    
if (escolha == 9 or escolha == -9):
    execute_python_file(filename = 'WaveFunction.py')
    
if (escolha == 777 or escolha == -777):
    execute_python_file(filename = 'kpoints_malha_2D_3D.py')
    
if (escolha == 888 or escolha == -888):
    execute_python_file(filename = 'correction_file.py')
